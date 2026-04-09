import json
import logging
import time
import numpy as np
import jellyfish
from rapidfuzz import fuzz
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score, precision_score, recall_score
from datetime import datetime, timedelta
from recordlinkage.datasets import load_febrl4

logging.basicConfig(
    filename='logstash/record_matching.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

FEATURE_NAMES = ['given_name_jw', 'surname_jw', 'surname_soundex', 'dob_exact', 'suburb_sim', 'postcode_exact']

def safe(v):
    return '' if v is None or (isinstance(v, float) and np.isnan(v)) else str(v)

def compute_features(rA, rB):
    gn  = jellyfish.jaro_winkler_similarity(safe(rA.given_name), safe(rB.given_name))
    sn  = jellyfish.jaro_winkler_similarity(safe(rA.surname),    safe(rB.surname))
    snx = float(jellyfish.soundex(safe(rA.surname) or 'X') == jellyfish.soundex(safe(rB.surname) or 'X'))
    dob = float(safe(rA.date_of_birth) != '' and safe(rA.date_of_birth) == safe(rB.date_of_birth))
    sub = fuzz.ratio(safe(rA.suburb),   safe(rB.suburb))   / 100.0
    pc  = float(safe(rA.postcode) == safe(rB.postcode))
    return [gn, sn, snx, dob, sub, pc]

def train(X, y):
    clf = RandomForestClassifier(n_estimators=100, class_weight='balanced', random_state=42)
    clf.fit(X, y)
    logging.info(json.dumps({"event": "training_complete", "samples": len(X), "positive_rate": round(float(y.mean()), 3)}))
    return clf

logging.info(json.dumps({"event": "data_load_start"}))
dfA, dfB, true_links = load_febrl4(return_links=True)

ids_A = list(dfA.index)
ids_B = list(dfB.index)
true_set = set(map(tuple, true_links.tolist()))

logging.info(json.dumps({"event": "data_loaded", "records_A": len(dfA), "records_B": len(dfB), "true_matches": len(true_set)}))

X_all, y_all = [], []

for (idxA, idxB) in true_set:
    X_all.append(compute_features(dfA.loc[idxA], dfB.loc[idxB]))
    y_all.append(1)

# Negatives: random pairs
rng = np.random.default_rng(42)
target_neg = len(true_set) * 4
sampled = 0
while sampled < target_neg:
    idxA = ids_A[rng.integers(len(ids_A))]
    idxB = ids_B[rng.integers(len(ids_B))]
    if (idxA, idxB) not in true_set:
        X_all.append(compute_features(dfA.loc[idxA], dfB.loc[idxB]))
        y_all.append(0)
        sampled += 1

X_all = np.array(X_all)
y_all = np.array(y_all)
logging.info(json.dumps({"event": "dataset_built", "total_pairs": len(y_all), "positive_rate": round(float(y_all.mean()), 3)}))

X_train, X_test, y_train, y_test = train_test_split(
    X_all, y_all, test_size=0.3, random_state=42, stratify=y_all
)
model = train(X_train, y_train)

BATCH_SIZE = 300
n_batches  = len(X_test) // BATCH_SIZE
end_time   = datetime.now() + timedelta(minutes=20)
batch_id   = 0

while datetime.now() < end_time and batch_id < n_batches:
    start   = (batch_id * BATCH_SIZE) % len(X_test)
    X_batch = X_test[start:start + BATCH_SIZE].copy()
    y_batch = y_test[start:start + BATCH_SIZE]

    # Drift: corrupt random features with increasing probability
    drift_rate = min(batch_id * 0.02, 0.30)
    if drift_rate > 0:
        mask = np.random.random(X_batch.shape) < drift_rate
        X_batch[mask] = np.random.random(mask.sum())

    preds       = model.predict(X_batch)
    importances = dict(zip(FEATURE_NAMES, model.feature_importances_.round(3).tolist()))

    logging.info(json.dumps({
        "event":               "batch_result",
        "batch_id":            batch_id,
        "drift_rate":          round(drift_rate, 3),
        "f1":                  round(f1_score(y_batch, preds, average='weighted', zero_division=0), 3),
        "precision":           round(precision_score(y_batch, preds, average='weighted', zero_division=0), 3),
        "recall":              round(recall_score(y_batch, preds, average='weighted', zero_division=0), 3),
        "match_ratio":         round(float(preds.sum() / len(preds)), 3),
        "feature_importances": importances,
    }))

    if drift_rate > 0.15:
        logging.warning(json.dumps({
            "event":      "drift_alert",
            "batch_id":   batch_id,
            "drift_rate": round(drift_rate, 3),
        }))

    # Retrain every 5 batches on a fresh random split
    if batch_id > 0 and batch_id % 5 == 0:
        X_r, _, y_r, _ = train_test_split(
            X_all, y_all, test_size=0.3, random_state=batch_id, stratify=y_all
        )
        model = train(X_r, y_r)
        logging.info(json.dumps({"event": "retrain", "batch_id": batch_id}))

    batch_id += 1
    time.sleep(60)

logging.info(json.dumps({"event": "run_complete", "total_batches": batch_id}))