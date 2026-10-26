import numpy as np
import matplotlib.pyplot as plt

hours = np.array([2, 4, 6, 8, 10])
marks = np.array([35, 45, 60, 75, 85])

covariance = np.cov(hours, marks)[0, 1]
print("Sample covariance:", covariance)

plt.scatter(hours, marks)
plt.xlabel("Study Hours")
plt.ylabel("Examination Marks")
plt.title("Study Hours vs Marks")
plt.grid(True)
plt.show()
