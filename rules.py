import pandas as pd

# Simple rule-based fraud checks for the Kaggle creditcard.csv dataset

def flag_high_value(df, threshold=1000):
    # Flag any transaction above the threshold (default = $1,000)
    return df['Amount'] > threshold

def flag_odd_hours(df, start=0, end=5):
    # Convert "Time" (in seconds) into hour of the day
    hours = (df['Time'] % 86400 // 3600)
    # Flag transactions that happen between midnight and 5AM
    return hours.between(start, end)

def apply_rules(df):
    # Apply both rules and add results as new columns
    df['Flag_HighValue'] = flag_high_value(df)
    df['Flag_OddHours'] = flag_odd_hours(df)

    # Mark as "Potential Fraud" if any rule is triggered
    df['Potential_Fraud'] = df[['Flag_HighValue','Flag_OddHours']].any(axis=1)
    return df

