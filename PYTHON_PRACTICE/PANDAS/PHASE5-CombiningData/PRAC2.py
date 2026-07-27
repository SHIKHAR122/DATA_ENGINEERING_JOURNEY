# ============================================
# PANDAS PHASE 5 — Advanced Merge Practice
# Date: 24 July 2026
# Full Integration: merge, concat, OOP,
# exception handling, groupby, apply, lambda
# ============================================

import pandas as pd
import numpy as np

# ============================================
# QUESTION 6 — Real World: HR Analytics Pipeline
# A company has employee data spread across
# three separate HR systems that were never
# integrated. Your job is to build one clean
# unified employee view.

personal_data = pd.DataFrame({
    "emp_id": [1, 2, 3, 4, 5, 6],
    "name": ["Shikhar", "Rahul", "Priya",
             "Aditya", "Sneha", "Karan"],
    "age": [24, 28, 26, 30, 25, 27],
    "city": ["Delhi", "Mumbai", "Delhi",
             "Kanpur", "Mumbai", "Delhi"]
})

job_data = pd.DataFrame({
    "emp_id": [1, 2, 3, 4, 7],
    "department": ["Data", "IT", "Data", "HR", "Finance"],
    "designation": ["Analyst", "Developer",
                   "Engineer", "Manager", "Analyst"],
    "joining_year": [2022, 2020, 2021, 2019, 2023]
})

salary_data = pd.DataFrame({
    "emp_id": [1, 2, 3, 5, 6, 7],
    "salary": [90000, 60000, 85000,
               55000, 48000, 70000],
    "bonus": [10000, 5000, 8000, 4000, 3000, 6000]
})

# Build a class HRPipeline with:
# - Method build_unified_view() that:
#       merges all three tables using LEFT JOIN
#       from personal_data as the base
#       fills missing department with "Unassigned"
#       fills missing salary with overall median salary
#       fills missing bonus with 0
#       adds "total_compensation" = salary + bonus
# - Method department_summary() that returns
#   avg salary, total headcount, avg age per dept
#   using groupby + agg()
# - Method flag_incomplete_records() that returns
#   rows where any critical field is still missing
#   after the fill operations
# - Method experience_band() that adds a column:
#   "Senior" if joining_year <= 2020
#   "Mid" if joining_year <= 2022
#   "Junior" otherwise
#   handle NaN joining_year as "Unknown"
#   using apply() + lambda
# - Method run() that executes the full pipeline
#   and prints a formatted report

class HRpipeline:
    def __init__(self,personal_data , job_data , salary_data ):
        self.personal_data=personal_data
        self.job_data=job_data
        self.salary_data=salary_data
        
    def build_unified_view(self):
        df=pd.merge(self.personal_data,self.job_data , on='emp_id', how='left')
        df=pd.merge(df,self.salary_data,on='emp_id',how='left')
        df.fillna({"department":"Unassigned" , "designation":"Unassigned" , "salary":df["salary"].mean(),"bonus":0},inplace=True)
        df["total_compensation"]=df["salary"]+df["bonus"]
        return df

    def department_salary(self):
        df=self.build_unified_view()
        summary=df.groupby("department").agg({"salary":"mean" , "name":"count" ,  "age":"mean"})
        return summary

    def flag_incomplete_records(self):
        df=self.build_unified_view()
        for col in df.columns:
            if df[col].isna().sum()>0:
                df[col + "_missing"] = df[col].isna()
        return df

    def experience_band(self):
        exp_df=self.build_unified_view()
        exp_df["experience_tag"] = exp_df["joining_year"].apply(lambda year: "UNKNOWN"if pd.isna(year)else ( "SENIOR" if year <= 2020 else "MID" if year <= 2022 else "JUNIOR"))
        return exp_df


    def run(self):
        print("\n THE FINAL RESULT OF THE TABLE IS : \n",self.build_unified_view())
        print("\nTHE SUMMARY OF THE DATA IS :\n", self.department_salary())
        print("\nTHE MISSING DATA REPORT IS : \n",self.flag_incomplete_records())
        print("\nTHE EXPERIENCE REPORT   IS :  \n",self.experience_band())

