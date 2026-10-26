import numpy as np
import matplotlib.pyplot as plt

temperature = np.array([22, 25, 28, 30, 32])
humidity = np.array([80, 75, 68, 60, 55])

data = np.column_stack((temperature, humidity))
cov_matrix = np.cov(data, rowvar=False)

print("Covariance matrix:")
print(cov_matrix)

plt.scatter(temperature, humidity)
plt.xlabel("Temperature (°C)")
plt.ylabel("Humidity (%)")
plt.title("Temperature vs Humidity")
plt.grid(True)
plt.show()
