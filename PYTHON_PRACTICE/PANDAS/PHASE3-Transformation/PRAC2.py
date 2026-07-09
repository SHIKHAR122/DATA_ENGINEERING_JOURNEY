# ============================================
# QUESTION — E-Commerce Monthly Report
# Date: 8 July 2026
# ============================================

import pandas as pd
import numpy as np

transactions = {
    "txn_id": [1, 2, 3, 4, 5, 6, 7, 8, 9, 3],
    "customer": ["shikhar", "RAHUL", "priya  ", "  ADITYA",
                "sneha", "RAHUL", "karan  ", "Meera",
                "shikhar", "priya  "],
    "category": ["Electronics", "clothing", "Electronics",
                "CLOTHING", "food", "Clothing", "FOOD",
                "electronics", "Food", "Electronics"],
    "amount": [5000, np.nan, 3200, 1500, 800,
              2200, np.nan, 4100, 600, 3200]
}

# Build a class EcommerceReport with:
# - Method clean() that removes duplicate txn_ids,
#   standardizes customer and category columns,
#   fills missing amount with category-wise median
# - Method category_summary() that returns total amount
#   and transaction count per category using groupby + agg
# - Method customer_summary() that returns total spend
#   per customer sorted descending
# - Method spending_tier() that adds a tier column:
#   "Premium" if amount >= 3000
#   "Regular" if amount >= 1000
#   "Budget" otherwise
#   then returns value_counts() of the tier column
# - Method run() that calls all methods in order
#   and prints a clean final report

# YOUR CODE HERE:
df=pd.DataFrame(transactions)
class Ecommerce:
    def __init__(self, df):    
        self.df=df
    

    def clean(self):
        self.df.drop_duplicates(subset=["txn_id"] ,inplace=True)
        l=["customer" , "category"]
        for col in l :
             self.df[col]=self.df[col].apply(lambda x: x.strip().title())
        self.df["amount"]=self.df["amount"].fillna(self.df.groupby("category")["amount"].transform("median"))
        return self.df
    
    def category_summary(self):
        total_amount= self.df.groupby("category")["amount"].sum()
        transaction_count = self.df.groupby("category").size()
        return total_amount , transaction_count
    
    def customer_summary(self):
        print(" \n THE TOTAL AMOUNT SPENT BY CUSTOMERS ARE : \n")
        return self.df.groupby("customer")["amount"].sum().sort_values(ascending=False)
        
    def spending_tier(self):
        self.df["tier"]= self.df["amount"].apply(lambda amount : "Premium" if amount>=3000 else "Regular" if amount>=1000 else "Budget")
        return self.df
    
    def run(self):
        
        print(self.clean())
        print(self.customer_summary())
        print(self.category_summary())



e=Ecommerce(df)
e.run()


