# ============================================
# FILE HANDLING — FULL PRACTICE SET
# Date: 10 June 2026
# ============================================

# QUESTION 1 - CSV Basic Write
# Create a list of dictionaries for 5 employees:
# fields: emp_id, name, department, salary
# Write it to "employees.csv" with proper headers.
# Print "employees.csv created successfully"

# YOUR CODE HERE:
import csv
data=[
    ["emp_id" , "name", "departement" , "salary"],
    [1,"shikhar ", "data", 750000],
    [2,"aditya","IT",850000],
    [3,"abhay","HRA",650000],
    [4,"ayush","data",450000],
    [5,"akshat","data",780000]
]

def write_csv(filename):
    with open(filename, "w",newline="") as file:
        writer=csv.writer(file,delimiter=",")
        writer.writerows(data)
        print("employees.csv created successfully")
write_csv("employee.csv")
#===========================================

# QUESTION 2 - CSV Basic Read
# Read "employees.csv" and print each row.
# Also print total number of employees.

# YOUR CODE HERE:
def read_csv(filename):
    with open(filename,"r") as file:
        content=csv.reader(file)
        header=next(content)
        for row in content:
            print(row)
        print("read successfully")


read_csv("employee.csv")

# ============================================

# QUESTION 3 - CSV Filter
# Read "employees.csv" and print only employees
# whose salary is above 50000.
# Print count of how many qualify.

# YOUR CODE HERE:
def filter(filename):
    count=0
    with open (filename , "r") as file:
        reader=csv.reader(file)
        header=next(reader)
        for row in reader:
            if int(row[3])>650000:
                print(row)
                count+=1
        print(count)
filter("employee.csv")


# ============================================

# QUESTION 4 - CSV Update
# Read "employees.csv".
# Give every employee in "data department
# a 10% salary raise.
# Write the updated data back to the same file.
# Print "Salaries updated"

# YOUR CODE HERE:
import csv
def update(filename):
    updated_rows=[]
    with open (filename,"r") as file:
        reader=csv.DictReader(file)
        for row in reader:
            if row["departement"].lower()=="data":
                current_salary=int(row["salary"])
                row["salary"]=int(current_salary * 1.10)
            updated_rows.append(row)
        
    with open(filename,"w",newline="") as file:
        writer=csv.DictWriter(file,fieldnames=["emp_id","name","departement","salary"])
        writer.writeheader()
        writer.writerows(updated_rows)
    print("SALARY UPDATED")
update("employee.csv")



# ============================================

# QUESTION 5 - JSON Basic Write
# Create a dictionary for a student:
# fields: name, college, semester, subjects (list),
#         scores (dict with subject:score pairs)
# Write it to "student.json" with indent=4
# Print "student.json created successfully"

# YOUR CODE HERE:
import json
data = {
    "name": "Shikhar",
    "college": "PSIT",
    "semester": 5,
    "subjects": ["CPP", "Python", "DSA", "SQL"],
    "scores": {
        "CPP": 95,
        "Python": 99,
        "DSA": 92,
        "SQL": 90
    }
}
def write_json(filename):
    with open (filename , "w") as file:
        json.dump(data,file,indent=4)
    print("JSON WRITTEN SUCCESSFULLY")

write_json("student.json")
    
# ============================================

# QUESTION 6 - JSON Basic Read
# Read "student.json"
# Print student name and college
# Print each subject and its score
# Print average score

# YOUR CODE HERE:
import json
def read_json(filename):
    with open(filename,"r") as file:
        reader=json.load(file)
        print(reader)
    print("READ SUCCESFULLY")
read_json("student.json")
# ============================================

# QUESTION 7 - JSON Update
# Read "student.json"
# Add a new subject "Data Engineering" with score 95
# Write back to the same file
# Print "student.json updated"

# YOUR CODE HERE:
import json 
updated_subject=[]
def update_json(filename):
    with open(filename,"r") as file:
        json.load(file)
    data["subjects"].append("data engineering")        
    data["scores"]["data engineering"]=95
    with open(filename, "w") as file:
        json.dump(data,file,indent=2)
print("JSON FILE UPDATED")

