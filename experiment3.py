"""
Experiment 3: Data Visualization using Matplotlib and Seaborn
Topics: Histogram, box plot, scatter plot, pair plot and correlation heatmap.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data
df = pd.read_csv("student_performance.csv")

# Fill the missing Marks value only for visualization
df["Marks"] = df["Marks"].fillna(df["Marks"].mean())

# 1. Histogram
plt.figure(figsize=(7, 4))
plt.hist(df["Marks"], bins=5, edgecolor="black")
plt.title("Distribution of Student Marks")
plt.xlabel("Marks")
plt.ylabel("Number of Students")
plt.show()

# 2. Box Plot
plt.figure(figsize=(7, 4))
sns.boxplot(y=df["Marks"])
plt.title("Box Plot of Student Marks")
plt.show()

# 3. Scatter Plot
plt.figure(figsize=(7, 4))
sns.scatterplot(data=df, x="StudyHours", y="Marks")
plt.title("Study Hours vs Marks")
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.show()

# 4. Pair Plot
sns.pairplot(df[["Marks", "Attendance", "StudyHours"]])
plt.show()

# 5. Correlation Heatmap
plt.figure(figsize=(7, 5))
corr = df[["Marks", "Attendance", "StudyHours"]].corr()
sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Heatmap")
plt.show()
