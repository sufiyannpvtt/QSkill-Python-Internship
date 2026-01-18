import joblib
import pandas as pd

def predict_price(input_data):
    model = joblib.load(
        "projects/02_House_Price_Prediction/models/linear_regression.pkl"
    )

    df = pd.DataFrame([input_data])
    prediction = model.predict(df)

    return prediction[0]


if __name__ == "__main__":
    sample_house = {
        "Area_sqft": 1400,
        "Bedrooms": 3,
        "Bathrooms": 2,
        "Location_Suburb": 0
    }

    price = predict_price(sample_house)
    print("Predicted House Price:", round(price, 2))
