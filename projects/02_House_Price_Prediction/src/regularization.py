import os
import pandas as pd
from sklearn.linear_model import Ridge, Lasso
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

def train_regularized_models(data_path):
    df = pd.read_csv(data_path)

    X = df.drop("Price", axis=1)
    y = df["Price"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    models = {
        "Ridge": Ridge(alpha=1.0),
        "Lasso": Lasso(alpha=0.1)
    }

    results = {}

    for name, model in models.items():
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)

        results[name] = {
            "MAE": mean_absolute_error(y_test, y_pred),
            "RMSE": mean_squared_error(y_test, y_pred) ** 0.5,
            "R2": r2_score(y_test, y_pred)
        }

        print(f"\n{name} Regression Results:")
        for k, v in results[name].items():
            print(f"{k}: {v:.4f}")

        # Print coefficients (important)
        print("Coefficients:")
        for feature, coef in zip(X.columns, model.coef_):
            print(f"  {feature}: {coef:.2f}")

    # Save comparison report
    os.makedirs("projects/02_House_Price_Prediction/outputs", exist_ok=True)
    report_path = "projects/02_House_Price_Prediction/outputs/regularization_report.txt"

    with open(report_path, "w") as f:
        for model, metrics in results.items():
            f.write(f"{model} Regression\n")
            for k, v in metrics.items():
                f.write(f"{k}: {v:.4f}\n")
            f.write("\n")

    print(f"\nRegularization report saved at: {report_path}")

if __name__ == "__main__":
    train_regularized_models(
        "projects/02_House_Price_Prediction/data/processed/house_prices_cleaned.csv"
    )
