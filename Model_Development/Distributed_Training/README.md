# Distributed Training with Ray and PyTorch

Distributed data-parallel training using **Ray Train** and **PyTorch** on the **Wine Quality dataset**.

## Introduction

A multi-layer perceptron (MLP) that classifies wine cultivars (3 classes, 13 features) — trained across 2 parallel workers using synchronous gradient averaging.

## Prerequisites

```bash
pip install "ray[train]" torch scikit-learn pandas
```

## Run

```bash
jupyter notebook ray_pytorch.ipynb
```

