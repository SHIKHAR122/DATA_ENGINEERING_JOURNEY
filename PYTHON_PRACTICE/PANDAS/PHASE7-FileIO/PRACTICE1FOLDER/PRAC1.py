# THIS IS THE VERY FIRST TESTING FOR THE PHASE  , FOR CURRENT PRACTICE SESSIONS WE ARE USING THE BUILT IN SQLITE LIBRARY4
# FOR THE UPCOMING SESSIONS WE WILL BE WORKING WITH SQLALCHEMY AND ALSO WITH A LARGE LIVE DATA SET 


# 10 AUGUST 2026 - SESSION I 


from sqlalchemy import create_engine
import pandas as pd 
engine = create_engine("sqlite:///practice.db")
df=pd.DataFrame({
    "id":[1,2,3,4,5,] , 
    "name":["SHIKHAR" , "ADITYA" ,"ATISH"  , "VISHESH" , "VAISHNAVI" ],
    "age":[20,21,22,21,20]
})
df.to_sql("employees" , engine  , if_exists="replace" ,index=False)
result=pd.read_sql("SELECT * FROM employees" , engine)

print(result)
print(f"Total Rows : {len(result)}")