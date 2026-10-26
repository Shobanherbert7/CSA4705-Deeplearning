import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

np.random.seed(42)

X = np.linspace(1, 10, 100).reshape(-1, 1)
y = 5 * X.ravel()**2 + np.random.normal(0, 15, 100)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)

train_pred = model.predict(X_train)
test_pred = model.predict(X_test)

print("Training MSE:",
      mean_squared_error(y_train, train_pred))
print("Testing MSE:",
      mean_squared_error(y_test, test_pred))

plt.scatter(X_test, y_test, label="Actual Marks")
plt.scatter(X_test, test_pred, label="Predicted Marks")
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.title("Linear Regression on Nonlinear Data")
plt.legend()
plt.show()
