import pandas as pd
import numpy as np

customers = pd.DataFrame({
    "customer_id": [101,102,103,104,105],
    "customer_name": ["Shikhar","Rahul","Priya","Aman","Neha"],
    "city": ["Delhi","Lucknow","Delhi","Mumbai","Pune"]
})

products = pd.DataFrame({
    "product_id":[201,202,203,204],
    "product_name":["Laptop","Mouse","Keyboard","Monitor"],
    "category":["Electronics","Accessories","Accessories","Electronics"]
})

orders = pd.DataFrame({
    "order_id":[1,2,3,4,5,6,7,8],
    "customer_id":[101,102,101,103,104,105,102,106],
    "product_id":[201,202,203,201,204,202,204,201],
    "order_amount":[70000,np.nan,2500,65000,18000,900,22000,75000],
    "status":["Delivered","Returned","Delivered","Delivered",
              "Returned","Delivered","Delivered","Delivered"],
    "order_date":[
        "2026-01-05",
        "2026-01-12",
        "2026-02-10",
        "2026-02-15",
        "2026-03-01",
        "2026-03-18",
        "2026-03-20",
        "2026-02-28"
    ]
})





# ============================================================
# QUESTION 9 — E-Commerce Return Analysis Pipeline
# CATEGORY: Pandas (Merge + GroupBy + Transform + Apply + Datetime)
# DIFFICULTY: Hard (Data Analyst Interview Level)
# ============================================================

# DATA STRUCTURES:

import pandas as pd
import numpy as np

customers = pd.DataFrame({
    "customer_id": [101,102,103,104,105],
    "customer_name": ["Shikhar","Rahul","Priya","Aman","Neha"],
    "city": ["Delhi","Lucknow","Delhi","Mumbai","Pune"]
})

products = pd.DataFrame({
    "product_id":[201,202,203,204],
    "product_name":["Laptop","Mouse","Keyboard","Monitor"],
    "category":["Electronics","Accessories","Accessories","Electronics"]
})

orders = pd.DataFrame({
    "order_id":[1,2,3,4,5,6,7,8],
    "customer_id":[101,102,101,103,104,105,102,106],
    "product_id":[201,202,203,201,204,202,204,201],
    "order_amount":[70000,np.nan,2500,65000,18000,900,22000,75000],
    "status":[
        "Delivered",
        "Returned",
        "Delivered",
        "Delivered",
        "Returned",
        "Delivered",
        "Delivered",
        "Delivered"
    ],
    "order_date":[
        "2026-01-05",
        "2026-01-12",
        "2026-02-10",
        "2026-02-15",
        "2026-03-01",
        "2026-03-18",
        "2026-03-20",
        "2026-02-28"
    ]
})


# ============================================================
# BUILD A CLASS:
#
# class EcommercePipeline:
# ============================================================


# ------------------------------------------------------------
# Method 1 — extract()
# ------------------------------------------------------------
#
# Merge orders with customers using LEFT JOIN.
#
# Merge the result with products using LEFT JOIN.
#
# Return the merged dataframe.
#
# ------------------------------------------------------------


# ------------------------------------------------------------
# Method 2 — clean()
# ------------------------------------------------------------
#
# Perform the following cleaning operations:
#
# 1. Fill missing order_amount using
#    category-wise median.
#
# 2. Flag rows where customer information
#    is missing.
#
# 3. Flag rows where product information
#    is missing.
#
# 4. Replace missing customer names
#    with "Unknown".
#
# Return cleaned dataframe.
#
# ------------------------------------------------------------


# ------------------------------------------------------------
# Method 3 — transform()
# ------------------------------------------------------------
#
# Convert order_date into datetime.
#
# Create:
#
# year
#
# month_name
#
# weekday
#
# Create a new column:
#
# is_return
#
# Returned  -> 1
# Delivered -> 0
#
# Use apply() + lambda.
#
# Return transformed dataframe.
#
# ------------------------------------------------------------


# ------------------------------------------------------------
# Method 4 — analyze()
# ------------------------------------------------------------
#
# Return ALL of the following:
#
# 1. Total Revenue by Category
#
#    Use groupby()
#
#
# 2. Total Revenue by City
#
#
# 3. Monthly Revenue Trend
#
#
# 4. Return Count per Category
#
#
# 5. Top Revenue Product
#
#    Use:
#
#    groupby() + idxmax()
#
#    Return the COMPLETE ROW.
#
#
# 6. Highest Spending Customer
#
#    Use:
#
#    groupby() + idxmax()
#
#    Return the COMPLETE ROW.
#
#
# 7. Average Order Value by City
#
#
# 8. Number of Orders per Customer
#
#
# 9. Revenue Contribution Percentage
#
#    For every order calculate:
#
#    revenue_percent =
#
#    (order_amount / total_company_revenue) * 100
#
#    Use transform().
#
# ------------------------------------------------------------


# ------------------------------------------------------------
# Method 5 — run()
# ------------------------------------------------------------
#
# Execute the complete pipeline.
#
# Print:
#
# Merged Data
#
# Cleaned Data
#
# Transformed Data
#
# Revenue by Category
#
# Revenue by City
#
# Monthly Revenue Trend
#
# Return Count per Category
#
# Top Revenue Product
#
# Highest Spending Customer
#
# Average Order Value by City
#
# Orders Per Customer
#
# Revenue Contribution Percentage
#
# ------------------------------------------------------------



class EcommercePipeline:
    def __init__(self , customers , products , orders ):
        self.customers=customers
        self.products= products
        self.orders=orders

    def extract(self):
        df=pd.merge(self.customers , self.orders , on="customer_id" , how="left")
        df=pd.merge(df , self.products , on = "product_id" , how='left')
        return df

    def clean (self):
        df=self.extract()
        flagged_df=df.copy()
        flagged_df["Reason"]=""

        
        for col in df.columns:
            if df[col].dtype == "object":
                df[col] = df[col].fillna("Unknown")
            else:
                df[col] = df[col].fillna(df[col].median())
                return df



ecp=EcommercePipeline(customers , products , orders )
print("\n THE MERGED DATA FRAME IS : \n" ,ecp.extract())
print("\n THE FLAGGED DATA IS : \n" , ecp.clean())