#  IN THIS PRACTICE SESSION WE ARE PRACTICING HOW THE "if_exists" METHOD  WORKS , AND HOW IT EFFECTS THE TABLE

import pandas as pd
from sqlalchemy import create_engine, text

engine = create_engine("sqlite:///prac2.db")

df = pd.DataFrame({
    "employee_id": [101, 102, 103, 104, 105, 106],
    "employee_name": ["Shikhar", "Aditya", "Vishesh",
                      "Shivam", "Vaishnavi", "Akshay"],
    "dept_name": ["DATA", "IT", "HR", "HR", "IT", "DATA"]
})

new_employees = pd.DataFrame({
    "employee_id": [107, 108],
    "employee_name": ["Rahul", "Priya"],
    "dept_name": ["DATA", "IT"]
})

df.to_sql("practice2", engine, if_exists="replace", index=False)

new_employees.to_sql("practice2", engine, if_exists="append", index=False)

all_data = pd.read_sql("SELECT * FROM practice2", engine)
print("\n THE DATABASE IS HAVING THE FOLLOWING DATA : \n" ,all_data)

data_dept = pd.read_sql(text("SELECT * FROM practice2 WHERE dept_name = :dname"),engine,params={"dname": "DATA"})
print("\nTHE EMPLOYEES WHO WORK IN THE DATA DEPARTMENT ARE:\n",data_dept)