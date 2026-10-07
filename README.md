# AI University Projects (BSCS, 6th Semester)

This repository contains written project documents for the Artificial Intelligence course:

1. [AI-Based Phishing Detection Agent](#1-ai-based-phishing-detection-agent)
2. [Jos Buttler T20I Runs Prediction Using Supervised Learning](#2-jos-buttler-t20i-runs-prediction-using-supervised-learning)

No setup or installation is required. These are written project documents, not running applications.

---

## 1. AI-Based Phishing Detection Agent

An AI university project that analyzes a URL and classifies it as Legitimate or Phishing, then warns the user if the link is malicious. It is built for the Pakistani context, where phishing attacks via SMS, WhatsApp, and email are a growing threat to online banking and mobile wallet users.

### 📌 Overview

Phishing websites trick users into revealing passwords, banking details, and other sensitive information by imitating trusted brands. This project models an intelligent agent that:

- Takes a URL as input
- Extracts key features (domain, length, symbols, HTTPS usage, etc.)
- Classifies the URL as Legitimate or Phishing
- Warns the user in real time if the URL is malicious

```
URL → Feature Analysis → AI Agent → Decision → Legitimate / Phishing → User Warning
```

### 📄 Contents

| File | Description |
|------|-------------|
| `AI_Phishing_Detection_Agent.docx` | Full project report (Word format) |
| `AI_Phishing_Detection_Agent.pdf` | Full project report (PDF format) |

### 📚 Report Sections

- Introduction
- Problem Statement (phishing in Pakistan)
- Proposed AI Solution
- Problem Formulation (initial state, goal state, inputs, actions, outcomes)
- Simple Graphical Diagram
- Environment Creation
- PEAS Analysis
- Environment Properties
- Simple Example
- Conclusion

---

## 2. Jos Buttler T20I Runs Prediction Using Supervised Learning

*A Machine Learning Approach for Predicting Cricket Player Performance*

A project proposal that predicts how many runs Jos Buttler (England, batter / wicketkeeper-batter) will score in his next T20 International match, using supervised machine learning on his historical T20I match-by-match performances.

### 📌 Overview

Cricket performance depends on many factors at once (opposition, venue, batting position, recent form), which makes it hard to predict by hand. This project plans a regression model that learns patterns from past matches, where the actual runs are known, and uses them to estimate runs in a future match.

| Item | Detail |
|------|--------|
| Learning type | Supervised Learning |
| Problem type | Regression |
| Target variable | Runs |
| Main model | Decision Tree Regressor |
| Optional comparison | Random Forest Regressor |
| Domain | Cricket / Sports Analytics |
| Evaluation metrics | MAE, RMSE, R² |

```
Historical T20I data → Preprocessing → Feature Engineering → Train/Test Split
→ Decision Tree Regressor → Evaluation (MAE, RMSE, R²) → Future Runs Prediction
```

### 📄 Contents

| File | Description |
|------|-------------|
| `Jos_Buttler_T20I_Runs_Prediction.pdf` | Detailed project proposal (16 pages) |
| `Jos_Buttler_OnePage.pdf` | One-page A4 summary of the proposal |

### 📚 Report Sections (detailed PDF)

- Project Overview and Selected Player
- Learning Problem Definition (Task, Experience, Performance Measure)
- Learning Domain and Problem Statement
- Project Workflow with flow diagram
- Data Collection, Dataset Metadata and Data Sources
- Dataset Features and Target Variable
- Data Preprocessing and Missing Value Analysis
- Feature Engineering (Previous Match Runs, Last 3 / Last 5 Match Average, Historical Average, Recent Form)
- Feature Selection and Categorical Encoding
- Data Splitting (chronological: older matches for training, newer for testing)
- Model Selection (Decision Tree Regressor, Random Forest comparison)
- Model Training and Testing (scikit-learn code outline)
- Performance Evaluation (MAE, RMSE, R² with formulas)
- Visualization Plan and Decision Tree Interpretation
- Final Prediction
- Data Leakage and Model Validity
- Limitations, Ethical / Academic Considerations, Expected Outcome
- Conclusion and References

### 📊 Data Sources

| Role | Source |
|------|--------|
| Primary data source | [Cricsheet](https://cricsheet.org/) |
| Verification | [ESPNcricinfo](https://www.espncricinfo.com/) and [Statsguru](https://stats.espncricinfo.com/) |
| Secondary | [Kaggle](https://www.kaggle.com/), [GitHub](https://github.com/) |

The exact dataset link will be added once the final dataset is selected.

### ⚠️ Project Status

This is a **proposal**. It describes the planned methodology only. No model has been trained, so there are no results yet: MAE, RMSE, R², tree rules and the final predicted runs are all **to be calculated after model training**. Any examples labelled "Hypothetical" in the report are for explanation only and are not real data.

---

## 🎓 Course

BSCS — Artificial Intelligence course projects.

## 📥 Usage

Download the `.docx` or `.pdf` files to view the reports. No setup or installation is required.

## ✍️ Author

Asif — BSCS, 6th Semester (AI & Cybersecurity)
