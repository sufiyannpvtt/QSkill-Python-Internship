import os
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import joblib

def train_model(data_path):
    df = pd.read_csv(data_path)

    X = df.drop("Price", axis=1)
    y = df["Price"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = LinearRegression()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    metrics = {
        "MAE": mean_absolute_error(y_test, y_pred),
        "RMSE": mean_squared_error(y_test, y_pred) ** 0.5,
        "R2": r2_score(y_test, y_pred)
    }

    # ensure dirs
    os.makedirs("projects/02_House_Price_Prediction/models", exist_ok=True)
    os.makedirs("projects/02_House_Price_Prediction/outputs", exist_ok=True)

    # save model
    joblib.dump(model, "projects/02_House_Price_Prediction/models/linear_regression.pkl")

    # save metrics
    with open("projects/02_House_Price_Prediction/outputs/accuracy_report.txt", "w") as f:
        for k, v in metrics.items():
            f.write(f"{k}: {v:.4f}\n")

    print("Training completed.")
    print(metrics)

    return model, metrics, X_test, y_test, y_pred


if __name__ == "__main__":
    train_model(
        "projects/02_House_Price_Prediction/data/processed/house_prices_cleaned.csv"
    )
