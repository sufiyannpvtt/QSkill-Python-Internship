import pandas as pd

def load_data(path):
    df = pd.read_csv(path)
    return df

if __name__ == "__main__":
    df = load_data("projects/02_House_Price_Prediction/data/raw/house_prices_raw.csv")

    print("First 5 rows:")
    print(df.head())

    print("\nDataset Info:")
    print(df.info())

    print("\nStatistical Summary:")
    print(df.describe())