hp=HRpipeline(personal_data , job_data , salary_data)
print(hp.run())


# ============================================

# QUESTION 7 — Real World: Sales Consolidation
# A retail chain has monthly sales files that
# need to be consolidated and analyzed.
# Some products appear in multiple months.

jan_sales = pd.DataFrame({
    "product_id": [101, 102, 103, 104],
    "product": ["Laptop", "Mouse", "Keyboard", "Monitor"],
    "units_sold": [5, 30, 15, 8],
    "revenue": [325000, 15000, 18000, 120000]
})

feb_sales = pd.DataFrame({
    "product_id": [101, 102, 105, 106],
    "product": ["Laptop", "Mouse", "Webcam", "Chair"],
    "units_sold": [3, 25, 12, 6],
    "revenue": [195000, 12500, 24000, 48000]
})

mar_sales = pd.DataFrame({
    "product_id": [103, 104, 105, 106],
    "product": ["Keyboard", "Monitor", "Webcam", "Chair"],
    "units_sold": [20, 10, 8, 4],
    "revenue": [24000, 150000, 16000, 32000]
})

product_info = pd.DataFrame({
    "product_id": [101, 102, 103, 104, 105, 106],
    "category": ["Electronics", "Electronics",
                "Accessories", "Electronics",
                "Accessories", "Furniture"],
    "supplier": ["TechCorp", "TechCorp", "OfficePro",
                "TechCorp", "OfficePro", "FurnitureCo"]
})

# Build a class SalesConsolidator with:
# - Method consolidate() that:
#       adds a "month" column to each DataFrame
#       before concatenating (Jan, Feb, Mar)
#       concatenates all three month DataFrames
#       resets index after concat
#       merges with product_info on product_id
# - Method monthly_summary() that returns
#   total revenue and units sold per month
# - Method category_performance() that returns
#   total revenue per category across all months
# - Method top_product_per_month() that returns
#   the highest revenue product for each month
#   using groupby + idxmax() pattern
# - Method run() that prints the full report

class SalesConsolidation :
    def __init__(self,jan_sales, feb_sales , mar_sales , product_info):
        self.jan_sales=jan_sales
        self.feb_sales=feb_sales
        self.mar_sales=mar_sales
        self.product_info=product_info

    def consolidate(self):
        self.jan_sales["month"] = "January"
        self.feb_sales["month"] = "February"
        self.mar_sales["month"] = "March"
        all_months=pd.concat([self.jan_sales , self.feb_sales, self.mar_sales], ignore_index=True)
        final_df= pd.merge(all_months , product_info , on="product_id" ,how='left')
        return final_df

    def monthly_summary(self):
        df=self.consolidate()
        return (df.groupby("month")[["revenue" , "units_sold"]].sum().reset_index())


    def category_performance(self):
        df1=self.consolidate()
        return(df1.groupby("category")[["revenue"]].sum().reset_index()) 


    def top_product_per_month(self):
        df = self.consolidate()
        idx=df.groupby("month")["revenue"].idxmax()
        return (df.loc[idx, ["month", "product", "revenue"]].reset_index(drop=True))


    
sc=SalesConsolidation(jan_sales, feb_sales, mar_sales,product_info)
print("\nTHE FINAL RESULT IS : \n", sc.consolidate())
print("\nTHE MONTHLY SUMMARY IS : \n" , sc.monthly_summary())
print("\nTHE CATEGORY PERFORMANCE IS : \n", sc.category_performance())
print("\nTHR TOP PRODUCTS PER MONTH IS : \n", sc.top_product_per_month())
# ============================================

# QUESTION 8 — HARDEST — Multi-source Data Pipeline
# You're a DA at a startup. Data comes from
# three different sources daily. Build a
# complete pipeline that merges, cleans,
# validates and analyzes it.

transactions = pd.DataFrame({
    "txn_id": [1, 2, 3, 4, 5, 6, 7, 8],
    "user_id": [101, 102, 101, 103, 104, 102, 105, 101],
    "product_id": [501, 502, 503, 501, 504, 502, 503, 504],
    "amount": [5000, np.nan, 3000, 8000, 2000, 4000, np.nan, 6000],
    "txn_date": ["2026-01-10", "2026-01-15", "2026-02-05",
                "2026-02-10", "2026-03-01", "2026-03-15",
                "2026-01-20", "2026-02-28"]
})

