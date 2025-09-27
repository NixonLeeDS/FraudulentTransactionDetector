import streamlit as st
import matplotlib.pyplot as plt
from rules import apply_rules
from utils import load_data, save_results

# ---------------------------
# Streamlit App
# ---------------------------

st.title("💳 Credit Card Fraud Detector (Rule-Based)")

# File uploader for CSV
uploaded_file = st.file_uploader("Upload the Kaggle creditcard.csv file", type="csv")

if uploaded_file:
    # Step 1: Load dataset
    df = load_data(uploaded_file)

    # Step 2: Apply fraud detection rules
    df = apply_rules(df)

    # Step 3: Show flagged transactions
    st.subheader("🚨 Flagged Transactions (Rule-Based)")
    st.dataframe(df[df['Potential_Fraud']])

    # Step 4: Visualization - Fraud vs Non-Fraud (based on rules)
    st.subheader("📊 Fraud vs Non-Fraud (Rule-Based)")
    fig, ax = plt.subplots()
    df['Potential_Fraud'].value_counts().plot(kind='bar', ax=ax)
    ax.set_xticklabels(['Legit', 'Potential Fraud'], rotation=0)
    st.pyplot(fig)

    # Step 5: Compare with true fraud labels in dataset
    if 'Class' in df.columns:
        st.subheader("✅ Comparison with True Fraud Labels")
        true_frauds = df[df['Class'] == 1]
        flagged_frauds = df[(df['Potential_Fraud'] == True) & (df['Class'] == 1)]

        st.write("Total Frauds in Dataset:", len(true_frauds))
        st.write("Frauds Flagged by Rules:", len(flagged_frauds))

    # Step 6: Option to save results
    if st.button("Save flagged transactions"):
        save_results(df)
        st.success("Results saved to outputs/flagged_transactions.csv")
