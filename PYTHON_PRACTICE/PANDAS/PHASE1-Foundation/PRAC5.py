# ============================================
# PHASE 1 FINAL — Foundations Capstone
# Date: 24 June 2026
# Combines: DataFrame creation, head/tail/shape/info/describe,
# loc/iloc, column selection, dtypes, select_dtypes,
# basic boolean filtering, apply(), sort_values()
# Integrated with: OOP, Exception Handling
# ============================================

import pandas as pd

# A college wants a report on its 5th semester students.

students_data = {
    "roll_no": [101, 102, 103, 104, 105, 106, 107, 108],
    "name": ["Shikhar", "Rahul", "Priya", "Aditya",
             "Sneha", "Karan", "Meera", "Vikram"],
    "branch": ["CSE", "ECE", "CSE", "ME",
               "CSE", "ECE", "CSE", "ME"],
    "attendance_pct": [92, 65, 88, 45, 95, 70, 55, 80],
    "marks": [95, 60, 89, 38, 97, 55, 42, 75]
}

# QUESTION — Build a class StudentReport with:
#
# - Attribute: df (built from students_data inside __init__)
#
# - Method overview() that:
#       prints shape, dtypes, and describe() of numeric columns
#       (use select_dtypes)
#
# - Method get_student(roll_no) that:
#       raises ValueError if roll_no doesn't exist in df
#       otherwise returns that student's row using loc[]
#       (figure out how to check existence before using loc)
#
# - Method branch_filter(branch_name) that:
#       returns all students in the given branch
#       using boolean filtering
#
# - Method add_result_column() that:
#       uses apply() to add a "result" column:
#       "Pass" if marks >= 40 AND attendance_pct >= 75
#       "Fail" otherwise
#       (this needs row-wise apply since it checks 2 columns)
#
# - Method top_performers(n) that:
#       returns top n students sorted by marks descending
#       only columns: name, branch, marks, result
#
# - Method at_risk_students() that:
#       returns students where result is "Fail"
#       using boolean filtering on the result column
#
# Create a StudentReport object.
# Call overview().
# Call get_student(103) — should work.
# Call get_student(999) — should raise ValueError, catch it and print the message.
# Call branch_filter("CSE") and print result.
# Call add_result_column().
# Call top_performers(3) and print result.
# Call at_risk_students() and print result.

# YOUR CODE HERE:
df=pd.DataFrame(students_data)
class StudentReport:
    def __init__(self):
        self.df=df
    
    def overview(self):
        numeric_data= self.df.select_dtypes(include='number')
        print("\nTHE NUMERIC DATA TYPES ARE: \n")
        print(numeric_data)
        print("THE SHAPE OF THE NUMERIC DATA ARE: ",numeric_data.shape)
        print("\nTHE DTYPES OF THE NUMERIC DATA ARE:\n", numeric_data.dtypes)
        print("THE DESCRIPTION OF THE NUMERICS DATA ARE:\n", numeric_data.describe())

    def get_student(self,roll_number):
        if roll_number not in df["roll_no"].values:
            raise ValueError ("THE ROLL NUMBER DOES NOT EXIST ...")
        else :
            return self.df.loc[self.df["roll_no"]==roll_number]
    
    def branch_filter(self,branch_name):
        return self.df.loc[self.df["branch"]==branch_name]
    
    def add_result_columns(self):
        self.df["result"]=self.df.apply(lambda row : "Pass" if row["marks"]>=40 and row["attendance_pct"]>=75 else "Fail",axis=1)
        return self.df["result"] 

    def top_performers(self,n):
        return self.df[["name","marks","branch","result"]].sort_values(by="marks", ascending=False).head(n)
    
    def at_risk(self):
        return self.df[self.df["result"]=="Fail"]



sr=StudentReport()
sr.overview()
print(sr.get_student(103))
print(sr.branch_filter("CSE"))
try:
    print(sr.get_student(1111))
except ValueError as e:
    print(e)
print(sr.add_result_columns())
print(sr.top_performers(3))
print(sr.at_risk())