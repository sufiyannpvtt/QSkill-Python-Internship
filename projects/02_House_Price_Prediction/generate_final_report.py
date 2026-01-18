from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Image, PageBreak
)
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch
import os

OUTPUT_PDF = "projects/02_House_Price_Prediction/House_Price_Prediction_Report.pdf"
OUTPUTS_DIR = "projects/02_House_Price_Prediction/outputs"

doc = SimpleDocTemplate(OUTPUT_PDF, pagesize=A4)
styles = getSampleStyleSheet()
story = []

# ---------------- TITLE ----------------
story.append(Paragraph("<b>House Price Prediction using Machine Learning</b>", styles["Title"]))
story.append(Spacer(1, 0.3 * inch))

story.append(Paragraph("<b>Internship:</b> Python Development Internship (QSkill)", styles["Normal"]))
story.append(Paragraph("<b>Project:</b> House Price Prediction (Regression Models)", styles["Normal"]))
story.append(Spacer(1, 0.3 * inch))

# ---------------- OBJECTIVE ----------------
story.append(Paragraph("<b>1. Objective</b>", styles["Heading2"]))
story.append(Paragraph(
    "The objective of this project is to predict house prices based on multiple features "
    "such as area, number of bedrooms, bathrooms, and location using machine learning "
    "regression techniques.",
    styles["Normal"]
))

# ---------------- DATASET ----------------
story.append(Spacer(1, 0.2 * inch))
story.append(Paragraph("<b>2. Dataset Description</b>", styles["Heading2"]))
story.append(Paragraph(
    "The dataset contains housing attributes including area in square feet, number of bedrooms, "
    "bathrooms, location category, and the target variable price. "
    "Categorical variables were encoded and numerical features were prepared for modeling.",
    styles["Normal"]
))

# ---------------- MODELS ----------------
story.append(PageBreak())
story.append(Paragraph("<b>3. Models Used</b>", styles["Heading2"]))
story.append(Paragraph(
    "- Linear Regression (baseline model)<br/>"
    "- Ridge Regression (L2 regularization)<br/>"
    "- Lasso Regression (L1 regularization & feature selection)",
    styles["Normal"]
))

# ---------------- METRICS ----------------
story.append(Spacer(1, 0.2 * inch))
story.append(Paragraph("<b>4. Model Evaluation Metrics</b>", styles["Heading2"]))

metrics_path = os.path.join(OUTPUTS_DIR, "accuracy_report.txt")
if os.path.exists(metrics_path):
    with open(metrics_path) as f:
        metrics_text = "<br/>".join(f.readlines())
    story.append(Paragraph(metrics_text, styles["Normal"]))

# ---------------- PREDICTION PLOT ----------------
story.append(PageBreak())
story.append(Paragraph("<b>5. Prediction Results</b>", styles["Heading2"]))
story.append(Spacer(1, 0.2 * inch))

pred_plot = os.path.join(OUTPUTS_DIR, "prediction_plot.png")
if os.path.exists(pred_plot):
    story.append(Paragraph("Actual vs Predicted House Prices", styles["Heading3"]))
    story.append(Spacer(1, 0.1 * inch))
    story.append(Image(pred_plot, width=5.5 * inch, height=4 * inch))

# ---------------- FEATURE IMPORTANCE ----------------
story.append(PageBreak())
story.append(Paragraph("<b>6. Feature Importance Analysis</b>", styles["Heading2"]))
story.append(Spacer(1, 0.2 * inch))

feat_plot = os.path.join(OUTPUTS_DIR, "feature_importance.png")
if os.path.exists(feat_plot):
    story.append(Paragraph("Linear Regression Coefficient Analysis", styles["Heading3"]))
    story.append(Spacer(1, 0.1 * inch))
    story.append(Image(feat_plot, width=5.5 * inch, height=4 * inch))

# ---------------- REGULARIZATION ----------------
story.append(PageBreak())
story.append(Paragraph("<b>7. Ridge & Lasso Regularization</b>", styles["Heading2"]))

reg_path = os.path.join(OUTPUTS_DIR, "regularization_report.txt")
if os.path.exists(reg_path):
    with open(reg_path) as f:
        reg_text = "<br/>".join(f.readlines())
    story.append(Paragraph(reg_text, styles["Normal"]))

# ---------------- CONCLUSION ----------------
story.append(PageBreak())
story.append(Paragraph("<b>8. Conclusion</b>", styles["Heading2"]))
story.append(Paragraph(
    "The project demonstrates a complete machine learning pipeline from data preprocessing "
    "to model training, evaluation, and explainability. Linear Regression provided a strong "
    "baseline, while Ridge and Lasso improved generalization and interpretability.",
    styles["Normal"]
))

story.append(Spacer(1, 0.3 * inch))
story.append(Paragraph("<i>— End of Report —</i>", styles["Normal"]))

doc.build(story)

print("Final Project-2 PDF report generated successfully.")
