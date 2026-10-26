import numpy as np

A = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

vector = A.flatten()
total = np.sum(A)

print("Flattened vector:", vector)
print("Total pixel intensity:", total)
