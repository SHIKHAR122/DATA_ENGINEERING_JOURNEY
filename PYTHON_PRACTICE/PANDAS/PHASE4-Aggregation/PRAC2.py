# ============================================
# PHASE 4 FINAL — Sales Intelligence Report
# Date: 16 July 2026
# ============================================

import pandas as pd
import numpy as np
sales_data = {
    "sale_id": [1,2,3,4,5,6,7,8,9,10,11,12],
    "salesperson": ["Shikhar","Rahul","Shikhar","Priya",
                   "Rahul","Priya","Shikhar","Aditya",
                   "Priya","Aditya","Rahul","Shikhar"],
    "region": ["North","South","North","East",
               "South","East","North","West",
               "East","West","South","North"],
    "product_category": ["Electronics","Clothing","Electronics",
                        "Food","Clothing","Electronics","Food",
                        "Electronics","Clothing","Food",
                        "Electronics","Clothing"],
    "units_sold": [5, 3, np.nan, 8, 2, 6, np.nan, 4, 7, 3, 5, 2],
    "unit_price": [15000, 800, 15000, 200, 800, 15000,
                  200, 15000, 800, 200, 800, 800],
    "quarter": ["Q1","Q1","Q2","Q1","Q2","Q2",
               "Q1","Q2","Q1","Q2","Q1","Q2"]
}

# Build a class SalesIntelligence with:
#
# - Method clean() that fills missing units_sold
#   with the median units_sold for that product_category
#
# - Method add_revenue() that adds a revenue column
#   (units_sold * unit_price) and a performance_tier
#   using apply():
#   "Star" if revenue >= 50000
#   "Good" if revenue >= 10000
#   "Average" otherwise
#
# - Method regional_summary() that uses agg() to return
#   for each region: total revenue, average units sold,
#   count of sales transactions
#
# - Method salesperson_pivot() that creates a pivot table
#   showing total revenue per salesperson (rows)
#   vs product_category (columns)
#
# - Method quarter_crosstab() that creates a crosstab
#   of quarter vs region showing transaction counts,
#   with normalize="index" so each row shows
#   what % of that quarter's sales came from each region
#
# - Method top_salesperson() that returns the salesperson
#   with the highest total revenue using groupby + idxmax()
#
# - Method performance_distribution() that returns
#   value_counts() of performance_tier as percentages
#
# YOUR CODE HERE:

df= pd.DataFrame(sales_data)
class SalesIntelligence :
    def __init__(self,df):
        self.df=df
    
    def clean(self):
        self.df["units_sold"]=self.df["units_sold"].fillna(self.df.groupby("product_category")["units_sold"].transform("median"))
        return self.df
    
    def add_revenue(self):
        self.df["revenue"]=self.df["units_sold"]*self.df["unit_price"]
        self.df["revenue_tier"]=self.df["revenue"].apply(lambda revenue: "STAR" if revenue>=50000 else "GOOD" if revenue >=10000 else "AVERAGE" )
        return self.df
    

    def regional_summary(self):
        regional_summary=self.df.groupby("region").agg({
            "revenue" : "sum" , 
            "units_sold":"mean",
            "sale_id":"count"
        })
        return regional_summary
    
    def salespersonpivot(self):
       t1= pd.pivot_table(self.df,index="salesperson" , columns="product_category" , values="revenue")
       return t1
    

    def quarter_crosstab(self):
        ctab=pd.crosstab(self.df["quarter"] , self.df["region"] , normalize="index")
        return ctab
    
    def top_salesperson(self):
       return self.df.groupby("salesperson")["revenue"].sum().idxmax()
    

    def performance_distribution(self):
        performance_count=self.df["revenue_tier"].value_counts(normalize=True)
        return performance_count
        
        

si=SalesIntelligence(df)
print(si.clean())
print("\nTHE DATA FRAME WITH REVENUE AND TIER LIST IS:  :\n" , si.add_revenue())
print("\n THE REGIONAL SUMMARY IS : \n" , si.regional_summary())
print("\nTHE PIVOT TABLE FOR EACH SALES REVENUE OF SALESPERSON : \n" , si.salespersonpivot())
print("\n THE CROSS TABLE IS :\n" ,si.quarter_crosstab())
print("THE EMPLOYEE WITH THE TOP  SALES IS : " , si.top_salesperson())
print("\nTHE PERFORMANCE DISTRIBUTION IS : \n",si.performance_distribution())
