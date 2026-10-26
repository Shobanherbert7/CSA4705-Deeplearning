import numpy as np
import matplotlib.pyplot as plt
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

np.random.seed(42)

X = np.linspace(0, 24, 80).reshape(-1, 1)
y = 25 + 8 * np.sin(2 * np.pi * X.ravel() / 24)
y += np.random.normal(0, 1.5, 80)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)

X_plot = np.linspace(0, 24, 300).reshape(-1, 1)

plt.scatter(X_train, y_train, label="Training Data")

for degree in [1, 3, 12]:
    model = make_pipeline(
        PolynomialFeatures(degree),
        LinearRegression()
    )
    model.fit(X_train, y_train)

    train_pred = model.predict(X_train)
    test_pred = model.predict(X_test)

    print(f"\nDegree {degree}")
    print("Training MSE:",
          mean_squared_error(y_train, train_pred))
    print("Testing MSE:",
          mean_squared_error(y_test, test_pred))

    plt.plot(
        X_plot, model.predict(X_plot),
        label=f"Degree {degree}"
    )

plt.xlabel("Time (hours)")
plt.ylabel("Temperature (°C)")
plt.title("Temperature Prediction Models")
plt.legend()
plt.show()
