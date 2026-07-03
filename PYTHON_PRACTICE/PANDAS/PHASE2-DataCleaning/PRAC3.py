"""
===========================
PANDAS DATA CLEANING CHALLENGE
===========================

Objective:
Clean and preprocess the given employee dataset using Pandas.

Instructions:
- Write clean, readable code.
- Do NOT modify the dataset manually.
- Use appropriate Pandas functions.
- Print the output wherever required.
"""

import pandas as pd
import numpy as np

# ==========================
# Dataset
# ==========================

employees = {
    "employee ID": [101, 102, 103, 104, 104, 105, 106, 107],
    "name": [
        "  shikhar ",
        "RAHUL",
        None,
        "Priya ",
        "Priya ",
        " aDiTyA",
        "Karan",
        "Neha "
    ],
    "department": [
        "IT",
        "hr",
        "Finance",
        "IT",
        "IT",
        None,
        "Hr",
        " finance "
    ],
    "email": [
        "Shikhar@GMAIL.com",
        "rahul@yahoo.com",
        None,
        "PRIYA@gmail.COM",
        "PRIYA@gmail.COM",
        "aditya@outlook.com",
        "karan@gmail.com",
        "NEHA@GMAIL.COM"
    ],
    "salary": [
        "60000",
        "45000",
        "55000",
        None,
        None,
        "70000",
        "52000",
        "48000"
    ],
    "experience": [
        2,
        np.nan,
        4,
        5,
        5,
        np.nan,
        3,
        2
    ],
    "status": [
        "ACTIVE",
        "inactive",
        "Pending",
        "ACTIVE",
        "ACTIVE",
        "pending",
        "Inactive",
        "active"
    ]
}

df = pd.DataFrame(employees)

# ==========================================================
# PART 1 - Explore the Data
# ==========================================================

# 1. Print the first 5 rows.
# 2. Print the last 3 rows.
# 3. Print the shape of the DataFrame.
# 4. Print all column names.
# 5. Print the data types of each column.
# 6. Print DataFrame information using info().
class Panda_practice:
    def __init__(self,df):
        self.df=df

    def explore(self):
        print("\nTHE FIRST FIVE ROWS OF THE DATA SET ARE : \n",self.df.head(5))
        print("\nTHE LAST THREE ROWS OF THE DATA ARE:\n", self.df.tail(3))
        print("\nTHE SHAPE OF THE DATA FRAME IS :\n" , self.df.shape)
        print("\nTHE NAME OF ALL THE COLUMNS ARE : \n",self.df.info() )
        print("\nTHE DATA TYPE OF EACH COLUMN IS : \n" , self.df.dtypes)

    
        
# ==========================================================
# PART 2 - Missing Values
# ==========================================================

# 7. Find the number of missing values in each column.
# 8. Find the total number of missing values in the DataFrame.
# 9. Display only those rows that contain at least one missing value.
# 10. Fill missing Salary values with the mean Salary.
# 11. Fill missing Experience values with 0.
# 12. Fill missing Department values with "Unknown".
# 13. Fill missing Name values with "Missing".
    def missing(self):
        print("\nTHE TOTAL NUMBER OF MISSING VALUES IN EACH COLUMN IS : \n", self.df.isnull().sum())
        print("\nTHE TOTAL NUMBER OF MISSING VALUES  IN THE WHOLE DATA FRAME IS :\n" , self.df.isnull().sum().sum())
        print("\nTHE ROWS HAVING ATLEAST ONE MISSING VALUES: \n" , self.df[self.df.isnull().any(axis=1)])
        self.df["salary"] = self.df["salary"].fillna(self.df["salary"].mean())
        self.df["experience"]=self.df["experience"].fillna(0)
        self.df["department"]=self.df["department"].fillna("Unknown")
        self.df["name"]=self.df["name"].fillna("Missing")
        return self.df

# ==========================================================
# PART 3 - Duplicate Handling
# ==========================================================

# 14. Check which rows are duplicates.
# 15. Count the number of duplicate rows.
# 16. Remove duplicate rows.
# 17. Print the new shape of the DataFrame.
    def duplicate(self):
        print("THE ROWS WHICH ARE DUPLICATES ARE : ",self.df.duplicated())
        print("THE TOTAL NUMBER OF DUPLICATED ROWS ARE : ",self.df.duplicated.sum())
        
# ==========================================================
# PART 4 - String Cleaning
# ==========================================================

# 18. Remove leading/trailing spaces from:
#       - Name
#       - Department
#       - Email

# 19. Convert:
#       - Name to Title Case
#       - Department to lowercase
#       - Email to lowercase

# 20. Replace department values:
#       it -> IT
#       hr -> HR
#       finance -> Finance
#       unknown -> Unknown

# 21. Replace status values:
#       active -> Active
#       inactive -> Inactive
#       pending -> Pending

# ==========================================================
# PART 5 - Data Type Conversion
# ==========================================================

# 22. Convert Salary from string to integer.
# 23. Verify the data types again.

# ==========================================================
# PART 6 - Creating New Columns
# ==========================================================

# 24. Create a new column called "Email_Domain"
#     Example:
#     shikhar@gmail.com -> gmail.com

# Hint:
# .str.split("@").str[1]

# 25. Create a new column called "Salary_Category"

# Rules:
# Salary < 50000           -> Low
# Salary between 50000-65000 -> Medium
# Salary > 65000           -> High

# (Hint: Use apply() or np.select())

# ==========================================================
# PART 7 - Filtering
# ==========================================================

# 26. Display all Gmail users.
# 27. Display all employees from the IT department.
# 28. Display employees earning more than ₹50,000.
# 29. Display employees having experience greater than 3 years.
# 30. Display employees whose names contain "ra" (case insensitive).

# ==========================================================
# PART 8 - Statistics
# ==========================================================

# 31. Find:
#       - Average Salary
#       - Maximum Salary
#       - Minimum Salary

# 32. Count employees in each department.
# 33. Count employees in each status.
# 34. Count unique email domains.
# 35. Display all unique departments.

# ==========================================================
# PART 9 - Rename Columns
# ==========================================================

# Rename the following columns:

# Employee ID -> emp_id
# Name        -> emp_name
# Salary      -> salary
# Department  -> department

# ==========================================================
# PART 10 - Final Output
# ==========================================================

# 36. Print the cleaned DataFrame.
# 37. Print df.info() to verify the cleaning.
# 38. Save the cleaned DataFrame as:
#
#     clean_employee_data.csv
#
# using:
#
# df.to_csv()
#
# ==========================================================
# BONUS (Interview Level)
# ==========================================================

# 39. Which department has the highest average salary?

# 40. Which email domain occurs most frequently?

# 41. How many employees are Active?

# 42. Sort employees by Salary in descending order.

# 43. Reset the index after removing duplicates.

# 44. Save only Gmail users into a new DataFrame called:
#
# gmail_users
#
# and print it.


