# ============================================
# PANDAS PHASE 1 + 2 + 3 INTEGRATED PRACTICE
# Date: 05 JULY 2026
# Phase 3 topics: groupby, agg, value_counts,
# pivot_table, sort_values
# Integrated with: OOP, Exception Handling,
# Lambda, apply(), File Handling
# ============================================

import pandas as pd
import numpy as np

# ============================================
# QUESTION 1
# A retail company gives you this raw sales data.
# It has the usual mess — inconsistent product names,
# missing quantities, and duplicate entries.
# After cleaning it, management wants to know total
# revenue per product category and which category
# performed best.

sales = {
    "order_id": [1, 2, 3, 4, 5, 6, 7, 8, 9, 2],
    "product": ["  laptop", "MOUSE", "Laptop", "keyboard  ",
               "MOUSE  ", "Monitor", "keyboard", "Laptop",
               "monitor  ", "MOUSE"],
    "category": ["Electronics", "electronics", "Electronics",
                "Accessories", "electronics", "Electronics",
                "accessories", "Electronics", "electronics",
                "electronics"],
    "quantity": [2, np.nan, 1, 3, 5, 2, np.nan, 1, 3, 5],
    "unit_price": [65000, 500, 65000, 1200, 500,
                  15000, 1200, 65000, 15000, 500]
}

# Build a class SalesAnalyzer with:
# - Method clean() that:
#       removes duplicate order_ids
#       standardizes product and category (strip + title)
#       fills missing quantity with median quantity
# - Method revenue_by_category() that:
#       adds a revenue column (quantity * unit_price)
#       returns total revenue grouped by category
# - Method top_product() that:
#       returns the product with highest total revenue
# - Method summary() that:
#       prints shape before and after cleaning
#       prints category revenue
#       prints top product
df=pd.DataFrame(sales)
class SalesAnalyzer:
    def __init__(self,df):
        self.original_df=df.copy()
        self.df = df.copy()

    def clean(self):
        self.df["order_id"]=self.df["order_id"].drop_duplicates()
        self.df.dropna(how='any',inplace=True)
        self.df["product"]=self.df["product"].str.strip().str.title()
        self.df["category"]=self.df["category"].str.strip().str.title()
        self.df["quantity"]=self.df["quantity"].fillna(self.df["quantity"].mean())
        self.df = self.df.reset_index(drop=True)
        return self.df
    
    def revenue_by_category(self):
        self.df["revenue"]=self.df["quantity"]*self.df["unit_price"]
        self.df.groupby("category")["revenue"].sum()
        return self.df
    

    def top_product(self):
        print("THE PRODUCT WITH THE HIGHEST TOTAL REVENUE IS :")
        return self.df.groupby("product")['revenue'].sum().idxmax()


    def summary(self):
       print("Shape before cleaning:", self.original_df.shape)
       print("Shape after cleaning :" , self.df.shape)
       print("\nTHE CATEGORY REVENUE IS :\n")
       print(self.df.groupby("category")["revenue"].sum()) 
       print("\nTop Product:")
       print(self.df.groupby("product")["revenue"].sum().sort_values(ascending=False).head(1))
       print("\nTHE TOP THREE PRODUCTS ARE :\n")
       print(self.df.groupby("product")["revenue"].sum().sort_values(ascending=False).head(3))

       
ss=SalesAnalyzer(df)
ss.clean()
print(ss.revenue_by_category())
print(ss.top_product())
ss.summary()
# ============================================

# QUESTION 2
# An HR team gives you employee data across departments.
# Some salaries are missing, some department names are
# inconsistent. After cleaning, they want:
# average salary per department, headcount per department,
# and the department with the highest average salary.

hr_data = {
    "emp_id": [1, 2, 3, 4, 5, 6, 7, 8],
    "name": ["Shikhar", "Rahul", "Priya", "Aditya",
            "Sneha", "Karan", "Meera", "Vikram"],
    "department": ["Data", "IT", "data", "HR",
                  "IT ", "Data", " hr", "IT"],
    "salary": [90000, np.nan, 95000, 45000,
              60000, np.nan, 48000, 62000]
}

# Build a class HRAnalyzer with:
# - Method clean() that standardizes department names
#   and fills missing salary with department-wise mean
#   using groupby().transform()
# - Method dept_stats() that returns a DataFrame showing
#   average salary and headcount per department
#   using groupby() with agg()
# - Method highest_paid_dept() that returns the department
#   name with the highest average salary


# ============================================

# QUESTION 3
# A school principal wants a full performance report
# on students. The data has missing marks, inconsistent
# branch names, and needs both individual and group-level
# analysis.

school_data = {
    "roll_no": [1, 2, 3, 4, 5, 6, 7, 8],
    "name": ["Shikhar", "Rahul", "Priya", "Aditya",
            "Sneha", "Karan", "Meera", "Vikram"],
    "branch": ["CSE", "cse", "ECE", "Ece",
               "CSE ", " ece", "CSE", "ECE"],
    "maths": [95, 60, np.nan, 38, 97, 55, 42, 75],
    "science": [88, 72, 89, np.nan, 91, 60, 55, 80],
    "english": [76, 65, 82, 70, np.nan, 58, 48, 72]
}

# Build a class SchoolReport with:
# - Method clean() that standardizes branch names and
#   fills missing subject marks with that subject's mean
# - Method add_student_stats() that adds:
#       total marks column (sum of all 3 subjects)
#       average marks column
#       grade column using apply():
#       A(>=85), B(>=70), C(>=55), D(>=40), F
# - Method branch_performance() that returns
#   average marks per branch using groupby()
# - Method top_students(n) that returns top n students
#   sorted by total marks


# ============================================

# QUESTION 4 — HARDEST
# You're a data analyst at a startup. You receive a
# CSV file path as input (write the CSV first using
# file handling). The file contains order data that
# needs full cleaning and analysis.
# This simulates exactly what happens on Day 1 of a
# DA internship.

order_data = {
    "order_id": [101, 102, 103, 104, 105, 106, 107, 101],
    "customer": ["  shikhar", "RAHUL  ", "Priya", "  ADITYA",
                "sneha", "karan  ", "Meera", "  shikhar"],
    "product": ["Laptop", "laptop  ", "MOUSE", "Mouse",
               "KEYBOARD", "keyboard", "Monitor", "Laptop"],
    "category": ["Electronics", "electronics", "Electronics",
                "Electronics", "Accessories", "accessories",
                "Electronics", "Electronics"],
    "quantity": [2, 1, np.nan, 3, 2, np.nan, 1, 2],
    "unit_price": [65000, 65000, 500, 500,
                  1200, 1200, 15000, 65000]
}

# Build a class OrderPipeline with:
# - Method write_raw_csv(filepath) that writes
#   order_data to a CSV file using file handling
# - Method extract(filepath) that reads the CSV
#   using pd.read_csv() with FileNotFoundError handling
# - Method clean() that:
#       removes duplicate order_ids
#       standardizes customer, product, category
#       fills missing quantity with median
# - Method transform() that adds:
#       revenue column (quantity * unit_price)
#       revenue_tier using apply() + lambda:
#       "High" if revenue >= 100000
#       "Medium" if revenue >= 10000
#       "Low" otherwise
# - Method analyze() that returns:
#       total revenue per category (groupby)
#       top customer by total revenue (groupby)
#       value_counts() of revenue_tier
# - Method run(filepath) that calls all steps
#   in order and prints a final summary report