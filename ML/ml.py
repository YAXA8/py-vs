import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# 1. Create simple sample data: y = 2.5 * x + 10 + noise
np.random.seed(42)
X = 2 * np.random.rand(100, 1)  # 100 random values between 0 and 2
y = 2.5 * X.squeeze() + 10 + np.random.randn(100) * 0.5  # Linear relation + Gaussian noise

# 2. Split into train and test sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)   

# 3. Initialize and fit the Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# 4. Make predictions on the test set
y_pred = model.predict(X_test)

# 5. Evaluate the model
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

print("--- Model Parameters ---")
print(f"Slope (Weight / β₁):     {model.coef_[0]:.4f}")
print(f"Intercept (Bias / β₀):   {model.intercept_:.4f}\n")

print("--- Evaluation Metrics ---")
print(f"Mean Squared Error (MSE):       {mse:.4f}")
print(f"Root Mean Squared Error (RMSE): {rmse:.4f}")
print(f"R-squared (R²):                 {r2:.4f}")

# 6. Visualize the results
plt.figure(figsize=(8, 5))
plt.scatter(X_test, y_test, color="blue", label="Actual Test Data")
plt.plot(
    X_test,
    y_pred,
    color="red",
    linewidth=2,
    label="Fitted Regression Line"
)
plt.xlabel("X")
plt.ylabel("y")
plt.title("Simple Linear Regression (scikit-learn)")
plt.legend()
plt.grid(True, linestyle="--", alpha=0.6)
plt.show()