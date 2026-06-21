# ============================================
# CASE STUDY — Phase 1 Foundations Only
# Date: 21 June 2026
# ============================================

import pandas as pd

inventory_data = {
    "item_id": [1, 2, 3, 4, 5, 6, 7, 8],
    "item_name": ["Laptop", "Mouse", "Keyboard", "Monitor",
                  "Webcam", "Chair", "Desk", "Headphones"],
    "category": ["Electronics", "Electronics", "Electronics",
                "Electronics", "Electronics", "Furniture",
                "Furniture", "Electronics"],
    "price": [65000, 500, 1200, 15000, 2000, 8000, 12000, 3000],
    "stock": [5, 50, 30, 8, 12, 3, 2, 20]
}

df = pd.DataFrame(inventory_data)

# YOUR TASK:
#
# A warehouse manager wants a quick report on this inventory.
# Using ONLY foundational Pandas operations — head(), tail(),
# shape, info(), describe(), dtypes, loc[], iloc[], and
# selecting columns — answer the following:
#
# 1. Show the first 3 items in the inventory
# 2. Show the last 2 items
# 3. How many rows and columns does this inventory have?
# 4. What are the data types of each column?
# 5. Show only the "item_name" and "price" columns
# 6. Show full details of the item at index 4 using loc[]
# 7. Show full details of the item at position 4 using iloc[]
# 8. Show items at index 2 through 5 (inclusive) using loc[]
# 9. Get the statistical summary (describe()) of numeric columns
# 10. Print a one-line manual summary like this format:
#     "Total items: X | Average price: Y | Total stock units: Z"
#     (calculate average price and total stock manually,
#      not using describe())
#
# Write your code for all 10 tasks. No filtering required.

# YOUR CODE HERE:


print("THE FIRST THREE ITEMS IN THE INVENTORY ARE:\n",df.head(3))
print("THE LAST 2 ITEMS IN THE INVENTORY ARE : \n", df.tail(2))
print("THE NUMBER OF ROWS AND COLUMNS IN THE INVENTORY ARE : ", df.shape)
print("THE DATA ITEMS OF EACH COLUMNS ARE : \n",df.dtypes)
print("THE ITEM NAME AND THE PRICES ARE: \n", df[["item_name" , "price"]])
print("\n THE DETAILS OF THE ITEM AT INDEX 4 IS : ",df.loc[4])
print("\n THE DETAILS OF THE ITEMS FROM INDEX 2 TO 5 ARE:\n",df.iloc[2:6])
print("\nTHE STATISTICAL SUMMARY OF THE NUMERIC COLUMNS ARE :\n")
numeric_data=df.select_dtypes(include='number')
print(numeric_data.describe())

total_items=df["item_name"].nunique()
print("SUMMARY OF THE WHOLE DATA FRAME IS :")
avg_price= sum(df["price"])/len(df["price"])
total_stocks= sum(df["stock"])
print("TOTAL ITEMS : {} | TOTAL PRICE : {} | TOTAL STOCKS : {}".format(total_items , avg_price , total_stocks))