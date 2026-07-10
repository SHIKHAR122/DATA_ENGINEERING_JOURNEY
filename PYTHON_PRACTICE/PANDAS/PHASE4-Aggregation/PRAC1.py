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

df = pd.DataFrame(employee_data)

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


# ============================================
# QUESTION 4 — crosstab()
# Using the employee DataFrame:
#
# - Create a crosstab of department vs city
#   (shows how many employees from each dept are in each city)
# - Create a crosstab of performance vs department
# - Add normalize=True to one crosstab and explain
#   in a comment the difference between crosstab
#   with and without normalize
# - In a comment explain: what is the difference
#   between pivot_table and crosstab? When would
#   you use one over the other?

# YOUR CODE HERE:


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


