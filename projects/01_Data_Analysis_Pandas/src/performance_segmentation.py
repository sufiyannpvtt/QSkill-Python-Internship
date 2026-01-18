import pandas as pd

def segment_students(input_path, output_path):
    df = pd.read_csv(input_path)

    def classify_performance(marks):
        if marks >= 85:
            return "Excellent"
        elif marks >= 70:
            return "Good"
        elif marks >= 50:
            return "Average"
        else:
            return "Poor"

    df["Performance_Category"] = df["Final_Marks"].apply(classify_performance)

    df.to_csv(output_path, index=False)

    return df
