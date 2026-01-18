# House Price Prediction using Machine Learning

## Project Overview

This project predicts house prices based on key features such as area, number of
bedrooms, bathrooms, and location. The goal is to demonstrate an end-to-end
machine learning pipeline.

## Workflow

1. Data preprocessing and feature encoding
2. Train-test split
3. Model training using Linear Regression
4. Model evaluation using MAE, RMSE, and R²
5. Feature importance analysis
6. Ridge and Lasso regularization
7. Final report generation with visualizations

## Models Used

- Linear Regression
- Ridge Regression (L2)
- Lasso Regression (L1)

## Key Results

- R² score ~ 0.96 indicating strong predictive performance
- Area and number of bedrooms are major price drivers
- Lasso helped in feature selection

## Folder Structure

- `data/` → raw and processed datasets
- `src/` → preprocessing, training, evaluation scripts
- `models/` → saved ML models
- `outputs/` → metrics and plots
- `docs/` → assumptions and model explanation

## Status

Completed
