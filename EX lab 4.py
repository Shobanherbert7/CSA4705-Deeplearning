import numpy as np

# Sample sales for 7 products (replace with your store's data)
week1 = np.array([120, 85, 200, 60, 150, 95, 40])
week2 = np.array([135, 70, 210, 45, 160, 80, 55])

# Total sales for the two weeks (element-wise, per product)
total = week1 + week2

# Change from week 1 to week 2 (positive = increase, negative = fall)
change = week2 - week1

print("Week 1:", week1)
print("Week 2:", week2)
print("Total per product:", total)
print("Change (week2 - week1):", change)
print("Overall total:", total.sum())

# Products whose sales fell
fell_mask = change < 0
fell_idx = np.where(fell_mask)[0]
print("Products that fell (0-based index):", fell_idx)
print("Products that fell (product number):", fell_idx + 1)
print("Drop amounts:", change[fell_mask])
