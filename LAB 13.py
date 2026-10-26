import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson

lam = 4

probability = poisson.pmf(6, lam)
print("P(exactly 6 customers):", probability)

x = np.arange(0, 13)
y = poisson.pmf(x, lam)

plt.bar(x, y)
plt.xlabel("Number of Customers")
plt.ylabel("Probability")
plt.title("Poisson Distribution")
plt.show()