users = pd.DataFrame({
    "user_id": [101, 102, 103, 104],
    "username": ["shikhar", "rahul", "priya", "aditya"],
    "tier": ["Gold", "Silver", "Gold", "Bronze"]
})

products = pd.DataFrame({
    "product_id": [501, 502, 503, 504],
    "name": ["Laptop", "Mouse", "Keyboard", "Monitor"],
    "category": ["Electronics", "Electronics",
                "Accessories", "Electronics"],
    "unit_price": [65000, 500, 1200, 15000]
})

# Build a class StartupPipeline with:
# - Method extract_and_merge() that:
#       merges transactions with users (LEFT JOIN)
#       merges result with products (LEFT JOIN)
#       uses suffixes where needed
# - Method clean() that:
#       fills missing amount with category-wise median
#       flags rows where user info is missing
#       flags rows where product info is missing
# - Method transform() that:
#       converts txn_date to datetime
#       extracts month and year as separate columns
#       adds "effective_amount" = amount * tier_multiplier:
#       Gold = 1.1, Silver = 1.0, Bronze = 0.9
#       unknown tier = 1.0
#       use apply() + lambda for this
# - Method analyze() that returns:
#       total revenue per category (groupby)
#       total revenue per user tier (groupby)
#       monthly revenue trend (groupby by month)
# - Method run() that chains everything and
#       prints a complete startup analytics report



class StartupPieline:
    def __init__(self , transactions , users , products):
        self.transactions= transactions
        self.users=users
        self.products= products
    def extract_and_merge(self):
        final_df = pd.merge( self.transactions,  self.users, on="user_id", how="left")
        final_df = pd.merge(final_df, self.products,on="product_id",how="left")
        return final_df

    def clean(self):

        df = self.extract_and_merge()
        
        df["user_missing"] = df[["username", "tier"]].isnull().any(axis=1)
        df["product_missing"] = df[["name", "category", "unit_price"]].isnull().any(axis=1)
        df["amount"] = df["amount"].fillna(df.groupby("category")["amount"].transform("median"))
        df["username"] = df["username"].fillna("Unknown")
        df["tier"] = df["tier"].fillna("Unknown")
        df["name"] = df["name"].fillna("Unknown")
        df["category"] = df["category"].fillna("Unknown")

        return df


    def transform(self):
        df=self.extract_and_merge()
        df=self.clean()
        df["txn_date"]=pd.to_datetime(df["txn_date"])
        df["year"]=df["txn_date"].dt.year
        df["month"]=df["txn_date"].dt.month
        df["effective_amount"] = df.apply(lambda row: row["amount"] * (1.1 if row["tier"] == "Gold" else 1.0 if row["tier"] == "Silver"else 0.9 if row["tier"] == "Bronze"else 1.0),axis=1)
        return df
        


    def analyze(self):
        df = self.transform()
        category_revenue = (df.groupby("category")["effective_amount"].sum().reset_index())
        tier_revenue = (df.groupby("tier")["effective_amount"].sum().reset_index())
        monthly_revenue = (df.groupby("month")["effective_amount"].sum().reset_index())
        return category_revenue, tier_revenue, monthly_revenue
        



    def run(self):
        print("========== STARTUP ANALYTICS REPORT ==========\n")
        merged_df = self.extract_and_merge()
        print("Merged Data:")
        print(merged_df)

        clean_df = self.clean()
        print("\nCleaned Data:")
        print(clean_df)

        transformed_df = self.transform()
        print("\nTransformed Data:")
        print(transformed_df)

        category_revenue, tier_revenue, monthly_revenue = self.analyze()

        print("\nRevenue by Category")
        print(category_revenue)

        print("\nRevenue by Tier")
        print(tier_revenue)

        print("\nMonthly Revenue Trend")
        print(monthly_revenue)

        print("\n========== END OF REPORT ==========")



sp = StartupPieline(transactions, users, products)

sp.run()