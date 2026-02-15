
## Project Overview

This project demonstrates end-to-end data analysis using Python.  
It includes data cleaning, feature engineering, aggregation, visualization, and exporting processed data.

The objective is to analyze sales data and extract meaningful business insights.

---

## Tech Stack

- Python  
- Pandas  
- Matplotlib  
- CSV Dataset  

---

## Project Structure

```
Task_15/
│── data_analysis.py
│── sales_data.csv
│── cleaned_sales_data.csv
│── README.md
```

---

## Key Features

✔ Data Cleaning  
✔ Feature Engineering  
✔ GroupBy Aggregations  
✔ Time-Based Analysis  
✔ Business Insights Generation  
✔ Data Visualization  
✔ Export Cleaned Dataset  

---

## Dataset Description

| Column | Description |
|--------|------------|
| OrderID | Unique order identifier |
| Date | Order date |
| Region | Sales region |
| Product | Product name |
| Category | Product category |
| Quantity | Units sold |
| Price | Unit price |

---

## Analysis Performed

### Exploratory Data Analysis (EDA)
- head()
- info()
- describe()

### Data Cleaning
- Handled missing values
- Converted Date column to datetime format

### Feature Engineering
- Created `Total_Sales = Quantity × Price`
- Extracted Month from Date

### Aggregation
- Monthly Sales Trend
- Region-wise Sales
- Category Contribution

### Visualization
- Line Chart → Monthly Sales Trend
- Bar Chart → Region-wise Sales
- Pie Chart → Category Distribution

---

## Business Insights

- Electronics category generates higher overall revenue.
- Sales vary significantly across regions.
- Monthly trends help identify peak sales periods.
- Data-driven insights support strategic decision-making.

---

## How to Run

### Step 1
Navigate to project folder:

```
cd Task_15
```

### Step 2
Run the script:

```
python data_analysis.py
```

---

## Skills Demonstrated

- Data Cleaning & Preprocessing  
- Feature Engineering  
- Aggregation & Grouping  
- Time Series Analysis  
- Data Visualization  
- Business Insight Interpretation  
- Debugging File Path Issues  

---


⭐ If you found this project useful, consider giving it a star on GitHub!
