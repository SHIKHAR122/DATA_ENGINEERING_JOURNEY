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
df3-
class Ecommerce:
    def __init__(self, df3):