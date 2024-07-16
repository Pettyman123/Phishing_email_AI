import pandas as pd

def load_data(filepath):
    return pd.read_csv(filepath)

def preprocess_text(text_data, fillna=True):
    # Fill NaNs with empty string or handle as necessary
    if fillna:
        text_data = text_data.fillna("")
    # Add more preprocessing steps as needed (e.g., lowercasing, removing punctuation, etc.)
    # Example: text_data = text_data.str.lower()
    return text_data

