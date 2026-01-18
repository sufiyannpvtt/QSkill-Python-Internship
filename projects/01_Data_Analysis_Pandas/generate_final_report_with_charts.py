from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Image, PageBreak
)
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch
import os

# Output PDF
OUTPUT_PDF = "projects/01_Data_Analysis_Pandas/Student_Performance_Analysis_Report.pdf"

# Charts directory
CHARTS_DIR = "projects/01_Data_Analysis_Pandas/outputs/charts"

doc = SimpleDocTemplate(OUTPUT_PDF, pagesize=A4)
styles = getSampleStyleSheet()
story = []

# ------------------ TITLE ------------------
story.append(Paragraph("<b>Student Performance Data Analysis Report</b>", styles["Title"]))
story.append(Spacer(1, 0.3 * inch))

story.append(Paragraph("<b>Internship:</b> Python Development Internship (QSkill)", styles["Normal"]))
story.append(Paragraph("<b>Intern:</b> Mohammad Shadullah", styles["Normal"]))
story.append(Paragraph("<b>Project:</b> Data Analysis using Pandas & Matplotlib", styles["Normal"]))
story.append(Spacer(1, 0.3 * inch))

# ------------------ OBJECTIVE ------------------
story.append(Paragraph("<b>1. Objective</b>", styles["Heading2"]))
story.append(Paragraph(
    "The objective of this project is to analyze student academic performance data, "
    "identify key influencing factors, and derive actionable insights using Python.",
    styles["Normal"]
))
story.append(Spacer(1, 0.2 * inch))

# ------------------ EDA SECTION ------------------
story.append(PageBreak())
story.append(Paragraph("<b>2. Exploratory Data Analysis (EDA)</b>", styles["Heading2"]))
story.append(Spacer(1, 0.2 * inch))

charts = [
    ("Marks Distribution", "marks_distribution.png"),
    ("Attendance Distribution", "attendance_distribution.png"),
    ("Study Hours Distribution", "study_hours_distribution.png"),
    ("Marks by Gender", "marks_by_gender.png"),
    ("Attendance vs Marks", "attendance_vs_marks.png"),
    ("Study Hours vs Marks", "study_hours_vs_marks.png"),
    ("Correlation Heatmap", "correlation_heatmap.png"),
]

for title, file_name in charts:
    img_path = os.path.join(CHARTS_DIR, file_name)

    if os.path.exists(img_path):
        story.append(Paragraph(f"<b>{title}</b>", styles["Heading3"]))
        story.append(Spacer(1, 0.1 * inch))
        story.append(Image(img_path, width=5.5 * inch, height=3.5 * inch))
        story.append(Spacer(1, 0.3 * inch))

# ------------------ INSIGHTS ------------------
story.append(PageBreak())
story.append(Paragraph("<b>3. Key Insights</b>", styles["Heading2"]))
story.append(Paragraph(
    "- Higher attendance strongly correlates with better academic performance.<br/>"
    "- Study hours improve marks up to a threshold, after which returns diminish.<br/>"
    "- Female students show slightly higher median scores.<br/>"
    "- Attendance and study hours are key predictors of final marks.",
    styles["Normal"]
))

story.append(Spacer(1, 0.3 * inch))
story.append(Paragraph("<i>— End of Report —</i>", styles["Normal"]))

doc.build(story)

print(" Final PDF with charts generated successfully.")
