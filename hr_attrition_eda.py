# Import Libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv("HR_Attrition_Cleaned.csv")

#  Quick Overview
print(" Dataset Loaded Successfully!\n")
print(df.head())
print("\nDataset Info:\n")
print(df.info())
print("\nSummary Stats:\n")
print(df.describe())

# Basic Metrics
total_emp = df.shape[0]
attrition_counts = df['Attrition'].value_counts()
attrition_percent = round(df['Attrition'].value_counts(normalize=True) * 100, 2)

print("\n Total Employees:", total_emp)
print("Attrition Counts:\n", attrition_counts)
print("Attrition Percentage:\n", attrition_percent)



#  Visualization (EDA)
plt.style.use("seaborn-v0_8-darkgrid")


#  Attrition by Department
plt.figure(figsize=(9,5))
dept_chart = sns.countplot(data=df, x='Department', hue='Attrition')
plt.title("Attrition by Department")
plt.xlabel("Department")
plt.ylabel("Employee Count")

# Add data labels
for p in dept_chart.patches:
    height = p.get_height()
    if height > 0:
        dept_chart.annotate(f'{height}', 
                            (p.get_x() + p.get_width()/2., height),
                            ha='center', va='bottom', fontsize=10, color='black')
plt.show()


#  Age Distribution by Attrition
plt.figure(figsize=(9,5))
sns.histplot(data=df, x='Age', hue='Attrition', kde=True, bins=20)
plt.title("Age Distribution by Attrition")
plt.xlabel("Age")
plt.ylabel("Count")
plt.show()


#  Monthly Income vs Attrition
plt.figure(figsize=(9,5))
sns.boxplot(data=df, x='Attrition', y='MonthlyIncome')
plt.title("Monthly Income by Attrition")
plt.show()


#  OverTime vs Attrition
plt.figure(figsize=(6,4))
ot_chart = sns.countplot(data=df, x='OverTime', hue='Attrition')
plt.title("OverTime vs Attrition")

# Add data labels
for p in ot_chart.patches:
    height = p.get_height()
    if height > 0:
        ot_chart.annotate(f'{height}', 
                          (p.get_x() + p.get_width()/2., height),
                          ha='center', va='bottom', fontsize=10, color='black')
plt.show()


#  Job Role vs Attrition
plt.figure(figsize=(10,6))
job_chart = sns.countplot(data=df, y='JobRole', hue='Attrition')
plt.title("Attrition by Job Role")

# Add data labels
for p in job_chart.patches:
    width = p.get_width()
    if width > 0:
        job_chart.annotate(f'{width}', 
                           (width, p.get_y() + p.get_height()/2.),
                           ha='left', va='center', fontsize=10, color='black')
plt.show()


#  Simplified Correlation Heatmap (Key Numeric Columns)
important_cols = [
    'Age','MonthlyIncome','DistanceFromHome',
    'JobLevel','TotalWorkingYears',
    'YearsAtCompany','YearsSinceLastPromotion','YearsWithCurrManager'
]
plt.figure(figsize=(8,6))
sns.heatmap(df[important_cols].corr(), annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Correlation Heatmap (Key Numeric Columns)")
plt.show()

