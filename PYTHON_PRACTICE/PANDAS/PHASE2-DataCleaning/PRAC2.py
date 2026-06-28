# ============================================
# PANDAS — PHASE 1 + 2 INTERVIEW STYLE
# Date: 28 June 2026
# ============================================

import pandas as pd
import numpy as np

# ------------------------------------------------
# QUESTION 1
# A college sends you a CSV-style admissions dataset
# (already loaded as a dict below). Several students have
# applied more than once due to a form glitch, and a few
# entries are missing their score. The admissions head
# wants one clean record per student and no missing scores
# left unresolved.

admissions = {
    "applicant_id": [1, 2, 3, 2, 4, 5, 3, 6],
    "name": ["Shikhar", "Rahul", "Priya", "Rahul",
            "Aditya", "Sneha", "Priya", "Karan"],
    "score": [88, np.nan, 76, 91, 65, np.nan, 76, 82]
}

# Build a class AdmissionsCleaner that takes this data,
# produces one clean record per applicant_id, and fills
# any remaining missing scores with the overall average
# score. Add a method that reports how many duplicate
# applications were found and removed.


df=pd.DataFrame(admissions)
class AdmissionCleaner:
    def __init__(self,df):
        self.df=df
        self.duplicated_rows=0
    def cleaner(self):
        self.duplicated_rows=self.df.duplicated(subset="applicant_id").sum()
        self.df = self.df.sort_values(by="score",na_position="last")
        self.df=self.df.drop_duplicates(subset="applicant_id",keep="first")
        overall_avg = self.df["score"].mean()
        self.df["score"] = self.df["score"].fillna(overall_avg)
        return self.df
    

    def summary_data(self):
        return self.duplicated_rows

ac=AdmissionCleaner(df)
print(ac.cleaner())
print("THE TOTAL NUMBER OF ROWS REMOVED ARE :", ac.summary_data())
# ------------------------------------------------
# QUESTION 2
# An HR system exports employee names inconsistently —
# some have extra spaces, some are in different cases,
# and the department field has typos in casing too.
# You're asked to standardize this before it gets loaded
# into the company directory tool.

employees = {
    "emp_name": ["  shikhar sharma", "RAHUL VERMA  ",
                "Priya Singh", "  aditya kumar"],
    "dept": ["data", "DATA", "Engineering", "engineering "],
    "Emp Salary": ["72000", "55000", "88000", "61000"]
}

# Clean this dataset so names are properly capitalized
# with no extra whitespace, departments are consistent,
# the salary column has a sensible name and is usable
# for numeric calculations, not stored as text.
df2=pd.DataFrame(employees)
class CompanyTool:
    def __init__(self, df2):
        self.df2 = df2

    def clean(self):
        self.df2["emp_name"] = self.df2["emp_name"].str.upper().str.strip()
        self.df2["dept"]=self.df2["dept"].str.upper().str.strip()
        self.df2 = self.df2.rename(columns={"Emp Salary": "salary"})
        self.df2["salary"] = self.df2["salary"].astype(int)
        return self.df2


ct = CompanyTool(df2)
print(ct.clean())

# ------------------------------------------------
# QUESTION 3
# A support ticketing system logs customer emails with
# wildly inconsistent casing, which is creating duplicate
# customer profiles. You're asked to find out exactly how
# many "customers" in this list are actually the same
# person re-logged under different email casing.

tickets = {
    "ticket_id": [101, 102, 103, 104, 105, 106],
    "customer_email": ["amit@gmail.com", "NEHA@yahoo.com",
                       "AMIT@GMAIL.com", "raj@outlook.com",
                       "neha@YAHOO.com", "raj@OUTLOOK.com"]
}

# Identify the true number of unique customers in this
# dataset and produce a clean version of the table with
# one row per actual customer.
df3=pd.DataFrame(tickets)
class ticketingsystem:
    def __init__(self, df3):
        self.df3=df3
    def transform(self):
        self.df3["customer_email"]=self.df3["customer_email"].str.lower().str.strip()
        self.df3.drop_duplicates(subset="customer_email", inplace=True)
        return self.df3
    def relogged(self):
        return self.df3["customer_email"].nunique()
ts = ticketingsystem(df3)

print(ts.transform())
print("Unique customers:", ts.relogged())
# ------------------------------------------------
# QUESTION 4
# A retail chain shares product feedback data collected
# from multiple store branches. The "rating" field has
# some missing entries, and the reviewer names have
# inconsistent formatting. Management wants a usable
# version of this data along with a short report of what
# was wrong with it originally.

reviews = {
    "reviewer": ["Shikhar", "  rahul", None, "PRIYA",
                "aditya  ", " ", "Sneha"],
    "rating": [4, np.nan, 5, np.nan, 3, 2, np.nan],
    "store": ["Kanpur", "kanpur", "Lucknow", "LUCKNOW",
             "Kanpur", "lucknow ", "Lucknow"]
}

# Build something that cleans this dataset properly,
# decides what to do with missing reviewers and missing
# ratings, standardizes the store names, and then tells
# you how many rows were unusable and had to be removed
# versus how many were fixable.
df4=pd.DataFrame(reviews)
class retail:
    def __init__(self,df4):
        self.df4=df4
        self.fixed=0
        self.removed=0
    def convert(self):
        self.df4["reviewer"]=self.df4["reviewer"].str.strip().str.upper()
        self.df4["store"]=self.df4["store"].str.strip().str.upper()
        self.fixed += self.df4["reviewer"].isna().sum()
        self.df4["reviewer"]=self.df4["reviewer"].replace({None:"N/A"})
        self.df4["reviewer"]=self.df4["reviewer"].replace({"":"N/A"})
        blank = self.df4["reviewer"] == ""
        self.fixed += blank.sum()
        self.df4.loc[blank, "reviewer"] = "N/A"
        self.fixed += self.df4["rating"].isna().sum()
        avg = self.df4["rating"].mean()
        self.df4["rating"] = self.df4["rating"].fillna(avg)
        return self.df4
        
    def summary(self):
        return self.fixed , self.removed
        


r=retail(df4)

print(r.convert())    
print(r.summary())
# ------------------------------------------------
# QUESTION 5 — Hardest in this set
# You're handed a raw signup export from a marketing
# campaign. It's genuinely messy — missing names, mixed
# casing everywhere, duplicate signups under slightly
# different email formatting, and a phone number column
# stored as text with inconsistent spacing.

signups = {
    "full_name": ["Shikhar Sharma", "  rahul verma",
                 None, "PRIYA SINGH  ", "Shikhar Sharma",
                 "aditya kumar", " "],
    "email": ["shikhar@gmail.com", "RAHUL@yahoo.com",
             "x@x.com", "priya@GMAIL.com",
             "SHIKHAR@gmail.com", "aditya@outlook.com",
             "y@y.com"],
    "phone": [" 9876543210", "9876543211 ", "9876543212",
             "9876543213 ", " 9876543210", "9876543214",
             "9876543215"]
}

# Produce a genuinely clean version of this signup list —
# one row per real person, properly formatted name, email
# and phone — and explain what made each removed row
# invalid or duplicate.