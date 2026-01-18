import matplotlib.pyplot as plt
import seaborn as sns

def create_visualizations(df):
    """
    Generates graphs and saves them as images
    """

    # Bar Chart
    plt.figure()
    plt.bar(df["Student"], df["Marks"])
    plt.xlabel("Student")
    plt.ylabel("Marks")
    plt.title("Marks Distribution")
    plt.savefig("projects/01_Data_Analysis_Pandas/outputs/charts/marks_bar_chart.png")
    plt.close()

    # Scatter Plot
    plt.figure()
    plt.scatter(df["Attendance"], df["Marks"])
    plt.xlabel("Attendance (%)")
    plt.ylabel("Marks")
    plt.title("Attendance vs Marks")
    plt.savefig("projects/01_Data_Analysis_Pandas/outputs/charts/attendance_scatter.png")
    plt.close()

    # Heatmap
    plt.figure()
    sns.heatmap(df.corr(), annot=True, cmap="coolwarm")
    plt.title("Correlation Heatmap")
    plt.savefig("projects/01_Data_Analysis_Pandas/outputs/charts/correlation_heatmap.png")
    plt.close()
