# Lab 1: Text Analyzer - ML Application with CI/CD

A simple machine learning text analysis application with automated testing using **pytest** and **unittest** through **GitHub Actions**.

---

## Project Overview

This project demonstrates:
- **Text analysis functionality** using Python
- **Automated testing** with pytest and unittest frameworks
- **CI/CD pipeline** using GitHub Actions

---

## Project Structure

```
Github_Labs/
└── Lab1/
    ├── data/
    │   └── __init__.py
    ├── src/
    │   ├── __init__.py
    │   └── text_analyzer.py       
    ├── test/
    │   ├── __init__.py
    │   ├── test_pytest.py         # pytest test cases
    │   └── test_unittest.py       # unittest test cases
    ├
    ├── README.md
    └── requirements.txt            
└──.github/
       └── workflows/
           ├── github_lab1_pytest_action.yml      # pytest CI workflow
           └── github_lab2_unittest_action.yml    # unittest CI workflow    
```


## Setup

2. **Create virtual environment** (recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

---

## Running Tests

### Run pytest tests
```bash
# Run all pytest tests
pytest test/test_pytest.py

# Run with verbose output
pytest test/test_pytest.py -v
```

### Run unittest tests
```bash
# Run all unittest tests
python -m unittest test/test_unittest

# Run with verbose output
python -m unittest test/test_unittest -v
```

## 🔄 GitHub Actions Workflow files

### `github_lab1_pytest_action.yml`
### `github_lab2_unittest_action.yml`

**Triggers:**
- Push to main branch
-----
