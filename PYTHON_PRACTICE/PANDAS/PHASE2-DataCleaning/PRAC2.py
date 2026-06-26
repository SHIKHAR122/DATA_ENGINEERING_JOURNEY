# ============================================
# SECTION B — Real Interview Style Problems (5 Questions)
# ============================================
import pandas as pd 
import numpy as np
# QUESTION B1 — Asked in DA Internship Interviews
# "Here's a customer dataset. Clean it and tell me how
#  many genuinely usable records remain."
    # Build this class yourself:
    # - Method clean() that:
    #     removes rows with null customer_name
    #     removes exact duplicate rows
    #     strips whitespace from customer_name and email
    #     standardizes email to lowercase
    #     returns the cleaned df
    # - Method usable_count() that:
    #     returns count of rows after clean() has run
    #     raises ValueError if clean() hasn't been called yet
    #     (hint: track this with a flag attribute)

raw_customers = {
    "customer_name": ["Shikhar", "  Rahul", None, "Priya  ",
                      "Shikhar", "Aditya", "  ", "Sneha"],
    "email": ["Shikhar@Gmail.com", "rahul@yahoo.com", "x@x.com",
             "PRIYA@gmail.com", "Shikhar@Gmail.com",
             "aditya@outlook.com", "y@y.com", "sneha@gmail.com"]
}

# Create CustomerDataCleaner, call clean(), call usable_count().
# Try calling usable_count() on a NEW object before clean()
# — should raise ValueError.

# YOUR CODE HERE:
df=pd.DataFrame(raw_customers)
class CustomerDataCleaner:
    def __init__(self, data):
        self.df = pd.DataFrame(data)

    def clean(self):
        self.df.dropna(inplace=True)
        self.df.drop_duplicates(inplace=True)
        self.df = self.df[self.df["customer_name"].str.strip() != ""]
        self.df["customer_name"]=self.df["customer_name"].str.strip()
        self.df["email"]=self.df["email"].str.lower()
        return self.df
              
    def usable_count(self):
        return len(self.df)
cd=CustomerDataCleaner(df)
print(cd.clean())
print("THE COUNT OF THE CLEAN ROWS ARE :",cd.usable_count())

# ============================================

# QUESTION B2 — Asked in DA Internship Interviews
# "We suspect our sales data has inconsistent product names
#  due to manual entry. Standardize them and recalculate
#  total revenue per actual product."
sales_raw = {
    "product": ["laptop", "Laptop", "LAPTOP ", " laptop",
               "mouse", "Mouse", "keyboard", "Keyboard "],
    "quantity": [2, 1, 3, 1, 10, 5, 8, 4],
    "price": [65000, 65000, 65000, 65000,
             500, 500, 1200, 1200]
}

# Using string operations (.str.strip(), .str.lower(),
# .str.title()) to standardize "product" names BEFORE
# grouping — then use groupby (you've used this conceptually
# before via aggregation, now apply it formally):
#
# df.groupby("product")["quantity"].sum() type pattern
#
# - Standardize product names so "laptop", "Laptop ",
#   " laptop" all become one consistent value
# - Calculate revenue column (price * quantity)
# - Calculate total revenue PER cleaned product name
# - Print which product generated the most revenue

# YOUR CODE HERE:

# ============================================

# QUESTION B3 — Asked in DA Internship Interviews
# "This employee dataset has missing salary values for
#  some departments. Don't just drop them — fill them
#  intelligently."
employees_raw = {
    "name": ["Shikhar", "Rahul", "Priya", "Aditya",
            "Sneha", "Karan", "Meera"],
    "department": ["Data", "IT", "Data", "IT",
                   "Data", "HR", "HR"],
    "salary": [90000, np.nan, 95000, 60000,
              np.nan, 45000, np.nan]
}

# - Fill missing salary with the AVERAGE salary of that
#   employee's OWN department, not the overall average
#   hint: groupby("department")["salary"].transform("mean")
#   this is a real technique used constantly in DE/DA work
# - Print the DataFrame before and after filling
# - Explain in a comment why this is better than filling
#   with the overall mean salary

# YOUR CODE HERE:


# ============================================

# QUESTION B4 — Asked in DA Internship Interviews
# "Some user signups have duplicate accounts with slightly
#  different email casing. Identify and remove the true
#  duplicates."
signups = {
    "user_id": [1, 2, 3, 4, 5, 6],
    "name": ["Shikhar", "Rahul", "Shikhar", "Priya",
            "RAHUL", "Aditya"],
    "email": ["shikhar@gmail.com", "rahul@yahoo.com",
             "SHIKHAR@GMAIL.COM", "priya@gmail.com",
             "rahul@YAHOO.com", "aditya@outlook.com"]
}

# - Standardize email to lowercase first
# - Now check for duplicates based on the standardized email
#   using duplicated(subset=...)
# - Drop these duplicates keeping the first occurrence
# - Print how many true duplicate accounts were found
# - Print the final cleaned signups DataFrame

# YOUR CODE HERE:


# ============================================

# QUESTION B5 — HARDEST — Full Real World Scenario
# "You're given a raw feedback form export. It's messy in
#  every way real data is messy. Clean it completely and
#  give us a usable dataset plus a summary of what you fixed."
feedback_raw = {
    "respondent": ["Shikhar", "  rahul", "PRIYA", None,
                  "Shikhar", "aditya  ", "sneha", " "],
    "rating": [5, 3, np.nan, 4, 5, 2, np.nan, 1],
    "comment": ["Great service", "ok", "GOOD", "Bad",
               "Great service", "could be better",
               "excellent", "terrible"],
    "department_visited": ["sales", "Sales", "SUPPORT",
                           "support ", "sales", "Billing",
                           " billing", "Support"]
}

# Build a class FeedbackCleaner with:
# - Method clean() that handles ALL of these issues:
#     1. Remove rows with null or blank respondent
#     2. Standardize respondent name (strip + title case)
#     3. Fill missing rating with the median rating
#     4. Standardize department_visited (strip + title case)
#     5. Remove exact duplicate rows (same respondent +
#        same comment)
# - Method summary() that prints:
#     total rows before cleaning
#     total rows after cleaning
#     how many nulls were fixed
#     how many duplicates were removed
#     average rating after cleaning
#
# Create object, call clean(), call summary().

# YOUR CODE HERE: