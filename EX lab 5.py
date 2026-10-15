import numpy as np

# Sample USD prices for 5 licences (replace with your own)
usd = np.array([49.99, 120.00, 299.50, 15.75, 89.00])

RATE = 83.5       # INR per USD
DISCOUNT = 0.10   # 10 %

# Convert USD to INR
inr = usd * RATE

# Apply 10 % discount
discounted = inr * (1 - DISCOUNT)

print("USD prices:        ", usd)
print("INR prices:        ", inr)
print("Discounted (INR):  ", discounted)

# Check: each discounted price == 0.9 x 83.5 x USD price
expected = 0.9 * 83.5 * usd
assert np.allclose(discounted, expected), "Mismatch in discounted prices!"
print("Check passed: discounted == 0.9 * 83.5 * USD for all 5 licences.")
