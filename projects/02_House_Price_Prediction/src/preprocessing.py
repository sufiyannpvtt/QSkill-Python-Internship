import pandas as pd

def preprocess_data(input_path, output_path):
    df = pd.read_csv(input_path)

    # Handle missing values (future-proof)
    df.fillna(df.median(numeric_only=True), inplace=True)

    # Encode categorical column: Location
    df = pd.get_dummies(df, columns=["Location"], drop_first=True)

    # Save cleaned dataset
    df.to_csv(output_path, index=False)

    return df

if __name__ == "__main__":
    cleaned_df = preprocess_data(
        "projects/02_House_Price_Prediction/data/raw/house_prices_raw.csv",
        "projects/02_House_Price_Prediction/data/processed/house_prices_cleaned.csv"
    )

    print("Cleaned Data Preview:")
    print(cleaned_df.head())
