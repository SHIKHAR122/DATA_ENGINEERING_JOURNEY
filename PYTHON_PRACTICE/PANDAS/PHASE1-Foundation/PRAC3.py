# ============================================
# PANDAS PRACTICE - OBJECT TYPE MASTERY
# Date: 21 June 2026
# Focus: DataFrame vs Series vs row vs value confusion
# ============================================

import pandas as pd

data = {
    "product": ["Laptop", "Mouse", "Keyboard", "Monitor", "Webcam"],
    "price": [65000, 500, 1200, 15000, 2000],
    "quantity": [2, 15, 8, 3, 6],
    "category": ["Electronics", "Electronics", "Electronics", "Electronics", "Electronics"]
}
df = pd.DataFrame(data)

# QUESTION 1 - Type Identification Drill
# For EACH line below, BEFORE running it, write a comment
# predicting the exact type (DataFrame, Series, str, int, etc).
# THEN run print(type(...)) to verify. If wrong, write WHY.
#
# a) df["price"]
# b) df[["price"]]
# c) df.loc[0]
# d) df.loc[[0]]
# e) df.iloc[0]["price"]
# f) df.iloc[0:2]
# g) df["price"].iloc[0]
# h) df.columns
# i) df.shape
# j) df["category"].value_counts()
# k) df.apply(lambda row: row["price"], axis=1)
# l) df["price"].apply(lambda x: x*2)

# YOUR CODE HERE — write prediction, then verify, for all 12:

# a) Series
print(type(df["price"]))

# b) DataFrame
print(type(df[["price"]]))

# c) Series
print(type(df.loc[0]))

# d) DataFrame
print(type(df.loc[[0]]))

# e) numpy.int64 (or int depending on version)
print(type(df.iloc[0]["price"]))

# f) DataFrame
print(type(df.iloc[0:2]))

# g) numpy.int64 (or int depending on version)
print(type(df["price"].iloc[0]))

# h) pandas.core.indexes.base.Index
print(type(df.columns))

# i) tuple
print(type(df.shape))

# j) Series
print(type(df["category"].value_counts()))

# k) Series
print(type(df.apply(lambda row: row["price"], axis=1)))

# l) Series
print(type(df["price"].apply(lambda x: x*2)))
# ============================================

# QUESTION 2 - Series vs DataFrame Operations
# Write a function inspect_object(obj) that:
# - Takes ANY object (Series, DataFrame, or single value)
# - Prints its type
# - If DataFrame: prints shape and columns
# - If Series: prints the Series name and length
# - Otherwise: prints "Single value: " + str(obj)
#
# Test it with all 12 expressions from Question 1.
# This forces you to handle each type correctly.

# YOUR CODE HERE:
def inspect_obj(obj):
    print("TYPE IS : ", type(obj))
    if isinstance(obj,df.DataFrame):
        print("SHAPE IS : ",obj.shape())
        print("COLUMNS ARE : ", list(obj.columns))
    elif isinstance(obj,df.Series):
        print("THE NAME OF THE SERIES IS : ",obj.name)
        print("THE LENGTH OF THE SERIES IS : ",len(obj))
    else:
        print("SINGLE VALUE: ",str(obj))


# ============================================

# QUESTION 3 - apply() Row vs Column Confusion — Direct Test
# Using the df above:
#
# - Write get_total_column(col) that takes a Series
#   (a single column) and returns its sum
#   Call it like: get_total_column(df["price"])
#
# - Write get_total_row(row) that takes a row (Series from
#   axis=1 apply) and returns price * quantity for that row
#   Call it using: df.apply(get_total_row, axis=1)
#
# - Explain in a comment: when you do df.apply(func, axis=1),
#   what type is "row" inside func? What can you do with it?
#
# - Explain in a comment: when you do df["price"].apply(func),
#   what type is the value passed into func? What can you do with it?

# YOUR CODE HERE:
def get_total_columns(col):
    return col.sum()

print(get_total_columns(df["price"]))

def get_total_rows(row):
    return row["price"]*row["quantity"]    

df["revenue"] = df.apply(get_total_rows, axis=1)
print(df["revenue"])
# ============================================

# QUESTION 4 - HARDEST — Full Object-Aware Pipeline
# Create a class InventoryAuditor with:
# - Attribute: df
# - Method get_column(col_name) that:
#       returns df[col_name] — explicitly comment what type this is
# - Method get_row(index) that:
#       returns df.loc[index] — explicitly comment what type this is
# - Method get_single_value(index, col_name) that:
#       returns df.loc[index, col_name] — comment the type
# - Method total_inventory_value() that:
#       must correctly identify that price and quantity
#       are Series, multiply them (Series * Series = Series),
#       then call .sum() to get a single number
#       comment what type exists at EACH step
# - Method low_stock_products(threshold) that:
#       returns a DataFrame (not Series!) of products
#       where quantity < threshold
#       use df[df["quantity"] < threshold] — comment why
#       this returns a DataFrame not a Series
#
# Create an InventoryAuditor with the df above.
# Call every method and print results.
# For EACH method, add a comment confirming the actual
# type returned using type(result).

# YOUR CODE HERE:

class InventoryAuditor:
    def __init__(self,df):
        self.df=df

    def get_column(self,col_name):
        return self.df[col_name]
    
    def get_rows(self,index):
        return self.df.loc[index]

    def get_single_value(self,index,col_name):
        return self.df.loc[index,col_name]

    def total_inventory_value(self):
        price=self.df["price"]
        quantity=self.df["quantity"]
        inventory_value=price*quantity
        total_value=inventory_value.sum()
        return total_value

    def low_stock_products(self,threshold):
        return self.df[self.df["quantity"]<threshold]
        