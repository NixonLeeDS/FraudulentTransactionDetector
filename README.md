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
   python -m streamlit run app.py
   ```




## Dataset
This project uses the Credit Card Fraud Detection dataset from Kaggle

Note: The dataset is not included in this repository because it is larger than GitHub’s 100 MB file limit.

How to set it up
1. Download the dataset from Kaggle:
https://www.kaggle.com/mlg-ulb/creditcardfraud
2. Extract the creditcard.csv file.
3. Place it inside the data/ folder of this project:
4. Start the app and upload the file through the Streamlit interface, or let the app load it from the data/ folder if configured.




Example Output

-Flagged suspicious transactions in a table view
-Bar chart comparing flagged vs non-flagged transactions
- Summary of total fraud cases vs frauds caught by rules

<img width="678" height="455" alt="image" src="https://github.com/user-attachments/assets/438ae3eb-2d59-4507-a1d0-39f9c7f69f73" />
<img width="694" height="721" alt="image" src="https://github.com/user-attachments/assets/ed99d596-cefc-4833-b126-f422b91c70ee" />

