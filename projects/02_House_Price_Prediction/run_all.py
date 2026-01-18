import subprocess
import sys

def run_step(description, command):
    print(f"\n {description}")
    print(f"Running: {command}")

    result = subprocess.run(
        command, shell=True, text=True
    )

    if result.returncode != 0:
        print(f" Failed at step: {description}")
        sys.exit(1)
    else:
        print(f" Completed: {description}")

def main():
    steps = [
        (
            "Data Preprocessing",
            "python3 projects/02_House_Price_Prediction/src/preprocessing.py"
        ),
        (
            "Model Training (Linear Regression)",
            "python3 projects/02_House_Price_Prediction/src/train.py"
        ),
        (
            "Model Evaluation & Prediction Plot",
            "python3 projects/02_House_Price_Prediction/src/evaluate.py"
        ),
        (
            "Feature Importance Analysis",
            "python3 projects/02_House_Price_Prediction/src/feature_importance.py"
        ),
        (
            "Ridge & Lasso Regularization",
            "python3 projects/02_House_Price_Prediction/src/regularization.py"
        ),
        (
            "Final PDF Report Generation",
            "python3 projects/02_House_Price_Prediction/generate_final_report.py"
        )
    ]

    print("\n Starting FULL House Price Prediction Pipeline")

    for desc, cmd in steps:
        run_step(desc, cmd)

    print("\n ALL STEPS COMPLETED SUCCESSFULLY")
    print(" Final Report Ready: House_Price_Prediction_Report.pdf")

if __name__ == "__main__":
    main()