update_json("student.json")

# ============================================

# QUESTION 8 - CSV + Exception Handling
# Write a function safe_read_csv(filename) that:
# - Reads any CSV file
# - Catches FileNotFoundError
# - Catches csv.Error for malformed CSV
# - Catches PermissionError
# - Returns list of rows as dicts if successful
# - Returns empty list on any error
#
# Test with valid file and missing file.

# YOUR CODE HERE:
def safe_read_csv(filename):
    
    with open(filename,"r") as file:
        try:
            reader=csv.DictReader(file)
            res=[]
            for row in reader:
                res.append(dict(row))
            return res
        except FileNotFoundError:
            print("FILE NOT FOUND")
        except csv.Error:
            print("NOT FORMATED CSV")
        except PermissionError:
            print("NO PERMISSION GRANTED")
        return []
data=safe_read_csv("employee.csv")
print(data)
# ============================================

# QUESTION 9 - JSON + Exception Handling
# Write a function safe_read_json(filename) that:
# - Reads any JSON file
# - Catches FileNotFoundError
# - Catches json.JSONDecodeError
# - Catches PermissionError
# - Returns parsed data if successful
# - Returns None on any error
# - Logs every error to "errors.log" with timestamp
#
# Test with valid file, missing file, and
# create a file called "broken.json" with
# content "this is not json" to test JSONDecodeError

# YOUR CODE HERE:
import json
from datetime import datetime

def safe_read_json(filename):
    try:
        with open(filename, "r") as file:
            data = json.load(file)
            return data
    except FileNotFoundError as e:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open("errors.log", "a") as log_file:
            log_file.write(f"{timestamp} | FileNotFoundError | {e}\n")
        print("FILE NOT FOUND")
    except json.JSONDecodeError as e:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open("errors.log", "a") as log_file:
            log_file.write(f"{timestamp} | JSONDecodeError | {e}\n")
        print("INVALID JSON FORMAT")
    except PermissionError as e:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open("errors.log", "a") as log_file:
            log_file.write(f"{timestamp} | PermissionError | {e}\n")
        print("PERMISSION DENIED")

    return None

# print(safe_read_json("student.json"))

# # Missing file
# print(safe_read_json("missing.json"))

# Create broken JSON file for testing
with open("broken.json", "w") as file:
    file.write("this is not json")

print(safe_read_json("broken.json"))


# ============================================

# QUESTION 10 - Real World — Data Cleaning Pipeline
# You have this raw data as a list of dicts:
raw_data = [
    {"id": 1, "name": "Shikhar", "age": "21", "salary": "90000"},
    {"id": 2, "name": "", "age": "25", "salary": "75000"},
    {"id": 3, "name": "Rahul", "age": "abc", "salary": "80000"},
    {"id": 4, "name": "Aditya", "age": "28", "salary": "-5000"},
    {"id": 5, "name": "Priya", "age": "22", "salary": "65000"},
    {"id": 6, "name": "Karan", "age": "30", "salary": "95000"},
    {"id": 7, "name": "", "age": "27", "salary": "70000"},
]
# Write a pipeline that:
# - Removes rows where name is empty
# - Converts age to integer — skip row if conversion fails
# - Converts salary to integer — skip row if conversion fails
# - Removes rows where salary is negative
# - Writes clean data to "clean_employees.csv"
# - Writes rejected rows with reason to "rejected.csv"
#   reason column should say why it was rejected:
#   "empty name", "invalid age", "invalid salary",
#   "negative salary"
# - Prints summary:
#   "Total rows: 7"
#   "Clean rows: X"
#   "Rejected rows: X"

# YOUR CODE HERE:
def remove_rows(filename):
    clean_row=[]
    rejected_row=[]
    total_row=[]
    with open(filename,"r")as file:
        reader=csv.DictReader(file)
        for row in reader:
            total_row+=1
            if row["name"].strip() is "":
                row["reason"]="empty name"
                rejected_row.append(row)
                continue
        try:
            row["age"]=int(row["age"])
        except ValueError:
            row["reason"]="invalid age"
            rejected_row.append(row)
            
        
            
