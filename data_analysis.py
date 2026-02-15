import pandas as pd
import matplotlib.pyplot as plt

# 1. Load Dataset
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, "sales_data.csv")

df = pd.read_csv(file_path)


# 2. Basic Exploration
print("First 5 rows:")
print(df.head())

print("\nDataset Info:")
print(df.info())

print("\nStatistical Summary:")
print(df.describe())

# 3. Handle Missing Values (if any)
df.fillna(0, inplace=True)

# 4. Create New Column: Total Sales
df["Total_Sales"] = df["Quantity"] * df["Price"]

# 5. Convert Date to Datetime
df["Date"] = pd.to_datetime(df["Date"])

# 6. Monthly Sales Analysis
df["Month"] = df["Date"].dt.month
monthly_sales = df.groupby("Month")["Total_Sales"].sum()

# 7. Region-wise Sales
region_sales = df.groupby("Region")["Total_Sales"].sum()

# 8. Category-wise Sales
category_sales = df.groupby("Category")["Total_Sales"].sum()

# 9. Visualization

# Monthly Sales Trend
plt.figure()
monthly_sales.plot(kind="line")
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.show()

# Region-wise Sales
plt.figure()
region_sales.plot(kind="bar")
plt.title("Region-wise Sales")
plt.xlabel("Region")
plt.ylabel("Total Sales")
plt.show()

# Category-wise Sales
plt.figure()
category_sales.plot(kind="pie", autopct='%1.1f%%')
plt.title("Category contribution")
plt.ylabel("")
plt.show()

# 10. Export Cleaned Data
df.to_csv("cleaned_sales_data.csv", index=False)

print("\nAnalysis Completed Successfully.")
