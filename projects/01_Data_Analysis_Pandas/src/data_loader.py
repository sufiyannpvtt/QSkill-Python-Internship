import pandas as pd

def load_data(file_path):
    """
    Loads CSV data into a Pandas DataFrame
    """
    df = pd.read_csv(file_path)
    return df


def clean_data(df):
    """
    Performs basic data cleaning
    """
    # Remove duplicate rows
    df = df.drop_duplicates()

    # Handle missing values
    df = df.fillna(method="ffill")

    return df
