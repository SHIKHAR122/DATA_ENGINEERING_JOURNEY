# ============================================
# PANDAS PRACTICE - DAY 1 (Phase 1 - Foundations)
# Date: 19 June 2026
# Integrated with: OOP, Exception Handling, File Handling, Lambda
# ============================================

import pandas as pd

# QUESTION 1 - Easy
# Create a dictionary of student data:
# names, ages, marks, colleges (at least 6 students)
#
# - Convert it into a DataFrame
# - Print head(), tail(2), shape, info(), describe()
# - Print only the "marks" column
# - Print rows using both loc[] and iloc[] for index 2
# - Check dtype of each column

# YOUR CODE HERE:
students = {
    "name":["SHIKHAR","ADITYA","KRISH","SAMARTH","HARSH","SHIVAM"],
    "ages":[20,21,22,21,20,19],
    "marks":[100,99,98,90,91,97],
    "college":["PSIT","MAIT","KIT","AHSS","IIIT","IIMS"]
}
df = pd.DataFrame(students)
print(df)
print("HEAD IS :" , df.head())
print("TAIL IS :",df.tail(2))
print("SHAPE IS :",df.shape)
df.info()
print("DESCRIPTION IS : ",df.describe())
print(df["marks"])
print(df.loc[2])
print(df.loc[1:3,"name":"college"])
print(df.iloc[2])
print(df.dtypes)
# ============================================

# QUESTION 2 - Medium — Combined with File Handling + Exception Handling
# Write a class DataLoader with:
# - Attribute: filepath
# - Method load_csv() that:
#       tries to read the CSV into a DataFrame using pd.read_csv()
#       catches FileNotFoundError — prints "File not found"
#       catches pd.errors.EmptyDataError — prints "File is empty"
#       returns the DataFrame if successful, None otherwise
# - Method summary() that:
#       if DataFrame loaded: prints shape, columns, dtypes
#       if not loaded: prints "No data loaded yet"
#
# First write a CSV "employees.csv" with columns:
# emp_id, name, department, salary (at least 8 rows)
#
# Create a DataLoader object.
# Call load_csv() and summary().
# Try loading a missing file — should catch error gracefully.

# YOUR CODE HERE:
import csv 
data = [
    {"emp_id":1 , "name":"Shikhar" , "department":"data" , "salary":900000},
    {"emp_id":2 , "name":"Shivam" , "department":"HR" , "salary":60000},
    {"emp_id":3 , "name":"George" , "department":"data" , "salary":300000},
    {"emp_id":4 , "name":"John" , "department":"IT" , "salary":190000},
    {"emp_id":5 , "name":"Eren" , "department":"Finance" , "salary":750000},
    {"emp_id":6 , "name":"Nathan" , "department":"HR" , "salary":99000},
    {"emp_id":7 , "name":"Shivi" , "department":"Finance" , "salary":40000},
    {"emp_id":8 , "name":"Vaishnavi" , "department":"Finance" , "salary":89000}

]
with open ("employees.csv", "w",newline="")as file:
    writer=csv.DictWriter(file,fieldnames=["emp_id","name","department","salary"])
    writer.writeheader()
    writer.writerows(data)

class DataLoader:
    def __init__(self,filepath):
        self.filepath=filepath
        self.df=None

    def load_csv(self):
        try:
            self.df=pd.read_csv(self.filepath)
            return self.df
        except FileNotFoundError :
            print("FILE NOT FOUND")
        except pd.errors.EmptyDataError:
            print("FILE IS EMPTY")

        return None

    def summary(self):
        if self.df is None :
            print("NO DATA IS LOADED YET")
            return 
        
        print("SHAPE IS :", self.df.shape)
        print("\n Columns")
        print(self.df.columns)

        print("\nDATA TYPES")
        print(list(self.df.dtypes))

loader=DataLoader("employees.csv")
loader.load_csv()
loader.summary()
    
bad_loader = DataLoader("missing.csv")
bad_loader.load_csv()
bad_loader.summary()
# ============================================

# QUESTION 3 - Medium — Combined with Lambda
# Using the employees DataFrame from Question 2:
#
# - Select only "name" and "salary" columns
# - Use loc[] to select rows where department is "Data"
# - Use iloc[] to select first 3 rows, first 2 columns
# - Create a new column "salary_category" using apply() + lambda:
#       "High" if salary > 80000
#       "Medium" if salary > 50000
#       "Low" otherwise
# - Print dtype of every column
# - Convert "emp_id" column to string using astype()

# YOUR CODE HERE:
df=pd.DataFrame(data)
print(df[["name" , "salary"]])


