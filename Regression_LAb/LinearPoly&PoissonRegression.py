import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, PolynomialFeatures
from sklearn.linear_model import LinearRegression, PoissonRegressor
from sklearn.metrics import mean_squared_error, mean_absolute_error

# Load Data
data = pd.read_csv("Data.csv")
eval_data = pd.read_csv("Eval.csv")

# Exploratory Data Analysis (EDA)
print(data.info())
print(data.describe())
print(data.isnull().sum())

sns.pairplot(data)
plt.show()

# Data Preprocessing
X = data.drop(columns=["TARGET_Capacity", "TARGET_CaseCount"])
y_capacity = data["TARGET_Capacity"]
y_casecount = data["TARGET_CaseCount"]

# Train-Test Split
X_train, X_test, y_train_cap, y_test_cap = train_test_split(X, y_capacity, test_size=0.2, random_state=42)
X_train_case, X_test_case, y_train_case, y_test_case = train_test_split(X, y_casecount, test_size=0.2, random_state=42)

# Feature Scaling
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Model 1: Linear Regression for Capacity
lin_reg = LinearRegression()
lin_reg.fit(X_train_scaled, y_train_cap)
cap_pred = lin_reg.predict(X_test_scaled)
print("Linear Regression RMSE:", np.sqrt(mean_squared_error(y_test_cap, cap_pred)))

# Model 2: Polynomial Regression
poly = PolynomialFeatures(degree=2)
X_train_poly = poly.fit_transform(X_train_scaled)
X_test_poly = poly.transform(X_test_scaled)

poly_reg = LinearRegression()
poly_reg.fit(X_train_poly, y_train_cap)
cap_pred_poly = poly_reg.predict(X_test_poly)
print("Polynomial Regression RMSE:", np.sqrt(mean_squared_error(y_test_cap, cap_pred_poly)))

# Model 3: Poisson Regression for CaseCount
poisson_reg = PoissonRegressor()
poisson_reg.fit(X_train_scaled, y_train_case)
case_pred = poisson_reg.predict(X_test_scaled)
print("Poisson Regression MAE:", mean_absolute_error(y_test_case, case_pred))

# Final Predictions
eval_X_scaled = scaler.transform(eval_data)
eval_cap_pred = lin_reg.predict(eval_X_scaled)
eval_case_pred = poisson_reg.predict(eval_X_scaled)

# Save Predictions
submission = pd.DataFrame({"Id": eval_data.index, "TARGET_Capacity": eval_cap_pred, "TARGET_CaseCount": eval_case_pred})
submission.to_csv("sample_solution.csv", index=False)

print("Predictions saved in sample_solution.csv")
