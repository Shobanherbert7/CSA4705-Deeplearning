import matplotlib.pyplot as plt

prior = 0.02
sensitivity = 0.95
false_positive = 0.05

posterior = (
    sensitivity * prior
    / (sensitivity * prior
       + false_positive * (1 - prior))
)

print("Prior probability:", prior)
print("Posterior probability:", posterior)

plt.bar(
    ["Prior Probability", "After Positive Test"],
    [prior, posterior]
)
plt.ylabel("Probability")
plt.title("Disease Probability Before and After Test")
plt.ylim(0, 1)
plt.show()
