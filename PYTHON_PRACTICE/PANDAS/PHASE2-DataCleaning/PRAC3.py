"""
===========================
PANDAS DATA CLEANING CHALLENGE
===========================

Objective:
Clean and preprocess the given employee dataset using Pandas.

Instructions:
- Write clean, readable code.
- Do NOT modify the dataset manually.
- Use appropriate Pandas functions.
- Print the output wherever required.
"""

import pandas as pd
import numpy as np

# ==========================
# Dataset
# ==========================

employees = {
    "employee ID": [101, 102, 103, 104, 104, 105, 106, 107],
    "name": [
        "  shikhar ",
        "RAHUL",
        None,
        "Priya ",
        "Priya ",
        " aDiTyA",
        "Karan",
        "Neha "
    ],
    "department": [
        "IT",
        "hr",
        "Finance",
        "IT",
        "IT",
        None,
        "Hr",
        " finance "
    ],
    "email": [
        "Shikhar@GMAIL.com",
        "rahul@yahoo.com",
        None,
        "PRIYA@gmail.COM",
        "PRIYA@gmail.COM",
        "aditya@outlook.com",
        "karan@gmail.com",
        "NEHA@GMAIL.COM"
    ],
    "salary": [
        "60000",
        "45000",
        "55000",
        None,
        None,
        "70000",
        "52000",
        "48000"
    ],
    "experience": [
        2,
        np.nan,
        4,
        5,
        5,
        np.nan,
        3,
        2
    ],
    "status": [
        "ACTIVE",
        "inactive",
        "Pending",
        "ACTIVE",
        "ACTIVE",
        "pending",
        "Inactive",
        "active"
    ]
}

df = pd.DataFrame(employees)

# ==========================================================
# PART 1 - Explore the Data
# ==========================================================

# 1. Print the first 5 rows.
# 2. Print the last 3 rows.
# 3. Print the shape of the DataFrame.
# 4. Print all column names.
# 5. Print the data types of each column.
# 6. Print DataFrame information using info().
class Panda_practice:
    def __init__(self,df):
        self.df=df

    def explore(self):
        print("\nTHE FIRST FIVE ROWS OF THE DATA SET ARE : \n",self.df.head(5))
        print("\nTHE LAST THREE ROWS OF THE DATA ARE:\n", self.df.tail(3))
        print("\nTHE SHAPE OF THE DATA FRAME IS :\n" , self.df.shape)
        print("\nTHE NAME OF ALL THE COLUMNS ARE : \n",self.df.info() )
        print("\nTHE DATA TYPE OF EACH COLUMN IS : \n" , self.df.dtypes)

    
    def fillnulls(self):
        self.df["salary"] = self.df["salary"].fillna(self.df["salary"].mean)
        self.df["experience"] = self.df["experience"].fillna(0)
        self.df["department"] = self.df["department"].fillna("Unknown")
        self.df["name"] = self.df["name"].fillna("Missing")
        self.df = self.df.dropna(subset=["email"])

        return self.df  

pp=Panda_practice(df)
print(pp.fillnulls())


# ==========================================================
# PART 2 - Missing Values
# ==========================================================

# 7. Find the number of missing values in each column.
# 8. Find the total number of missing values in the DataFrame.
# 9. Display only those rows that contain at least one missing value.
# 10. Fill missing Salary values with the mean Salary.
# 11. Fill missing Experience values with 0.
# 12. Fill missing Department values with "Unknown".
# 13. Fill missing Name values with "Missing".
    def missing(self):
        print("\nTHE TOTAL NUMBER OF MISSING VALUES IN EACH COLUMN IS : \n", self.df.isnull().sum())
        print("\nTHE TOTAL NUMBER OF MISSING VALUES  IN THE WHOLE DATA FRAME IS :\n" , self.df.isnull().sum().sum())
        print("\nTHE ROWS HAVING ATLEAST ONE MISSING VALUES: \n" , self.df[self.df.isnull().any(axis=1)])
        self.df["salary"] = self.df["salary"].fillna(self.df["salary"].mean())
        self.df["experience"]=self.df["experience"].fillna(0)
        self.df["department"]=self.df["department"].fillna("Unknown")
        self.df["name"]=self.df["name"].fillna("Missing")
        return self.df

# ==========================================================
# PART 3 - Duplicate Handling
# ==========================================================

# 14. Check which rows are duplicates.
# 15. Count the number of duplicate rows.
# 16. Remove duplicate rows.
# 17. Print the new shape of the DataFrame.
    def duplicate(self):
        print("THE ROWS WHICH ARE DUPLICATES ARE : ",self.df.duplicated())
        print("THE TOTAL NUMBER OF DUPLICATED ROWS ARE : ",self.df.duplicated().sum())
        self.df=self.df.drop_duplicates()
        print("\n THE NEW SHAPE OF THE DATA FRAME IS :\n",self.df.shape )


        return self.df

# ==========================================================
# PART 4 - String Cleaning
# ==========================================================

# 18. Remove leading/trailing spaces from:
#       - Name
#       - Department
#       - Email

# 19. Convert:
#       - Name to Title Case
#       - Department to lowercase
#       - Email to lowercase

# 20. Replace department values:
#       it -> IT
#       hr -> HR
#       finance -> Finance
#       unknown -> Unknown

# 21. Replace status values:
#       active -> Active
#       inactive -> Inactive
#       pending -> Pending
    def convert(self):
        self.df["name"]=self.df["name"].str.title().str.strip()
        self.df["department"]=self.df["department"].str.lower().str.strip()
        self.df["email"]=self.df["email"].str.lower().str.strip()
        self.df["status"] = self.df["status"].str.lower()
        self.df["department"] =self.df["department"].replace({
            "it" : "IT" , 
            "hr":"HR" ,
            "finance":"Finance" , 
            "unknown":"Unknown"
        })
        self.df["status"]=self.df["status"].replace({
            "active" : "Active" ,
            "inactive":"Inactive" , 
            "pending":"Pending"
        })
        return self.df




# ==========================================================
# PART 5 - Data Type Conversion
# ==========================================================

# 22. Convert Salary from string to integer.
# 23. Verify the data types again.
    def data(self):
        self.df["salary"] = self.df["salary"].astype(int)

        print("\nDATA TYPES AFTER CONVERSION:\n")
        print(self.df.dtypes)

        return self.df
# ==========================================================
# PART 6 - Creating New Columns
# ==========================================================

# 24. Create a new column called "Email_Domain"
#     Example:
#     shikhar@gmail.com -> gmail.com
    def new_col(self):
        self.df["email_domain"] = self.df.apply(
        lambda row: row["email"].split("@")[1],
        axis=1
    )

        return self.df
    
pp=Panda_practice(df)
print(pp.new_col())
