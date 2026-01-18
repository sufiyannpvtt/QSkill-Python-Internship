import os
import pandas as pd
import matplotlib.pyplot as plt
import joblib
from sklearn.model_selection import train_test_split

def evaluate_model(data_path, model_path):
    # Load data
    df = pd.read_csv(data_path)

    X = df.drop("Price", axis=1)
    y = df["Price"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Load trained model
    model = joblib.load(model_path)

    # Predict
    y_pred = model.predict(X_test)

    # LOCK: ensure outputs directory exists
    output_dir = "projects/02_House_Price_Prediction/outputs"
    os.makedirs(output_dir, exist_ok=True)

    # Plot
    plt.figure(figsize=(6, 6))
    plt.scatter(y_test, y_pred)
    plt.xlabel("Actual Price")
    plt.ylabel("Predicted Price")
    plt.title("Actual vs Predicted House Prices")

    output_path = os.path.join(output_dir, "prediction_plot.png")
    plt.savefig(output_path)
    plt.close()

    print(f"Evaluation completed. Plot saved at: {output_path}")

if __name__ == "__main__":
    evaluate_model(
        "projects/02_House_Price_Prediction/data/processed/house_prices_cleaned.csv",
        "projects/02_House_Price_Prediction/models/linear_regression.pkl"
    )
