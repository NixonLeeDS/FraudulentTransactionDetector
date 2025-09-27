# Fraudulent Transaction Detector

A simple Python-based tool to detect potentially fraudulent transactions using rule-based methods inspired by AML/CFT compliance. Includes a Streamlit dashboard for visualization.

---

## Features
- Load and analyze transaction datasets (CSV)
- Rule-based anomaly detection:
  - High-value transactions
  - Odd-hour transactions
- Interactive dashboard with Streamlit
- Export flagged transactions as CSV

---

## Tech Stack
- Python, pandas, matplotlib
- Streamlit (for frontend)

---

## How to Run
1. Clone the repo:
   ```bash
   git clone https://github.com/NixonLeeDS/FraudulentTransactionDetector
   cd fraudulent-transaction-detector
   ```
2. Install dependencies:
    ```bash
   pip install -r requirements.txt
    ```
3. Run app:
   ```bash
   streamlit run app.py
   ```
