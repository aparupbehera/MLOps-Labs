# Record Matching with ELK Stack

Record Matching using Random Forest on the FEBRL4 benchmark dataset — Monitored with ELK Stack


---

## What It Does

1. **Loads** the FEBRL4 dataset — two sets of 5000 synthetic person records with ~3000 known true matches.
2. **Blocks** candidate pairs by postcode, reducing the comparison space from ~25M to a tractable subset.
3. **Featurizes** each candidate pair using 6 similarity metrics:
   - Jaro-Winkler on given name and surname
   - Soundex phonetic match on surname
   - Exact DOB match
   - Fuzzy suburb similarity
   - Exact postcode match
4. **Trains** a Random Forest classifier (class-balanced) on 70% of candidates and runs batch inference** every 60 seconds, injecting increasing feature noise to simulate data drift.
5. **Logs** all metrics as structured JSON → Logstash → Elasticsearch → Kibana.

---

## Directory Structure

```
record-matching-elk/
├── docker-compose.yml     
├── metricbeat.yml          
├── requirements.txt     
├── record_matching.py      
├── README.md               
└── logstash/
    └── logstash.conf 
```

---

## Prerequisites

- Ubuntu (20.04+)
- Docker & Docker Compose
- Python 3.8+

---

## Setup & Run

### 1. Install Python dependencies

```bash
pip3 install -r requirements.txt
```

### 2. Start the ELK stack

```bash
docker-compose up -d
```

Wait a few seconds, verify Elasticsearch is up:

```bash
curl http://localhost:9200
```

### 3. Run the pipeline

```bash
python3 record_matching.py
```

The script runs emitting one batch per minute. Logs are written to `logstash/record_matching.log` and automatically picked up by Logstash.

---

## Kibana Setup

1. Open `http://localhost:5601`
2. Go to **Stack Management → Index Patterns → Create index pattern**
3. Add patterns like: `record-matching-*`, time field: `@timestamp`
4. Go to **Discover** to check all matching events 
