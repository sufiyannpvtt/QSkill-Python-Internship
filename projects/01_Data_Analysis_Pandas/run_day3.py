from src.performance_segmentation import segment_students

if __name__ == "__main__":
    segment_students(
        "projects/01_Data_Analysis_Pandas/data/processed/student_performance_cleaned.csv",
        "projects/01_Data_Analysis_Pandas/outputs/tables/performance_segments.csv"
    )

    print("Day-3: Performance segmentation completed successfully.")
