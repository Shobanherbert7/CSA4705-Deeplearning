import numpy as np
import matplotlib.pyplot as plt

C = np.array([
    [5, 2],
    [2, 2]
])

values, vectors = np.linalg.eigh(C)

index = np.argmax(values)
principal_vector = vectors[:, index]

print("Eigenvalues:", values)
print("Eigenvectors:")
print(vectors)
print("Largest eigenvalue:", values[index])
print("Principal eigenvector:", principal_vector)

for i in range(2):
    plt.quiver(
        0, 0,
        vectors[0, i], vectors[1, i],
        angles="xy", scale_units="xy", scale=1,
        label=f"Eigenvalue {values[i]:.2f}"
    )

plt.xlim(-1.2, 1.2)
plt.ylim(-1.2, 1.2)
plt.axhline(0, color="black")
plt.axvline(0, color="black")
plt.grid(True)
plt.legend()
plt.title("Principal Direction of Sensor Data")
plt.xlabel("Sensor 1")
plt.ylabel("Sensor 2")
plt.show()
