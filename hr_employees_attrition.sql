CREATE TABLE hr_attrition (
Age INT,
Attrition VARCHAR(10),
BusinessTravel VARCHAR(50),
DailyRate INT,
Department VARCHAR(50),
DistanceFromHome INT,
Education INT,
EducationField VARCHAR(100),
EmployeeCount INT,
EmployeeNumber INT PRIMARY KEY,
EnvironmentSatisfaction INT,
Gender VARCHAR(10),
HourlyRate INT,
JobInvolvement INT,
JobLevel INT,
JobRole VARCHAR(100),
JobSatisfaction INT,
MaritalStatus VARCHAR(20),
MonthlyIncome INT,
MonthlyRate INT,
NumCompaniesWorked INT,
Over18 CHAR(1),
OverTime VARCHAR(5),
PercentSalaryHike INT,
PerformanceRating INT,
RelationshipSatisfaction INT,
StandardHours INT,
StockOptionLevel INT,
TotalWorkingYears INT,
TrainingTimesLastYear INT,
WorkLifeBalance INT,
YearsAtCompany INT,
YearsInCurrentRole INT,
YearsSinceLastPromotion INT,
YearsWithCurrManager INT
);

SELECT * FROM hr_attrition;

-- Overall Attrition Rate
SELECT 
	(SUM(CASE WHEN Attrition='Yes' THEN 1 ELSE 0 END)*100.0)/COUNT(*) AS Attrition_Rate
FROM hr_attrition;

-- Department-wise Attrition
SELECT Department,
	COUNT(*) AS TotalEmployees,
	SUM(CASE WHEN Attrition='Yes' THEN 1 ELSE 0 END) AS Left_Employees,
	ROUND(SUM(CASE WHEN Attrition='Yes' THEN 1 ELSE 0 END)*100/COUNT(*),2) AS Attrition_Percent
FROM hr_attrition
GROUP BY Department
ORDER BY Attrition_Percent DESC;

-- OverTime impact
SELECT OverTime,
	COUNT(*) AS TotalEmployees,
	SUM(CASE WHEN Attrition='Yes' THEN 1 ELSE 0 END) AS Left_employees,
	AVG(MonthlyIncome) AS Avg_income
FROM hr_attrition
GROUP BY OverTime;


-- JobRole attrition
SELECT JobRole,
	SUM(CASE WHEN Attrition='Yes' THEN 1 ELSE 0 END) AS Left_employees,
	COUNT(*)AS Total_employees
FROM hr_attrition
GROUP BY JobRole
ORDER BY Left_employees Desc;

-- Salary band attriton
SELECT 
CASE 
	WHEN MonthlyIncome<5000 THEN 'Low' 
	WHEN MonthlyIncome BETWEEN 5000 AND 10000 THEN 'Medium'
	ELSE 'High'
END AS IncomeBand,
SUM(CASE WHEN Attrition='Yes' THEN 1 ELSE 0 END) AS Left_employees,
COUNT(*)AS Total_employees,
(SUM(CASE WHEN Attrition='Yes' THEN 1 ELSE 0 END)*100)/COUNT(*)AS Attrition_percent
FROM hr_attrition
GROUP BY IncomeBand;