print(df.loc[df["department"]=="data"])

print(df.iloc[0:3,0:2])


df["salary category"]=df["salary"].apply(
    lambda salary: "High" if salary>80000
    else "Medium" if salary>50000 else "Low"
)
print(df)

print(list(df.dtypes))
df["emp_id"]=df["emp_id"].astype(str)

print(df.dtypes)
# ============================================

# QUESTION 4 - Harder — Combined with OOP + Exception Handling
# Create a class EmployeeAnalyzer with:
# - Attribute: df (a DataFrame passed during init)
# - Method validate() that:
#       raises ValueError if df is empty
#       raises ValueError if "salary" column has any negative values
#       otherwise prints "Data validated successfully"
# - Method get_high_earners(threshold) that:
#       uses boolean filtering to return employees
#       with salary above threshold
# - Method describe_numeric() that:
#       returns describe() only for numeric columns
#       hint: df.describe() automatically does this,
#       but explicitly select numeric columns using
#       df.select_dtypes(include='number')
#
# Create an EmployeeAnalyzer with the employees DataFrame.
# Call validate().
# Call get_high_earners(60000) and print result.
# Call describe_numeric() and print result.
#
# Now manually add a row with salary = -5000 to test
# validate() raising the ValueError correctly.

# YOUR CODE HERE:

class EmployeeAnalyzer:
    def __init__(self,df):
        self.df=df
    
    def validate(self):
        if self.df.empty:
            raise ValueError(" DATA FRAME CANNOT BE EMPTY")
        if (self.df["salary"]<0).any():
            raise ValueError("VALUE CANNOT BE NEGATIVE")
        
        print("DATA VALIDATED SUCCCESSFULLY")

    def high_earners(self,threshold):
        return self.df.loc[self.df["salary"]>threshold,["name","salary"]]
    
    def describe_numeric(self):
        numeric_df=self.df.select_dtypes(include="number")
        return numeric_df.describe()

analyzer=EmployeeAnalyzer(df)
analyzer.validate()
print("\nHIGH EARNERS:\n")
print(analyzer.high_earners(30000))

print("\nNUMERIC SUMMARY\n")
print(analyzer.describe_numeric())

# ============================================

# QUESTION 5 - Hardest — Full Integration
# Combine everything — OOP, exception handling,
# file handling, lambda, and Pandas basics.
#
# Create a class EmployeePipeline with:
# - Attribute: filepath
# - Attribute: df (None initially)
# - Method extract() that:
#       tries to read CSV using pd.read_csv()
#       catches FileNotFoundError and prints message
#       stores result in self.df
# - Method inspect() that:
#       if self.df is None: raise ValueError("No data — run extract() first")
#       prints shape, dtypes, head(3)
# - Method add_salary_band() that:
#       uses apply() + lambda to add "salary_band" column:
#       "A" if salary >= 90000
#       "B" if salary >= 60000
#       "C" otherwise
# - Method top_earners(n) that:
#       returns top n employees sorted by salary descending
#       use sort_values()
#
# Create a pipeline object.
# Call extract() — should load employees.csv.
# Call inspect().
# Call add_salary_band().
# Call top_earners(3) — print result.
# Try calling inspect() before extract() on a NEW pipeline
# object with wrong filepath — should raise the ValueError.

# YOUR CODE HERE:

class EmployeePipeline:
    def __init__(self,filepath):
        self.df=None
        self.filepath=filepath
    def extract(self):
        try:
            self.df=pd.read_csv(self.filepath)
        except FileNotFoundError:
            print("FILE NOT FOUND ")

    def inspect(self):
        if self.df is None:
            raise ValueError("NO DATA - RUN extract() first")
        print("\nTHE SHAPE OF THE DATA FRAM IS \n",self.df.shape)
        print(self.df.dtypes)
        print("\n THE HEAD IOF THE DATA FRAME IS :\n",self.df.head(3))

    def add_salary_band(self):
        self.df["salary_band"]=self.df["salary"].apply(
            lambda salary:"A" if salary>=90000 else "B" if salary>=60000 else "C"
        )
        print(self.df)

    def top_earners(self,n):
        return (self.df.sort_values(by="salary",ascending=False)).head(n)

pipeline=EmployeePipeline("employees.csv")

pipeline.extract()
pipeline.inspect()

pipeline.add_salary_band()

print(pipeline.top_earners(3))


#  TEST CASES TO GENERATE AND VERIFY THE ERRORS...

# bad_pipeline=EmployeePipeline("wrong.csv")

# try:
#     bad_pipeline.inspect()
# except ValueError as e:
#     print(e)