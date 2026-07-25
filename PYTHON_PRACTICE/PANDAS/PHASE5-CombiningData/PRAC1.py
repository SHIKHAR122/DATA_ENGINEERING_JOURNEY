# ============================================
# PANDAS PHASE 5 — Combining DataFrames
# Date: 20 July 2026
# Topics: merge(), concat(), join(),
# merge conflicts, suffixes
# Integrated with: OOP, Exception Handling,
# Lambda, apply(), Phase 2+3 concepts
# ============================================

import pandas as pd
import numpy as np

# ============================================
# QUESTION 1 — merge() Basics
# You have two tables from an e-commerce system:

customers = pd.DataFrame({
    "customer_id": [1, 2, 3, 4, 5],
    "name": ["Shikhar", "Rahul", "Priya", "Aditya", "Sneha"],
    "city": ["Delhi", "Mumbai", "Delhi", "Kanpur", "Mumbai"]
})

orders = pd.DataFrame({
    "order_id": [101, 102, 103, 104, 105, 106],
    "customer_id": [1, 2, 1, 3, 6, 4],
    "amount": [5000, 3000, 8000, 2000, 4000, 6000]
})

# - INNER JOIN: merge customers and orders on customer_id
#   explain in a comment: why does order 105 disappear?
# - LEFT JOIN: merge customers and orders
#   explain in a comment: what happens to customer 5?
# - RIGHT JOIN: merge customers and orders
#   explain in a comment: what happens to order 105?
# - Find customers who have placed more than one order
#   using merge + value_counts()

# YOUR CODE HERE:
class Merge_practice:
    def __init__(self,customers , orders):
        self.orders=orders
        self.customers=customers

    def inner_clean(self):
        inner_join_df=pd.merge(orders, customers , on= "customer_id" , how='inner')
        return inner_join_df

    def left_clean(self):
        left_join_df=pd.merge(orders, customers , on= "customer_id" , how='left')
        return left_join_df

    def right_clean(self):    
        right_join_df=pd.merge(orders, customers , on= "customer_id" , how='right')
        return right_join_df

    def count(self):
        customer_df= pd.merge(orders , customers , on= "customer_id" , how="inner")
        count_df= customer_df["customer_id"].value_counts()
        result=count_df[count_df>1]
        return result
     

m=Merge_practice(customers , orders)
print("\n THE TABLES AFTER INNER JOIN IN THE TABLE IS : \n",m.inner_clean())
print("\n HE TABLES AFTER LEFT JOIN IN THE TABLE IS: \n",m.left_clean())
print("\nTHE TABLES AFTER THE RIGHT JOIN IN THE TABLE IS : \n",m.right_clean())
print("\nTHE COUNT OF THE CUSTOMERS WHO HAVE PLACED MORE THAN 1 ORDERS ARE :\n",m.count())
# ============================================
# QUESTION 2 — concat() Basics
# You have sales data split across two quarters:

q1_sales = pd.DataFrame({
    "sale_id": [1, 2, 3],
    "product": ["Laptop", "Mouse", "Keyboard"],
    "amount": [65000, 500, 1200],
    "quarter": ["Q1", "Q1", "Q1"]
})

q2_sales = pd.DataFrame({
    "sale_id": [4, 5, 6],
    "product": ["Monitor", "Webcam", "Chair"],
    "amount": [15000, 2000, 8000],
    "quarter": ["Q2", "Q2", "Q2"]
})

extra_info = pd.DataFrame({
    "sale_id": [1, 2, 3, 4, 5, 6],
    "salesperson": ["Shikhar", "Rahul", "Priya",
                   "Aditya", "Sneha", "Karan"]
})

# - Concatenate q1_sales and q2_sales row-wise
#   (stack them vertically)
# - Reset the index after concatenating
# - Concatenate q1_sales and extra_info column-wise
#   explain in a comment: what does axis=1 do differently


# YOUR CODE HERE:

class concatenate:
    def __init__(self,q1_sales , q2_sales):
        self.q1_sales=q1_sales
        self.q2_sales=q2_sales
        self.extra_info=extra_info


    def concatinate(self):
        concatenated_table=pd.concat([q1_sales,q2_sales])
        return concatenated_table
    

    def concatinate_vertical(self):
        vertical_concatinate=pd.concat([q1_sales , q2_sales],axis=1)
        return vertical_concatinate

c=concatenate(q1_sales  , q2_sales)
print("\n HORIZONTALLY CONCATINATED TABLE ARE :\n",c.concatinate())
print("\n VERTICALLY CONCATINATED TABLE ARE :\n",c.concatinate_vertical())




# ============================================
# QUESTION 3 — Handling Merge Conflicts + Suffixes
# Two systems recorded employee data independently
# and both have a "salary" column but with different values:

hr_system = pd.DataFrame({
    "emp_id": [1, 2, 3, 4],
    "name": ["Shikhar", "Rahul", "Priya", "Aditya"],
    "salary": [90000, 60000, 85000, 45000],
    "department": ["Data", "IT", "Data", "HR"]
})

finance_system = pd.DataFrame({
    "emp_id": [1, 2, 3, 5],
    "salary": [92000, 58000, 85000, 70000],
    "bonus": [10000, 5000, 8000, 6000]
})

# - Merge both systems on emp_id using INNER JOIN
#   notice the conflict — both have "salary" column
# - Use suffixes=("_hr", "_finance") to distinguish them
# - Add a column "salary_difference" = salary_hr - salary_finance
# - Find employees where HR and finance salaries don't match
# - Do a LEFT JOIN to keep all HR employees
#   and explain what happens to emp_id 4 (Aditya)

