# ============================================
# PANDAS PRACTICE - PHASE 1 REINFORCEMENT
# Date: 20 June 2026
# Focus: apply(), select_dtypes(), describe(), sort_values()
# Integrated with: OOP, Exception Handling, Lambda
# ============================================

import pandas as pd

# QUESTION 1 - Logic Building with apply()
# Create this sales DataFrame:
data = {
    "product": ["Laptop", "Mouse", "Keyboard", "Monitor",
                "Webcam", "Headphones", "Chair", "Desk"],
    "price": [65000, 500, 1200, 15000, 2000, 3000, 8000, 12000],
    "quantity": [2, 15, 8, 3, 6, 4, 2, 1],
    "category": ["Electronics", "Electronics", "Electronics",
                "Electronics", "Electronics", "Electronics",
                "Furniture", "Furniture"]
}
df = pd.DataFrame(data)

# Using apply() + lambda:
# - Create "revenue" column = price * quantity
# - Create "price_tier" column:
#       "Premium" if price >= 10000
#       "Standard" if price >= 1000
#       "Budget" otherwise
# - Create "discount" column using apply() on the WHOLE ROW
#   (not just one column) — use axis=1:
#       if category is "Electronics": discount = price * 0.1
#       if category is "Furniture": discount = price * 0.05
#   hint: def get_discount(row): return ... then
#         df.apply(get_discount, axis=1)
#
# Print the full DataFrame after adding all 3 columns.

# YOUR CODE HERE:
df["revenue"]=df.apply(lambda row : row["quantity"]*row["price"] , axis=1)

df["price_tier"]=df["price"].apply(lambda price : "Premium" if price>=10000 else "Standard" if price>=1000 else "Budget")

def get_discount(row):
    if row["category"]=="Electronics":
        return row["price"]*0.1
    elif row["category"]=="Furniture":
        return row["price"]*0.05
    

    return 0 

df["discount"]=df.apply(get_discount,1)
print(df)

# ============================================

# QUESTION 2 - select_dtypes() Logic Building
# Using the same DataFrame:
#
# - Select only numeric columns using select_dtypes(include='number')
# - Select only object/string columns using select_dtypes(include='object')
# - Calculate sum of ALL numeric columns at once
#   hint: numeric_df.sum()
# - Calculate mean of ALL numeric columns at once
# - Write a function count_column_types(df) that:
#       returns a dict like:
#       {"numeric": X, "object": Y}
#       counting how many columns of each type exist
#       use len(df.select_dtypes(include='number').columns)

# YOUR CODE HERE:

numeric_df = df.select_dtypes(include='number')
print("\nTHE NUMERIC DATA FRAMES ARE : \n",numeric_df)

string_df  = df.select_dtypes(include='object')
print("\nTHE STRING DATA FRAMES ARE : \n",string_df)

numeric_sum=numeric_df.sum()
print("THE SUM OF THE NUMERIC DATA FRAMES ARE : \n" , numeric_sum)

mean = numeric_df.mean()
print("\nTHE MEAN OF THE NUMERIC COLUMNS IS:\n", mean)
def count_column_types(df):
    count_numbers = len(df.select_dtypes(include='number').columns)
    count_objects = len(df.select_dtypes(include='object').columns)
    return {
        "numeric": count_numbers,
        "object": count_objects
    }
print(count_column_types(df))


# ============================================

# QUESTION 3 - describe() Deep Dive
# Using the same DataFrame:
#
# - Run describe() on the full DataFrame — observe what
#   happens to non-numeric columns
# - Run describe() with include='all' — observe the difference
# - Run describe() only on the "price" column
# - Manually extract specific stats WITHOUT describe():
#       mean, median, std, min, max of "price" column
#       using df["price"].mean(), .median(), .std() etc
# - Compare your manual values to what describe() showed —
#   write a comment confirming they match

# YOUR CODE HERE:
print("\nTHE DESCRIPTION IS : \n",df.describe())
print(df.describe(include='all'))
print(df["price"].describe())
print("THE MEAN OF THE PRICES ARE: ",df["price"].mean())
print("THE MEDIAN OF THE PRICES ARE : ",df["price"].median())
print("THE STANDARD DEVIATION OF THE PRICES ARE : ",df["price"].std())
#  YES THE VALUES OF MANUALLY EXTRACTED MEAN, MEDIAN AND SD IS  MATCHING WITH THE MEAN , MEDIAN AND STD OF THE DESCRIPTION()
# ============================================

# QUESTION 4 - HARDEST — Combining Everything
# Create a class ProductAnalyzer with:
# - Attribute: df
# - Method add_computed_columns() that:
#       uses apply() to add "revenue" and "price_tier"
#       (same logic as Question 1)
# - Method get_numeric_summary() that:
#       raises ValueError if df is empty
#       uses select_dtypes() to get numeric columns only
#       returns their describe() output
# - Method top_revenue_products(n) that:
#       uses sort_values() to sort by "revenue" descending
#       returns top n rows with only
#       ["product", "revenue", "price_tier"] columns
# - Method category_breakdown() that:
#       uses select_dtypes(include='object') to find
#       string columns
#       prints value_counts() for each string column found
#       hint: loop through those column names
#
# Create a ProductAnalyzer with the sales DataFrame.
# Call add_computed_columns().
# Call get_numeric_summary() and print it.
# Call top_revenue_products(3) and print it.
# Call category_breakdown().
#
# Now create an analyzer with an EMPTY DataFrame
# (pd.DataFrame()) and call get_numeric_summary()
# — should raise ValueError correctly.

# YOUR CODE HERE:

import pandas as pd

class ProductAnalyzer:
    def __init__(self,df):
        self.df=df

    def add_computed_columns(self):
        self.df["revenue"]=self.df.apply(lambda row: row["price"]*row["quantity"],axis=1)
        self.df["price_tier"]=self.df["price"].apply(lambda price:"Premium" if price>=1000 else "Standard" if price>=1000 else "Budget")
        return self.df

    def get_numeric_summary(self):
        if self.df.empty:
            raise ValueError("DATA FRAME IS EMPTY")
        numeric_df=self.df.select_dtypes(include="number")
        return numeric_df.describe()


    def top_revenue_products(self,n):
        return self.df.sort_values(by="revenue",ascending=False)[["product","revenue","price_tier"]].head(n)

    def category_breakdown(self):
        object_df=self.df.select_dtypes(include="object")
        for column in object_df.columns:
            print(f"\n{column.upper()} BREAKDOWN:\n")
            print(self.df[column].value_counts())



analyzer=ProductAnalyzer(df)

analyzer.add_computed_columns()

print("\nNUMERIC SUMMARY:\n")
print(analyzer.get_numeric_summary())

print("\nTOP REVENUE PRODUCTS:\n")
print(analyzer.top_revenue_products(3))

print("\nCATEGORY BREAKDOWN:")
analyzer.category_breakdown()


empty_analyzer=ProductAnalyzer(pd.DataFrame())

try:
    print(empty_analyzer.get_numeric_summary())
except ValueError as e:
    print("\nERROR:",e)