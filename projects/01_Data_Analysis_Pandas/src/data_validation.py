import pandas as pd

def validate_data(df):
    issues = []

    if df.isnull().sum().any():
        issues.append("Missing values detected")

    if (df["Attendance"] < 0).any() or (df["Attendance"] > 100).any():
        issues.append("Invalid attendance values")

    if (df["Study_Hours"] < 0).any():
        issues.append("Invalid study hours")

    return issues
