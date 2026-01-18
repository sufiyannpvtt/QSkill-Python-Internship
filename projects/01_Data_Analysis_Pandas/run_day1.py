from src.preprocessing import preprocess_data

if __name__ == "__main__":
    preprocess_data(
        "projects/01_Data_Analysis_Pandas/data/raw/student_performance_raw.csv",
        "projects/01_Data_Analysis_Pandas/data/processed/student_performance_cleaned.csv"
    )

    print("Day-1 preprocessing completed successfully.")
