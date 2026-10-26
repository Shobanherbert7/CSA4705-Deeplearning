import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

mean = 70
std = 10

probability = norm.cdf(80, mean, std) - norm.cdf(60, mean, std)
print("P(60 <= X <= 80):", probability)

x = np.linspace(40, 100, 500)
y = norm.pdf(x, mean, std)

plt.plot(x, y, label="Normal Distribution")
plt.fill_between(
    x, y, where=(x >= 60) & (x <= 80),
    alpha=0.4, label="Scores 60 to 80"
)
plt.xlabel("Examination Marks")
plt.ylabel("Probability Density")
plt.title("Normal Distribution of Marks")
plt.legend()
plt.show()
