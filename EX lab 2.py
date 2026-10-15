import numpy as np

roll_numbers = np.arange(1, 61)

time_points = np.linspace(0, 1, 50)

zeros_vec = np.zeros(8)

ones_vec = np.ones(8)

vectors = {
    "roll_numbers": roll_numbers,
    "time_points": time_points,
    "zeros_vec": zeros_vec,
    "ones_vec": ones_vec,
}

for name, v in vectors.items():
    print(f"{name}: length = {len(v)}, dtype = {v.dtype}")