# ============================================

# QUESTION 11 - Real World — Student Report Generator
# You have student data in a CSV called "class_data.csv"
# Create this file first with at least 8 students:
# fields: name, maths, science, english, hindi
#
# Write a pipeline that:
# - Reads the CSV
# - Calculates total and average for each student
# - Assigns grade: A(90+), B(75+), C(60+), D(40+), F
# - Writes full report to "report.json" with structure:
#   {
#     "total_students": X,
#     "class_average": X,
#     "top_student": "name",
#     "students": [
#         {"name": ..., "total": ...,
#          "average": ..., "grade": ...}
#     ]
#   }
# - Prints the top student and class average

# YOUR CODE HERE:


# ============================================

# QUESTION 12 - Real World — Inventory Manager
# Build a simple inventory system using JSON as storage:
#
# Create a class InventoryManager with:
# - Attribute: filename (JSON file to store data)
# - Method load() that reads JSON file
#   returns empty dict if file doesn't exist
# - Method save(data) that writes data to JSON file
# - Method add_item(name, quantity, price) that:
#       loads current inventory
#       if item exists: updates quantity
#       if new: adds with quantity and price
#       saves back to file
# - Method remove_item(name, quantity) that:
#       loads current inventory
#       raises KeyError if item not found
#       raises ValueError if quantity > available
#       reduces quantity and saves
# - Method display() that:
#       loads and prints all items with
#       name, quantity, price, total value
# - Method total_value() that:
#       returns sum of quantity * price for all items
#
# Test all methods thoroughly.

# YOUR CODE HERE:


# ============================================

# QUESTION 13 - Real World — Sales Data Analyzer
# Create this sales data CSV first — "sales.csv":
# fields: date, product, category, quantity, price
# Add at least 10 rows with different dates,
# products and categories.
#
# Write a pipeline that reads "sales.csv" and:
# - Calculates total revenue per product
# - Calculates total revenue per category
# - Finds best selling product by quantity
# - Finds highest revenue product
# - Writes summary to "sales_summary.json"
# - Prints the summary neatly

# YOUR CODE HERE:


# ============================================

# QUESTION 14 - Real World — Log Analyzer
# Build on top of your log_event and read_logs
# functions from yesterday.
#
# Add a function analyze_logs(filename) that:
# - Reads the log file
# - Counts total logs
# - Counts logs per level (INFO, WARNING, ERROR)
# - Finds the first ERROR and prints it
# - Finds the last ERROR and prints it
# - Returns a summary dict:
#   {
#     "total": X,
#     "INFO": X,
#     "WARNING": X,
#     "ERROR": X,
#     "first_error": "...",
#     "last_error": "..."
#   }
# - Writes summary to "log_summary.json"
#
# Generate at least 10 log events first
# then run analyze_logs on them.

# YOUR CODE HERE:


# ============================================

# QUESTION 15 - HARDEST — ETL Mini Pipeline
# Build a complete mini ETL pipeline using only
# file handling — no Pandas yet.
#
# You have raw sales data — create "raw_sales.csv":
# fields: transaction_id, customer_name, product,
#         quantity, unit_price, date
# Add 10+ rows including some dirty data:
# - Some rows with missing customer_name
# - Some rows with invalid quantity (negative or text)
# - Some rows with invalid unit_price (negative or text)
#
# EXTRACT:
# - Read raw_sales.csv
# - Log "Extraction started" to pipeline.log
# - Log total rows extracted
#
# TRANSFORM:
# - Remove rows with missing customer_name
# - Convert quantity and unit_price to numbers
# - Skip invalid rows and log them as WARNING
# - Calculate total_price = quantity * unit_price
# - Add a processed_at timestamp column
#
# LOAD:
# - Write clean data to "processed_sales.csv"
# - Write rejected rows to "rejected_sales.csv"
#
# SUMMARY:
# - Write pipeline summary to "pipeline_summary.json":
#   total extracted, total loaded, total rejected,
#   pipeline start time, pipeline end time,
#   total revenue from clean data
# - Log "Pipeline completed" to pipeline.log
# - Print the summary

# YOUR CODE HERE: