import numpy as np
import matplotlib.pyplot as plt
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import learning_curve

np.random.seed(42)

X = np.linspace(-3, 3, 100).reshape(-1, 1)
y = X.ravel()**2 + np.random.normal(0, 2, 100)

models = {
    "Linear Regression": LinearRegression(),
    "Polynomial Degree 15": make_pipeline(
        PolynomialFeatures(15),
        LinearRegression()
    )
}

for name, model in models.items():
    sizes, train_scores, validation_scores = learning_curve(
        model,
        X,
        y,
        train_sizes=np.linspace(0.2, 1.0, 5),
        cv=5,
        scoring="neg_mean_squared_error",
        shuffle=True,
        random_state=42
    )

    train_error = -train_scores.mean(axis=1)
    validation_error = -validation_scores.mean(axis=1)

    plt.figure()
    plt.plot(sizes, train_error, "o-", label="Training Error")
    plt.plot(sizes, validation_error, "o-", label="Validation Error")
    plt.xlabel("Number of Training Samples")
    plt.ylabel("Mean Squared Error")
    plt.title(f"Learning Curve: {name}")
    plt.legend()
    plt.grid(True)
    plt.show()

    print(name)
    print("Training errors:", train_error)
    print("Validation errors:", validation_error)
