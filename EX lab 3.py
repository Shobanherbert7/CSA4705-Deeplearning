import numpy as np

# Sample step counts for 30 days (replace with your band's data)
rng = np.random.default_rng(42)
steps = rng.integers(3000, 15000, size=30)

first_week = steps[:7]        # days 1-7
last_5     = steps[-5:]       # days 26-30
alternate  = steps[::2]       # days 1, 3, 5, ..., 29
reversed_v = steps[::-1]      # day 30 down to day 1

print("Steps:", steps)
print("First week:", first_week)
print("Last 5 days:", last_5)
print("Alternate days:", alternate)
print("Reversed:", reversed_v)

# Check lengths
assert len(first_week) == 7
assert len(last_5) == 5
assert len(alternate) == 15
assert len(reversed_v) == 30
print("Length checks passed: 7, 5, 15, 30")
