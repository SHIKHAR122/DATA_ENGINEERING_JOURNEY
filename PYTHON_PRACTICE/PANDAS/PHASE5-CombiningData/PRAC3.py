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
# class EcommercePipeline:
# ===========================================================
# ------------------------------------------------------------
# Method 1 — extract()
# ------------------------------------------------------------
# Merge orders with customers using LEFT JOIN.
# Merge the result with products using LEFT JOIN.
# Return the merged dataframe.
# ------------------------------------------------------------
# ------------------------------------------------------------
# Method 2 — clean()
# ------------------------------------------------------------
# Perform the following cleaning operations:
# 1. Fill missing order_amount using
#    category-wise median.
# 2. Flag rows where customer information
#    is missing.
# 3. Flag rows where product information
#    is missing.
# 4. Replace missing customer names
#    with "Unknown".
# Return cleaned dataframe.
# -----------------------------------------------------------
# ------------------------------------------------------------
# Method 3 — transform()
# ------------------------------------------------------------
# Convert order_date into datetime.
# Create:
# year
# month_name
# weekday
# Create a new column:
# is_return
# Returned  -> 1
# Delivered -> 0
# Use apply() + lambda.
# Return transformed dataframe.
# ------------------------------------------------------------
# ------------------------------------------------------------
# Method 4 — analyze()
# ------------------------------------------------------------
# Return ALL of the following:
# 1. Total Revenue by Category
#    Use groupby()
# 2. Total Revenue by City
# 3. Monthly Revenue Trend
# 4. Return Count per Category
# 5. Top Revenue Product
#    Use:
#    groupby() + idxmax()
#    Return the COMPLETE ROW.
# 6. Highest Spending Customer
#    Use
#    groupby() + idxmax()
#    Return the COMPLETE ROW.
# 7. Average Order Value by City
# 8. Number of Orders per Customer
# 9. Revenue Contribution Percentage
#    For every order calculate:
#    revenue_percent =
#    (order_amount / total_company_revenue) * 100
#    Use transform().
# ------------------------------------------------------------
# ------------------------------------------------------------
# Method 5 — run()
# ------------------------------------------------------------
# Execute the complete pipeline.#
# Print:
# Merged Data
# Cleaned Data
# Transformed Data
# Revenue by Category
# Revenue by City
# Monthly Revenue Trend
# Return Count per Category
# Top Revenue Product
# Highest Spending Customer
# Average Order Value by City
# Orders Per Customer
# Revenue Contribution Percentage
# -----------------------------------------------------------


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
     df["missing_customer"]=df[["customer_id"]].isnull().any(axis=1)
     df["product_missing"]=df[["product_id" , "product_name"]].isnull().any(axis=1)
     df["orders_missing"]=df[["order_id","order_amount","order_date"]].isnull().any(axis=1)
     df["customer_name"]=df["customer_name"].fillna("UNKNOWN")  
     df["order_amount"]=df["order_amount"].fillna(df.groupby("category")["order_amount"].transform("mean"))
     cleaned_df=df.copy()

     return cleaned_df



    def transform(self):
       df=self.extract()
       df=self.clean()
       df["order_date"]=pd.to_datetime(df["order_date"])
       df["year"]=df["order_date"].dt.year
       df["month"]=df["order_date"].dt.month
       df["weekday"]=df["order_date"].dt.weekday
       df["is_return"]=df["status"].apply(lambda x : 0 if x=="Delivered" else 1)
       transformed_df=df.copy()
       return transformed_df


    def analyze(self):
       df=self.extract()
       df=self.clean()
       df=self.transform()
       category_revenue=df.groupby("category")["order_amount"].transform("mean")
       revenue_per_city=df.groupby("city")["order_amount"].transform("mean")
       monthly_trend=df.groupby("month")["order_amount"].transform("mean")
       count_per_category=df.groupby("category")["customer_id"].transform("count")
       idx = df.groupby("customer_id")["order_amount"].idxmax()
       highest_paying_customer = df.loc[idx]
       average_order_by_city=df.groupby("city")["order_amount"].transform("mean")
       number_of_orders_per_customer = (df.groupby("customer_name")["order_id"].count())
       total_revenue = df["order_amount"].sum()
       revenue_contribution = (df["order_amount"] / total_revenue) * 100
       return category_revenue , revenue_per_city , monthly_trend ,  count_per_category , highest_paying_customer , average_order_by_city , number_of_orders_per_customer , revenue_contribution
       

    def run(self):

        print("=" * 60)
        print("        E-COMMERCE ANALYTICS REPORT")
        print("=" * 60)

        merged_df = self.extract()
        print("\n1. MERGED DATAFRAME")
        print(merged_df)

        cleaned_df = self.clean()
        print("\n2. CLEANED DATAFRAME")
        print(cleaned_df)

        transformed_df = self.transform()
        print("\n3. TRANSFORMED DATAFRAME")
        print(transformed_df)

        (
            category_revenue,
            revenue_per_city,
            monthly_trend,
            count_per_category,
            highest_paying_customer,
            average_order_by_city,
            number_of_orders_per_customer,
            revenue_contribution,
        ) = self.analyze()

        print("\n4. CATEGORY REVENUE")
        print(category_revenue)

        print("\n5. REVENUE PER CITY")
        print(revenue_per_city)

        print("\n6. MONTHLY REVENUE TREND")
        print(monthly_trend)

        print("\n7. RETURN COUNT PER CATEGORY")
        print(count_per_category)

        print("\n8. HIGHEST PAYING CUSTOMER (ROW INDEX)")
        print(highest_paying_customer)

        print("\n9. AVERAGE ORDER VALUE BY CITY")
        print(average_order_by_city)

        print("\n10. NUMBER OF ORDERS PER CUSTOMER")
        print(number_of_orders_per_customer)

        print("\n11. REVENUE CONTRIBUTION (%)")
        print(revenue_contribution)

        print("\n" + "=" * 60)
        print("          REPORT GENERATED SUCCESSFULLY")
        print("=" * 60)       




ecp = EcommercePipeline(customers, products, orders)
ecp.run()