# YOUR CODE HERE:
class Merge_conflicts:
    def __init__(self, hr_system, finance_system):
        self.hr_system=hr_system
        self.finance_system=finance_system


    def join_inner(self):
        merged_system=pd.merge(hr_system , finance_system , on="emp_id" , how="inner", suffixes=("_hr","_finance")) 
        merged_system["salary_difference"]=(merged_system["salary_hr"]-merged_system["salary_finance"])
        mismatch = merged_system[merged_system["salary_hr"] != merged_system["salary_finance"]]
        print("\nTHE MISMATCHED DATA FROM THE TABLE IS : \n")
        print(mismatch)
        return merged_system       

   

mc=Merge_conflicts(hr_system , finance_system)
print("\nTHE MERGED TABLE IS : \n",mc.join_inner())


# ============================================
# QUESTION 4 — Multiple Table Merges
# A school has three separate tables:

students = pd.DataFrame({
    "student_id": [1, 2, 3, 4, 5],
    "name": ["Shikhar", "Rahul", "Priya", "Aditya", "Sneha"],
    "branch": ["CSE", "ECE", "CSE", "ME", "CSE"]
})

marks = pd.DataFrame({
    "student_id": [1, 2, 3, 4, 6],
    "maths": [95, 60, 89, 38, 75],
    "science": [88, 72, 91, 55, 80]
})

attendance = pd.DataFrame({
    "student_id": [1, 2, 3, 5, 6],
    "attendance_pct": [92, 65, 88, 95, 70]
})

# - Merge students with marks on student_id (LEFT JOIN)
#   explain what happens to student 5 (Sneha)
# - Then merge the result with attendance (LEFT JOIN)
#   explain what happens to student 4 (Aditya)
# - After both merges, fill missing values appropriately
# - Add a "result" column:
#   "Pass" if maths >= 40 AND science >= 40
#         AND attendance_pct >= 75
#   "Fail" otherwise
#   use apply() with axis=1

# YOUR CODE HERE:
class work:
    def __init__(self,students, attendance , marks):
        self.students=students
        self.attendance=attendance
        self.marks=marks


    def transform(self):
        left_joined_df= pd.merge(students,marks, on= "student_id", how='left')
        final_left_df=pd.merge(left_joined_df,attendance,on="student_id",how='left')
        final_left_df.fillna({"maths": 0,"science": 0,"attendance_pct": 0}, inplace=True)
        final_left_df["result"]=final_left_df.apply(lambda df: "PASS" if df["maths"]>=40 and df["science"]>=40 and df["attendance_pct"]>=75 else "FAIL",axis=1)

        return final_left_df



    
w=work(students , attendance, marks)
print("\nTHE TABLE RESULT IS : \n",w.transform())
# ============================================
# QUESTION 5 — HARDEST — Full Integration
# Build a class DataMerger that simulates
# a real DA task — merging data from multiple
# sources, handling conflicts, and producing
# a final clean report.

raw_orders = pd.DataFrame({
    "order_id": [101, 102, 103, 104, 105],
    "customer_id": [1, 2, 1, 3, 4],
    "product_id": [501, 502, 503, 501, 504],
    "quantity": [2, 1, 3, np.nan, 2],
    "order_date": ["2026-01-15", "2026-02-10",
                  "2026-03-05", "2026-01-20", "2026-02-28"]
})

raw_customers = pd.DataFrame({
    "customer_id": [1, 2, 3, 5],
    "name": ["Shikhar", "Rahul", "Priya", "Sneha"],
    "segment": ["Premium", "Standard", "Premium", "Budget"]
})

raw_products = pd.DataFrame({
    "product_id": [501, 502, 503, 504],
    "product_name": ["Laptop", "Mouse", "Keyboard", "Monitor"],
    "unit_price": [65000, 500, 1200, 15000]
})

# Build a class DataMerger with:
# - Method merge_all() that:
#       merges orders with customers on customer_id
#       then merges result with products on product_id
#       use LEFT JOINs throughout
#       fills missing quantity with median
#       adds revenue column (quantity * unit_price)
#       explain in comments what happens to order 104
#       (customer_id=3 exists but customer_id=4 doesn't)
# - Method segment_revenue() that:
#       groups by segment and returns total revenue
#       using groupby + agg()
# - Method flag_missing() that:
#       identifies rows where customer or product
#       info is missing after merge
#       returns those rows as a separate DataFrame
# - Method run() that calls all methods and
#       prints a complete pipeline report

# YOUR CODE HERE:

class DataMerger:

    def __init__(self, raw_orders, raw_customers, raw_products):
        self.raw_orders = raw_orders
        self.raw_customers = raw_customers
        self.raw_products = raw_products

    def merge_all(self):

        df = pd.merge(self.raw_orders,self.raw_customers,on="customer_id",how="left")
        df = pd.merge(df,self.raw_products,on="product_id",how="left")
        # df.fillna({"name": "NA","segment": "NA","quantity": df["quantity"].median()}, inplace=True)
        df["revenue"] = df["quantity"] * df["unit_price"]
        return df

    def segment_revenue(self, final_df):
        return final_df.groupby("segment")["revenue"].sum()


    def flag_Missing(self):
        df=self.merge_all()

        df["customer_missing"]=df["name"].isna()
        df["segment_missing"]=df["segment"].isna()
        df["quantity_missing"]=df["quantity"].isna()


        return df



dm = DataMerger(raw_orders, raw_customers, raw_products)
df = dm.merge_all()
print(df)
print(dm.segment_revenue(df))
print(dm.flag_Missing())