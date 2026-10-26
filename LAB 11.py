import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom

n = 20
p = 0.1

probability = binom.pmf(3, n, p)
print("P(exactly 3 defective):", probability)

x = np.arange(0, n + 1)
y = binom.pmf(x, n, p)

plt.bar(x, y)
plt.xlabel("Number of Defective Components")
plt.ylabel("Probability")
plt.title("Binomial Distribution")
plt.show()
