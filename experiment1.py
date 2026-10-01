 import numpy as np
import pandas as pd

# NumPy Array
marks = np.array([78, 85, 92, 67, 88, 74])

print("NUMPY ARRAY")
print("Marks:", marks)
print("Mean:", np.mean(marks))
print("Maximum:", np.max(marks))
print("Minimum:", np.min(marks))
print("First three marks:", marks[:3])
print("Last three marks:", marks[-3:])

# Pandas DataFrame
students = {
    "Name": ["Aman", "Rahul", "Priya", "Sneha", "Arjun"],
    "Marks": [78, 85, 92, 67, 88],
    "Department": ["CSE", "CSE", "ISE", "CSE", "ISE"]
}

df = pd.DataFrame(students)

print("\nPANDAS DATAFRAME")
print(df)

print("\nFirst 3 rows:")
print(df.iloc[:3])

print("\nName column:")
print(df["Name"])

print("\nRows with Marks > 80:")
print(df[df["Marks"] > 80])

print("\nFirst 2 rows and first 2 columns:")
print(df.iloc[:2, :2])
