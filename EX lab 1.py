import numpy as np

# Store the marks in a NumPy vector
marks = np.array([72, 85, 91, 64, 88, 91, 55, 79])

# Summary statistics
print("Mean:", marks.mean())
print("Min:", marks.min())
print("Max:", marks.max())
print("Std dev:", marks.std())        # population SD (ddof=0)
# print("Sample SD:", marks.std(ddof=1))  # use this if the data is a sample

# Topper's position using argmax
topper_idx = np.argmax(marks)
print("Topper index (np.argmax):", topper_idx, "-> marks:", marks[topper_idx])

# Manual scan to verify
best_idx = 0
for i in range(1, len(marks)):
    if marks[i] > marks[best_idx]:    # strict '>' keeps the first max on ties
        best_idx = i
print("Topper index (manual scan):", best_idx)

# Check that they match
assert topper_idx == best_idx, "Mismatch between argmax and manual scan!"
print("Check passed: both methods agree.")
