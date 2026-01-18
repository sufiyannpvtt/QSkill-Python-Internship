def calculate_statistics(df):
    """
    Calculates basic statistical values
    """
    stats = {}

    stats["average_marks"] = df["Marks"].mean()
    stats["highest_marks"] = df["Marks"].max()
    stats["lowest_marks"] = df["Marks"].min()
    stats["attendance_marks_correlation"] = df["Marks"].corr(df["Attendance"])

    return stats
