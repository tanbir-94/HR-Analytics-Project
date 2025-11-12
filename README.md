HR Analytics Project — End-to-End Data Analysis Project

📊 Project Overview

The purpose of this project is to analyze employee attrition (employee turnover) and identify key factors that contribute to it.
Using Excel, SQL, Python, and Power BI, I built a complete data analytics workflow — from raw data cleaning to final business insights visualization.

This project helps HR departments understand:

Which departments have the highest attrition

How factors like age, income, overtime, and job role affect attrition

Key demographic and professional trends behind employee turnover



---

🗂 Project Workflow

Step	Tool Used	Description

Data Cleaning	Excel	Removed nulls, duplicates, and spelling errors; standardized categorical data
Database Setup	PostgreSQL (pgAdmin)	Created HR_Attrition table and imported cleaned CSV
SQL Analysis	SQL Queries	Performed detailed attrition analysis by department, overtime, job role, and income band
EDA (Exploratory Data Analysis)**	Python (Pandas, Seaborn, Matplotlib)	Explored dataset, created visual insights like attrition by department, income, overtime
Visualization Dashboard	Power BI	Built interactive HR Analytics Dashboard to summarize insights visually



---

🧹 Step 1: Data Cleaning (Excel)

Performed the following operations on the raw dataset:

Removed duplicate records

Handled null values in key columns

Corrected spelling mistakes and inconsistent categorical data

Verified data types (numeric/text)

Saved final dataset as HR_Attrition_Cleaned.csv



---

🧱 Step 2: Database Creation (SQL in pgAdmin)


---

🧮 Step 3: SQL Analysis


---

🐍 Step 4: Python EDA (Exploratory Data Analysis)

Libraries Used:

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

Key Insights Generated:

Attrition by Department (Bar Chart)

Age Distribution by Attrition (Histogram)

Monthly Income vs Attrition (Box Plot)

OverTime vs Attrition (Count Plot)

Job Role vs Attrition (Horizontal Bar Chart)

Correlation Heatmap for Numeric Features


Correlation Heatmap:

important_cols = [
    'Age','MonthlyIncome','DistanceFromHome',
    'JobLevel','TotalWorkingYears',
    'YearsAtCompany','YearsSinceLastPromotion','YearsWithCurrManager'
]
sns.heatmap(df[important_cols].corr(), annot=True, cmap='coolwarm')


---

📈 Step 5: Power BI Dashboard

Dashboard Title: HR Analytics Dashboard

KPIs Displayed:

Total Employees: 1470

Total Attrition: 237

Attrition Rate: 16.1%

Average Age: 37

Average Salary: 6.5K

Avg Years at Company: 7.01


Visuals Included:

Attrition by Department

Attrition by Age Group

Attrition by Job Role

Attrition by Education Field

Attrition by Gender

Attrition by Years at Company

OverTime Impact Visualization

Interactive Slicers: Department, Marital Status, Job Role


Key Insights:

🔹 Research & Development has the highest attrition (133 employees).

🔹 Majority of employees leaving are aged 25–34 years.

🔹 Males (150) leave more often than females (87).

🔹 Overtime workers show higher attrition rates.

🔹 Most attrition occurs within the first 1–3 years of joining.



---

💡 Final Insights Summary

High attrition in R&D and Sales departments.

Younger employees (25–34) are more likely to leave.

Overtime strongly correlates with employee turnover.

Lower income bands have higher attrition.

Early-career employees tend to switch jobs more frequently.



---

📁 Project Files Structure

HR_Analytics_Project/
│
├── HR_Attrition_Cleaned.csv              # Cleaned data             
├── hr_attrition_attrition.sql            # SQL table creation script  # All SQL queries
├── hr_attrition_eda.py                   # Python EDA script
├── HR_Analytics_Dashboard.png           ![Dashboard](HR_Analytics_Dashboard.png) 
└── README.md                             # Project documentation (this file)


---

🧰 Tools & Technologies

Excel – Data Cleaning

PostgreSQL / pgAdmin – SQL Analysis

Python (Pandas, Seaborn, Matplotlib) – Exploratory Data Analysis

Power BI – Dashboard Visualization



---

🏁 Conclusion

This HR Analytics Project showcases a complete data analytics pipeline from raw data to actionable insights.
It demonstrates practical use of Excel, SQL, Python, and Power BI in understanding workforce dynamics and reducing attrition.


---

🌐 Connect with Me

📧 Email: mdtanbirraza7@gmail.com
💼 LinkedIn: https://www.linkedin.com/in/md-tanbir-rja-067561236
📊 GitHub:   https://github.com/tanbir-94

