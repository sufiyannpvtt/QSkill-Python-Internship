import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def perform_eda(csv_path):
    # LOCK: output folders auto-create
    output_dir = "projects/01_Data_Analysis_Pandas/outputs/charts"
    os.makedirs(output_dir, exist_ok=True)

    df = pd.read_csv(csv_path)

    # Final Marks Distribution
    plt.figure()
    sns.histplot(df["Final_Marks"], bins=10, kde=True)
    plt.title("Distribution of Final Marks")
    plt.savefig(f"{output_dir}/marks_distribution.png")
    plt.close()

    #  Attendance Distribution
    plt.figure()
    sns.histplot(df["Attendance"], bins=10, kde=True)
    plt.title("Attendance Distribution")
    plt.savefig(f"{output_dir}/attendance_distribution.png")
    plt.close()

    #  Study Hours Distribution
    plt.figure()
    sns.histplot(df["Study_Hours"], bins=10, kde=True)
    plt.title("Study Hours Distribution")
    plt.savefig(f"{output_dir}/study_hours_distribution.png")
    plt.close()

    #  Marks by Gender
    plt.figure()
    sns.boxplot(x="Gender", y="Final_Marks", data=df)
    plt.title("Marks by Gender")
    plt.savefig(f"{output_dir}/marks_by_gender.png")
    plt.close()

    #  Attendance vs Marks
    plt.figure()
    sns.scatterplot(x="Attendance", y="Final_Marks", data=df)
    plt.title("Attendance vs Final Marks")
    plt.savefig(f"{output_dir}/attendance_vs_marks.png")
    plt.close()

    #  Study Hours vs Marks
    plt.figure()
    sns.scatterplot(x="Study_Hours", y="Final_Marks", data=df)
    plt.title("Study Hours vs Final Marks")
    plt.savefig(f"{output_dir}/study_hours_vs_marks.png")
    plt.close()

    # 7️⃣ Correlation Heatmap (NUMERIC ONLY)
    numeric_df = df.select_dtypes(include="number")

    plt.figure()
    sns.heatmap(numeric_df.corr(), annot=True, cmap="coolwarm")
    plt.title("Correlation Heatmap (Numeric Features)")
    plt.savefig(f"{output_dir}/correlation_heatmap.png")
    plt.close()

    print("EDA completed and all charts saved successfully.")
