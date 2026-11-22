"""
Experiment 9(b): Implement Matplotlib and Pandas libraries.

Aim:
To create a dataset using Pandas and visualize it using Matplotlib.
"""

import pandas as pd
import matplotlib.pyplot as plt

# Create a dataset using Pandas
data = {
    "Subject": ["Python", "DBMS", "OS", "EVS"],
    "Marks": [85, 90, 75, 80],
}

df = pd.DataFrame(data)

print("Student Marks:")
print(df)

# Create a bar graph
plt.bar(df["Subject"], df["Marks"], color="skyblue")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.title("Student Marks Analysis")
plt.show()
