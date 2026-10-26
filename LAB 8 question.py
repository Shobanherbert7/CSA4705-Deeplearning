import numpy as np
import matplotlib.pyplot as plt

A = np.array([
    [4, 2],
    [2, 4]
])

eigenvalues = np.linalg.eigvals(A)
print("Eigenvalues:", eigenvalues)

plt.bar(["Eigenvalue 1", "Eigenvalue 2"], eigenvalues)
plt.ylabel("Value")
plt.title("Eigenvalues of Matrix A")
plt.show()
