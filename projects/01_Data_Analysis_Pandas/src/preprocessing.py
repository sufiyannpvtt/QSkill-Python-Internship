import pandas as pd

def preprocess_data(input_path, output_path):
    df = pd.read_csv(input_path)

    # Log initial shape
    initial_shape = df.shape

    # Fill missing Study_Hours with median
    df["Study_Hours"] = df["Study_Hours"].fillna(df["Study_Hours"].median())


    # Remove duplicates
    df.drop_duplicates(inplace=True)

    # Convert data types
    df["Attendance"] = df["Attendance"].astype(int)

    # Save cleaned data
    df.to_csv(output_path, index=False)

    return initial_shape, df.shape
