# IN THIS SESSION WE ARE LEARNING HOW TO WORK WITH LARGE DATA BATCHED TOGETHER 
# PROBLEM STATEMENT - 
# Read a table in chunksize batches and sum a column across all chunks (same pattern as chunked CSV reading).

import pandas as pd
from sqlalchemy import create_engine 
import numpy as np


engine=create_engine("sqlite:///practice3.db")
big_df = pd.DataFrame({
    "employee_id": range(1, 10001),
    "employee_name": [f"Employee_{i}" for i in range(1, 10001)],
    "dept_name": np.random.choice(["DATA", "IT", "HR", "FINANCE"], size=10000),
    "salary": np.random.randint(30000, 150000, size=10000)
})

big_df.to_sql("practice3" , engine ,if_exists="replace",index=False)

total_salary=0
for chunk in pd.read_sql("SELECT * FROM  practice3" , engine  , chunksize=1000):
    total_salary+=chunk["salary"].sum()

print("THE TOTAL SALARY ACROSS ALL THE CHUNKS IS : " , total_salary)
direct_sum= pd.read_sql_query("SELECT SUM(salary) AS total_salary FROM practice3 " , engine )
print(" THE DIRECT SUM OF THE SALARY USING SQL QUERY IS : " , direct_sum)