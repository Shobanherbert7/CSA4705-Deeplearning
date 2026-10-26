import numpy as np
import matplotlib.pyplot as plt
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

np.random.seed(42)

X = np.linspace(-3, 3, 50).reshape(-1, 1)
y = X.ravel()**2 + np.random.normal(0, 2, 50)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

X_plot = np.linspace(-3, 3, 300).reshape(-1, 1)

plt.scatter(X_train, y_train, label="Training Data")
plt.scatter(X_test, y_test, label="Testing Data")

for degree in [2, 15]:
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

plt.xlabel("Feature")
plt.ylabel("Target")
plt.title("Underfitting vs Overfitting")
plt.ylim(-10, 15)
plt.legend()
plt.show()
