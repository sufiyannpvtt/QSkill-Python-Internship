import pandas as pd
import joblib
import matplotlib.pyplot as plt
import os

def analyze_feature_importance(data_path, model_path):
    df = pd.read_csv(data_path)

    X = df.drop("Price", axis=1)

    model = joblib.load(model_path)

    coefficients = model.coef_

    feature_importance = pd.DataFrame({
        "Feature": X.columns,
        "Coefficient": coefficients
    }).sort_values(by="Coefficient", ascending=False)

    # Print table
    print("\nFeature Importance (Coefficients):")
    print(feature_importance)

    # ensure output folder
    os.makedirs("projects/02_House_Price_Prediction/outputs", exist_ok=True)

    # Plot
    plt.figure(figsize=(8, 5))
    plt.barh(
        feature_importance["Feature"],
        feature_importance["Coefficient"]
    )
    plt.xlabel("Coefficient Value")
    plt.title("Feature Importance - Linear Regression")
    plt.gca().invert_yaxis()

    plt.savefig(
        "projects/02_House_Price_Prediction/outputs/feature_importance.png"
    )
    plt.close()

    print("\nFeature importance plot saved successfully.")

if __name__ == "__main__":
    analyze_feature_importance(
        "projects/02_House_Price_Prediction/data/processed/house_prices_cleaned.csv",
        "projects/02_House_Price_Prediction/models/linear_regression.pkl"
    )
