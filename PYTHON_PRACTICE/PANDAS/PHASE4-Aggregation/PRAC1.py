# ============================================
# PANDAS PHASE 3 — Aggregation Deep Dive
# Date: 9 July 2026
# Topics: value_counts, agg, pivot_table, crosstab
# Integrated with: OOP, Exception Handling, Lambda, apply()
# ============================================

import pandas as pd
import numpy as np

employee_data = {
    "emp_id": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "name": ["Shikhar", "Rahul", "Priya", "Aditya",
             "Sneha", "Karan", "Meera", "Vikram",
             "Pooja", "Arjun"],
    "department": ["Data", "IT", "Data", "HR",
                   "IT", "Data", "HR", "IT",
                   "Data", "HR"],
    "city": ["Delhi", "Mumbai", "Delhi", "Kanpur",
             "Mumbai", "Delhi", "Kanpur", "Mumbai",
             "Delhi", "Kanpur"],
    "salary": [90000, np.nan, 95000, 45000,
               60000, np.nan, 48000, 62000,
               88000, 50000],
    "experience_years": [3, 5, 4, 2, 6, 3, 1, 7, 4, 2],
    "performance": ["High", "Medium", "High", "Low",
                    "Medium", "High", "Low", "Medium",
                    "High", "Low"]
}



# ============================================
# QUESTION 1 — value_counts() Deep Dive
# Using the employee DataFrame:
#
# - Count how many employees are in each department
# - Count how many employees are in each city
# - Count performance ratings distribution
# - Get value_counts() as percentages (normalize=True)
#   for the performance column
# - Find which city has the most employees
#   without using groupby — only value_counts()
# - Find employees where performance appears
#   more than once — use value_counts() + filtering

# YOUR CODE HERE:
df=pd.DataFrame(employee_data)
class Count:
    def __init__(self,df):
        self.df=df
    def loader(self):
        dept_count=self.df["department"].value_counts()
        city_count=self.df["city"].value_counts()
        performance=self.df["performance"].value_counts(normalize=True)
        city_emp=self.df["city"].value_counts().idxmax()
        perform= self.df["performance"].value_counts()
        duplicate=perform[perform>1]
        print( "\nTHE NUMBER OF EMPLOYEES IN EACH DEPARTMENT IS : \n",dept_count)  
        print("\nTHE NUMBER OF EMPLOYEE IN EACH CITY ARE: \n", city_count) 
        print("THE PERFORMANCE PERCENTAGE ARE: " , performance)
        print("\n THE CITY WITH THE MOST EMPLOYEES ARE :\n" , city_emp)
        print("\n THE EMPLOYEES WHERE PERFORMANCE APPEARED MORE THAN ONCE IS : \n" ,duplicate)

obj=Count(df)
obj.loader()
# ============================================
# QUESTION 2 — agg() Deep Dive
# Using the employee DataFrame:
# First fill missing salaries with department-wise mean.
#
# - Use groupby + agg() to get for each department:
#       min salary, max salary, mean salary, count of employees
#       name the aggregated columns properly
# - Use groupby + agg() to get for each city:
#       total salary bill, average experience, headcount
# - Use groupby on TWO columns (department + city)
#   and get average salary for each combination
# - Find which department + city combination has
#   the highest average salary

# YOUR CODE HERE:
class Data:
    def __init__(self, df):
        self.df = df

    def work(self):
        self.df["salary"]=self.df["salary"].fillna(self.df.groupby("department")["salary"].transform("mean"))
        summary=self.df.groupby("department")["salary"].agg(["mean", "max" , "min" , "count"])
        city_summary=self.df.groupby("city").agg({
            "salary":"sum" , 
            "experience_years":"mean" , 
            "name" :"count"
        })  
        combination= self.df.groupby(["department" , "city"])["salary"].mean()
        highest_avg_salary=self.df.groupby(["department" , "city"])["salary"].mean().idxmax()
        print("\nTHE FIXED DATA FRAME IS : \n", self.df ) 
        print("\nTHE  MEAN , MAX , MIN , COUNT OF THE FIXED DATA FRAME IS :\n", summary) 
        print("\nTHE DETAILS FOR EACH CITY IS : \n" , city_summary)
        print("\nTHE AVERAGE SALARY FOR EACH DEPARTMENT IN EACH CITY IS : \n" , combination)
        print("\n THE DEPARTMENT IN THE EACH CITY WITH THE HIGHEST AVERAGE SALARY IS : \n",highest_avg_salary)
        
    
D = Data(df)
D.work()
# ============================================
# QUESTION 3 — pivot_table()
# Using the employee DataFrame:
#
# - Create a pivot table showing average salary
#   with department as rows and city as columns
# - Create a pivot table showing employee count
#   with performance as rows and department as columns
#   use aggfunc='count'
# - Create a pivot table showing total salary
#   with city as rows and performance as columns
# - Add margins=True to one of the above pivot tables
#   and explain in a comment what margins adds

# YOUR CODE HERE:
class Employee : 
    def __init__(self , df):
        self.df=df
    def work(self):
        pivot= pd.pivot_table(df  ,   index="department" ,  columns="city" ,values="salary" , aggfunc="mean" )
        employee_count=pd.pivot_table(df , index="performance", columns="department" , values="name" , aggfunc="count")
        total_salary=pd.pivot_table(df , index="city" , columns="performance" , values="salary" , aggfunc="mean")
        margin_value=pd.pivot_table(df , index="performance", columns="department" , values="name" , aggfunc="count",margins=True)
        return pivot , employee_count , total_salary , margin_value

e=Employee(df)
print(e.work())
# ============================================
# QUESTION 4 — crosstab()
# Using the employee DataFrame:
#
# - Create a crosstab of department vs city
#   (shows how many employees from each dept are in each city)
# - Create a crosstab of performance vs department
# - Add normalize=True to one crosstab 
# YOUR CODE HERE:
class Demo:
    def __init__(self,df):
        self.df=df
    def cross(self):
        table1=pd.crosstab(df["department"] , df["city"])
        print("\nTHE CROSS TABLE OF DEPARTMENT VS. CITY IS : \n" , table1)
        table2=pd.crosstab(df["performance"] , df["department"], normalize=True)
        print("\nTHE CROSS TABLE OF PERFORMANCE VS . DEPARTMENT IS :\n",table2)

d=Demo(df)
d.cross()
# ============================================
# QUESTION 5 — HARDEST — Full Integration
# Build a class EmployeeAnalytics with ALL of the above:
#
# - Method clean() that:
#       fills missing salary with department-wise mean
#       standardizes department and city (title case)
# - Method headcount_report() that:
#       returns value_counts() for department, city,
#       and performance as a dictionary of three Series
# - Method salary_report() that:
#       uses agg() to return min, max, mean, count
#       per department
# - Method performance_pivot() that:
#       returns a pivot table of average salary
#       with performance as rows, department as columns
# - Method city_dept_crosstab() that:
#       returns crosstab of city vs department
# - Method flag_high_earners() that:
#       uses apply() + lambda to add "earner_flag":
#       "Top" if salary >= 85000
#       "Mid" if salary >= 55000
#       "Entry" otherwise
# - Method run() that calls all methods and prints
#       a complete analytics report

# YOUR CODE HERE:


