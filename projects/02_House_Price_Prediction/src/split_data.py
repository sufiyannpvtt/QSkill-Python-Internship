import pandas as pd
from sklearn.model_selection import train_test_split

def split_data(data_path):
    df = pd.read_csv(data_path)

    X = df.drop("Price", axis=1)
    y = df["Price"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    print("Train shape:", X_train.shape)
    print("Test shape:", X_test.shape)

    return X_train, X_test, y_train, y_test


if __name__ == "__main__":
    split_data(
        "projects/02_House_Price_Prediction/data/processed/house_prices_cleaned.csv"
    )
