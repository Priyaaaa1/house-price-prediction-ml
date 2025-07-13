# 🏠 House Price Prediction using Machine Learning

This project predicts house prices based on various features using multiple regression models. Implemented in Python with scikit-learn, CatBoost, and visualization libraries, it demonstrates a full ML workflow from preprocessing to model export.

---

## 📁 Dataset

- **File**: `HousePricePrediction.xlsx`
- Contains both numerical and categorical features related to residential house sales.

---

## 🔍 Project Workflow

1. **Data Loading** using `pandas`
2. **Exploratory Data Analysis (EDA)**:
   - `.head()`, `.shape()`, correlation matrix
   - Unique value distribution for categorical features
3. **Data Cleaning**:
   - Dropped unnecessary columns (`Id`)
   - Filled or removed missing values
4. **Feature Engineering**:
   - One-hot encoding for categorical columns using `OneHotEncoder`
5. **Train-Test Split**:
   - 80/20 split using `train_test_split`
6. **Model Training**:
   - Support Vector Regressor
   - Random Forest Regressor
   - Linear Regression
   - CatBoost Regressor
7. **Model Evaluation**:
   - Mean Absolute Percentage Error (MAPE)
   - Mean Absolute Error (MAE)
   - Root Mean Squared Error (RMSE)
   - R² Score
8. **Prediction Visualization**:
   - Actual vs Predicted plot
9. **Model Saving**:
   - All models saved using `joblib`

---

## 🧠 Models Trained

| Model                  | Status           |
|------------------------|------------------|
| Support Vector Regressor | ✅ Trained & Saved |
| Random Forest Regressor  | ✅ Trained & Saved |
| Linear Regression         | ✅ Trained & Saved |
| CatBoost Regressor        | ✅ Trained        |

---

## 📈 Evaluation Metrics (Sample Output)

```text
Mean Absolute Error (MAE): 24536.42
Root Mean Squared Error (RMSE): 38452.68
R² Score: 0.8872
Mean Absolute Percentage Error (MAPE): 0.1438
