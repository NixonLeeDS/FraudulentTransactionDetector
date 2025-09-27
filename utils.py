import pandas as pd



def load_data(file):
    """
    Load CSV file into a pandas DataFrame.
    """
    return pd.read_csv(file)


def save_results(df, filename="outputs/flagged_transactions.csv"):
    """
    Save dataframe with fraud flags to CSV.
    """
    df.to_csv(filename, index=False)
