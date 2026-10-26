import numpy as np
import matplotlib.pyplot as plt

C = np.array([
    [3, 1],
    [1, 3]
])

values, vectors = np.linalg.eigh(C)

print("Eigenvalues:", values)
print("Eigenvectors:")
print(vectors)

for i in range(2):
    plt.quiver(
        0, 0,
        vectors[0, i], vectors[1, i],
        angles="xy", scale_units="xy", scale=1
    )

plt.xlim(-1.2, 1.2)
plt.ylim(-1.2, 1.2)
plt.axhline(0, color="black")
plt.axvline(0, color="black")
plt.grid(True)
plt.title("Eigenvectors of Covariance Matrix")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()
