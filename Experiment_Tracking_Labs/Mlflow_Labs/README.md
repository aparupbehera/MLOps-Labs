# Diabetes Prediction with PyTorch + MLflow

MLflow experiment tracking, model registration, and serving using a PyTorch MLP on the Pima Indians Diabetes dataset.
Objective is to run two models (baseline and larger mlp) and compare them on MLflow 
## Requirements

```bash
pip install mlflow torch scikit-learn pandas numpy requests
```

## Dataset

[Pima Indians Diabetes](https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv) — loaded automatically in the notebook. 768 samples, 8 numeric features, binary outcome.

## Lab Steps
Run the notebook cells

## Running the MLflow UI

```bash
mlflow ui
```
Open [http://localhost:5000](http://localhost:5000) to compare experiments.

## Serving the Model

```bash
mlflow models serve -m models:/diabetes_mlp/production -h 0.0.0.0 -p 5001 --no-conda
```