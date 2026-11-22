"""
Experiment 9(a): Implement NumPy and Pandas packages.

Aim:
To perform basic numerical operations using NumPy and data
manipulation using Pandas.
"""

import numpy as np
import pandas as pd

# NumPy operations
arr = np.array([10, 20, 30, 40, 50])

print("NumPy Array:", arr)
print("Sum:", np.sum(arr))
print("Mean:", np.mean(arr))
print("Maximum:", np.max(arr))
print("Minimum:", np.min(arr))

# Pandas operations
data = {
    "Name": ["John", "Alice", "Bob"],
    "Age": [20, 21, 19],
    "Marks": [85, 90, 78],
}

df = pd.DataFrame(data)

print("\nPandas DataFrame:")
print(df)

print("\nAverage Marks:", df["Marks"].mean())
print("\nStudent Names:")
print(df["Name"])
