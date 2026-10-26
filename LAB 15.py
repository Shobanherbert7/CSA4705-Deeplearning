import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import entropy

Y = np.array([0, 1, 0, 0])
P = np.array([0.1, 0.6, 0.2, 0.1])

cross_entropy = -np.sum(Y * np.log(P))
kl_divergence = entropy(Y, P)

print("Cross-entropy loss:", cross_entropy)
print("KL divergence:", kl_divergence)

x = np.arange(4)
width = 0.35

plt.bar(x - width/2, Y, width, label="Actual")
plt.bar(x + width/2, P, width, label="Predicted")
plt.xticks(x, ["Class 1", "Class 2", "Class 3", "Class 4"])
plt.ylabel("Probability")
plt.title("Actual vs Predicted Distribution")
plt.legend()
plt.show()
