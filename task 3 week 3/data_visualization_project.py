# ==========================================================
# DATA VISUALIZATION PROJECT
# Using Matplotlib and Seaborn
# Dataset: Tips Dataset (Built-in Seaborn Dataset)
# ==========================================================

# ----------------------------
# 1. Import Required Libraries
# ----------------------------

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set visual style for better presentation
sns.set(style="whitegrid")

# ----------------------------
# 2. Load Dataset
# ----------------------------

# Load built-in dataset from seaborn
data = sns.load_dataset("tips")

# Display first 5 rows
print("First 5 rows of dataset:")
print(data.head())

# ----------------------------
# 3. Basic Data Exploration
# ----------------------------

print("\nDataset Information:")
print(data.info())

print("\nStatistical Summary:")
print(data.describe())

# Check for missing values
print("\nMissing Values:")
print(data.isnull().sum())

# ==========================================================
# VISUALIZATION SECTION
# ==========================================================

# ----------------------------
# 4. Line Plot
# ----------------------------
# We calculate average total bill per table size
# This helps us understand spending trend as group size increases

avg_bill = data.groupby("size")["total_bill"].mean()

plt.figure()
plt.plot(avg_bill.index, avg_bill.values)
plt.title("Average Total Bill by Table Size")
plt.xlabel("Table Size")
plt.ylabel("Average Total Bill")
plt.show()


# ----------------------------
# 5. Scatter Plot
# ----------------------------
# Shows relationship between total bill and tip
# Helps identify correlation (Do higher bills lead to higher tips?)

plt.figure()
plt.scatter(data["total_bill"], data["tip"])
plt.title("Scatter Plot: Total Bill vs Tip")
plt.xlabel("Total Bill")
plt.ylabel("Tip")
plt.show()


# ----------------------------
# 6. Histogram
# ----------------------------
# Displays distribution of total bills
# KDE (Kernel Density Estimate) shows smooth distribution curve

plt.figure()
sns.histplot(data["total_bill"], kde=True)
plt.title("Distribution of Total Bill")
plt.xlabel("Total Bill")
plt.ylabel("Frequency")
plt.show()


# ----------------------------
# 7. Box Plot
# ----------------------------
# Box plot shows:
# - Median
# - Quartiles
# - Outliers
# Helps understand spread and extreme values

plt.figure()
sns.boxplot(x=data["total_bill"])
plt.title("Box Plot of Total Bill")
plt.xlabel("Total Bill")
plt.show()


# ==========================================================
# 8. Conclusion (Printed Output)
# ==========================================================

print("\nAnalysis Insights:")
print("1. Larger table sizes tend to have higher average total bills.")
print("2. There is a positive relationship between total bill and tip.")
print("3. The histogram shows that most bills are concentrated in mid-range values.")
print("4. The box plot reveals the spread of the data and possible outliers.")

# End of Project
