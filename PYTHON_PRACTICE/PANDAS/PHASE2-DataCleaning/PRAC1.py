# ============================================
# PANDAS PHASE 2 — Data Cleaning
# Date: 25 June 2026
# Topics: isnull, dropna, fillna, duplicated,
# drop_duplicates, rename, astype, .str operations, replace
# Integrated with: OOP, Exception Handling, Lambda, apply()
# ============================================

import pandas as pd
import numpy as np

# ============================================
# SECTION A — Detailed Practice (5 Questions)
# ============================================

# QUESTION A1 - Null Handling Basics
data = {
    "name": ["Shikhar", "Rahul", None, "Priya", "Aditya", None],
    "age": [21, np.nan, 25, 22, np.nan, 28],
    "marks": [95, 60, 89, np.nan, 75, 40]
}
df = pd.DataFrame(data)

# - Check which cells are null using isnull()
# - Count total nulls per column
# - Count total nulls in the entire DataFrame
# - Drop rows where "name" is null using dropna(subset=...)
# - Fill null "age" values with the mean age
# - Fill null "marks" values with 0
# - Print the cleaned DataFrame at the end

# YOUR CODE HERE:

print(df.isnull())

print("\n THE TOTAL NUMBER OF NULLS PER COLUMN  ARE: \n",df.isnull().sum())

print("\n THE TOTAL NUMBER OF NULLS IN THE WHOLE DATA FRAME   ARE: \n",df.isnull().sum().sum())

dff_new=df.dropna(subset=["name"])
print(dff_new)

df["age"]=df["age"].fillna(df["age"].mean())


df["marks"]=df["marks"].fillna(0)

print(df)
#  ============================================

# QUESTION A2 - Duplicates
data2 = {
    "order_id": [1, 2, 3, 2, 4, 3, 5],
    "product": ["Laptop", "Mouse", "Keyboard",
                "Mouse", "Monitor", "Keyboard", "Webcam"],
    "price": [65000, 500, 1200, 500, 15000, 1200, 2000]
}
df2 = pd.DataFrame(data2)

# - Check for duplicate rows using duplicated()
# - Count how many duplicate rows exist
# - Drop duplicates keeping the FIRST occurrence
# - Drop duplicates keeping the LAST occurrence
#   (do this on a fresh copy, don't overwrite the first result)
# - Check for duplicates based only on "order_id" column
#   using duplicated(subset=...)

# YOUR CODE HERE:

print(df2.duplicated())
print(df2.duplicated().sum())

print(df2.drop_duplicates(keep='first'))
print(df2.drop_duplicates(keep='last'))
print(df2.duplicated(subset=["order_id"]))

# ============================================

# QUESTION A3 - Renaming and Type Conversion
data3 = {
    "Emp ID": [1, 2, 3, 4],
    "Emp Name": ["Shikhar", "Rahul", "Priya", "Aditya"],
    "sal": ["90000", "45000", "78000", "60000"]
}
df3 = pd.DataFrame(data3)

# - Rename columns to: emp_id, emp_name, salary
#   using rename() with a dictionary
# - Check dtypes — notice "salary" is string
# - Convert "salary" to integer using astype()
# - Rename "emp_id" to "id" using rename() again
# - Print final DataFrame with dtypes confirmed

# YOUR CODE HERE:
df3.rename(columns={
    "Emp ID": "emp_id",
    "Emp Name": "emp_name",
    "sal":"salary"
},inplace=True)

df3["salary"]=df3["salary"].astype(int)
df3.rename(columns={"emp_id":"id"})
print(df3)
print(df3.dtypes)
# ============================================

# QUESTION A4 - String Operations
data4 = {
    "name": ["  shikhar  ", "RAHUL", "Priya  ", "  aditya"],
    "email": ["shikhar@GMAIL.com", "rahul@yahoo.COM",
              "priya@gmail.com", "aditya@OUTLOOK.com"],
    "city": ["new delhi", "MUMBAI", "Bangalore ", " kanpur"]
}
df4 = pd.DataFrame(data4)

# - Strip whitespace from "name" and "city" using .str.strip()
# - Convert "name" to title case using .str.title()
# - Convert "email" to lowercase using .str.lower()
# - Check which emails contain "gmail" using .str.contains()
# - Create a new column "email_domain" by splitting email
#   on "@" and taking the second part
#   hint: .str.split("@").str[1]

# YOUR CODE HERE:
df4[["name","city"]]=df4[["name","city"]].apply(lambda col : col.str.strip())
df4["email"]=df4["email"].str.lower()
df4["name"] = df4["name"].str.title()
df4["email"].str.contains("gmail", na=False)
df4["email_domain"]=df4["email"].str.strip("@").str[1]
print(df4)
# ============================================

# QUESTION A5 - Replace Values + Combined Cleaning
data5 = {
    "status": ["active", "Active", "INACTIVE", "inactive",
              "ACTIVE", "Pending", "pending"],
    "department": ["IT", "it", "HR", "Hr", "FINANCE",
                   "Finance", "IT"]
}
df5 = pd.DataFrame(data5)

# - Standardize "status" column: convert everything to
#   lowercase first using .str.lower(), then replace
#   using replace() to map:
#   "active" -> "Active", "inactive" -> "Inactive",
#   "pending" -> "Pending"
# - Standardize "department" similarly — lowercase first,
#   then use replace() to map "it"->"IT", "hr"->"HR",
#   "finance"->"Finance"
# - Print value_counts() for both columns after cleaning
#   to confirm there's only one variant of each value left

# YOUR CODE HERE:
df5["status"]=df5["status"].str.lower()


df5["status"]=df5["status"].replace({
    "active":"Active",
    "inactive":"Inactive",
    "pending":"Pending"
})


df5["department"]=df5["department"].str.lower()


df5["department"]=df5["department"].replace({
    "it":"IT",
    "hr":"HR",
    "finance":"Finance"
})
print(df5)


