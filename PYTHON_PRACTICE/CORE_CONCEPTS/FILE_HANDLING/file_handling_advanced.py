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
    employee_count=0
    with open(filename,"r") as file:
        content=csv.reader(file)
        header=next(content)
        for row in content:
            employee_count+=1
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
        data=json.load(file)
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
    
    
        try:
            with open(filename,"r") as file:
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
import csv
def clean_employee_data(filename):
    clean_rows = []
    rejected_rows = []
    total_rows = 0
    with open(filename, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            total_rows += 1
            # Empty name
            if row["name"].strip() == "":
                row["reason"] = "empty name"
                rejected_rows.append(row)
                continue
            # Invalid age
            try:
                row["age"] = int(row["age"])
            except ValueError:
                row["reason"] = "invalid age"
                rejected_rows.append(row)
                continue

            # Invalid salary
            try:
                row["salary"] = int(row["salary"])
            except ValueError:
                row["reason"] = "invalid salary"
                rejected_rows.append(row)
                continue
            # Negative salary
            if row["salary"] < 0:
                row["reason"] = "negative salary"
                rejected_rows.append(row)
                continue
            clean_rows.append(row)
    # Write clean rows
    with open("clean_employees.csv", "w", newline="") as file:
        writer = csv.DictWriter(file,fieldnames=["name", "age", "salary"])
        writer.writeheader()
        writer.writerows(clean_rows)
    # Write rejected rows
    with open("rejected.csv", "w", newline="") as file:

        writer = csv.DictWriter(file,fieldnames=["name", "age", "salary", "reason"])
        writer.writeheader()
        writer.writerows(rejected_rows)
    print(f"Total rows: {total_rows}")
    print(f"Clean rows: {len(clean_rows)}")
    print(f"Rejected rows: {len(rejected_rows)}")
# ============================================)

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
data=[
    {"name":"shikhar","maths":90,"science":89,"english":88,"hindi":97},
    {"name":"shivam","maths":70,"science":69,"english":22,"hindi":65},
    {"name":"abhay","maths":80,"science":84,"english":53,"hindi":76},
    {"name":"ashish","maths":40,"science":39,"english":43,"hindi":65},
    {"name":"vaishnavi","maths":99,"science":87,"english":99,"hindi":75},
    {"name":"ajay","maths":20,"science":39,"english":75,"hindi":54},
    {"name":"amara","maths":60,"science":83,"english":38,"hindi":43},
    {"name":"sanjay","maths":70,"science":65,"english":53,"hindi":54}
]

def student_report_generator(filename):
    with open(filename,"w",newline="") as file:
        writer=csv.DictWriter(file,fieldnames=["name","maths","science","english","hindi"])
        writer.writeheader()
        writer.writerows(data)
    print("csv file created successfully")

    students=[]
    class_average_sum=0
    highest_total=0
    top_students=""

    ##PIPELINE CREATION
    with open(filename,"r") as file:
        reader=csv.DictReader(file)

        for row in reader:
            total=(
                int(row["maths"])+
                int(row["science"])+
                int(row["english"])+
                int(row["hindi"])
            )

            average=round(total/4,2)

            if average>=90:
                grade="A"
            elif average>=75:
                grade="B"
            elif average>=60:
                grade="C"
            elif average>=40:
                grade="D"
            else:
                grade="F"

            student={
                "name":row["name"],
                "total":total,
                "average":average,
                "grade":grade
            }

            students.append(student)
            class_average_sum+=average

            if total>highest_total:
                highest_total=total
                top_students=row["name"]

    class_average=round(class_average_sum/len(students),2)

    report={
        "total_students":len(students),
        "class_average":class_average,
        "top_student":top_students,
        "students":students
    }

    with open("report.json","w") as file:
        json.dump(report,file,indent=4)
    print("REPORT GENERATED SUCCESSFULLY")
    print("TOP STUDENT:",top_students)
    print("CLASS AVERAGE:",class_average)

student_report_generator("class_data.csv")

# student_report_generator("class_data")
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
import json
class InventoryManager:
    def __init__(self,filename):
        self.filename=filename

    def load(self):
        try:
            with open(self.filename,"r") as file:
                data=json.load(file)
                return data 
        except FileNotFoundError:
            return {}
        
    def save(self,data):
        with open(self.filename, "w") as file:
            json.dump(data,file,indent=4)
    
        
    def add_item(self,name,quantity,price):
        inventory=self.load()
        if name in inventory:
            inventory[name]["quantity"]+=quantity
        else:
            inventory[name]={
                "quantity":quantity,
                "price":price
            }
        self.save(inventory)
        print("ITEM UPDATED")
    
    def remove_item(self,name,quantity):
        inventory=self.load()
        if name not in inventory:
            raise KeyError("ITEM NOT FOUND")
        
        if quantity>inventory[name]["quantity"]:
            raise ValueError ("NOT ENOUGH QUANTITY AVAILABLE")
    
        inventory[name]["quantity"]-=quantity
        self.save(inventory)


    def display(self):
        inventory=self.load()
        for name , details in inventory.items():
            quantity=details["quantity"]
            price=details["price"]
            total=quantity*price
            print("NAME : {}   QUANTITY : {}  PRICE : {}  TOTAL : {}".format(name,quantity,price,total))


    def total_value(self):
        inventory = self.load()
        total = 0
        for details in inventory.values():
            total += (details["quantity"]* details["price"])
        return total


manager = InventoryManager("inventory.json")
manager.add_item("Laptop", 10, 50000)
manager.add_item("Mouse", 20, 500)
manager.add_item("Laptop", 5, 50000)
manager.display()
print("TOTAL INVENTORY VALUE =", manager.total_value())
manager.remove_item("Mouse", 5)
manager.display()

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
data = [
    {"date":"2026-01-05","product":"Laptop","category":"Electronics","quantity":2,"price":65000},
    {"date":"2026-01-05","product":"Mouse","category":"Electronics","quantity":10,"price":500},
    {"date":"2026-01-06","product":"Keyboard","category":"Electronics","quantity":5,"price":1200},
    {"date":"2026-01-06","product":"T-Shirt","category":"Clothing","quantity":8,"price":799},
    {"date":"2026-01-07","product":"Jeans","category":"Clothing","quantity":4,"price":1499},
    {"date":"2026-01-07","product":"Notebook","category":"Stationery","quantity":20,"price":50},
    {"date":"2026-01-08","product":"Pen","category":"Stationery","quantity":50,"price":10},
    {"date":"2026-01-08","product":"Monitor","category":"Electronics","quantity":3,"price":15000},
    {"date":"2026-01-09","product":"Shoes","category":"Footwear","quantity":6,"price":2499},
    {"date":"2026-01-09","product":"Socks","category":"Footwear","quantity":15,"price":199}
]
def SalesDataAnalyzer(filename):
    with open(filename, "w",newline="") as file:
        writer=csv.DictWriter(file,fieldnames=["date","product","category","quantity","price"])
        writer.writeheader()
        writer.writerows(data)
    total_revenue_category={}
    total_revenue_product={}
    product_quantity={}
    with open(filename,"r") as file:
        reader=csv.DictReader(file)
        for row in reader:
            product=row["product"]
            category=row["category"]
            quantity = int(row["quantity"])
            price = int(row["price"])

            revenue=price*quantity

            if product not in total_revenue_product:
                total_revenue_product[product]=0
            total_revenue_product[product]+=revenue

            if category not in total_revenue_category:
                total_revenue_category[category]=0
            total_revenue_category[category]+=1

            if quantity not in product_quantity:
                product_quantity[product]=0
            product_quantity[product]+=1

    best_selling_product= max(product_quantity,key=product_quantity.get)
    highest_revenue_product=max(total_revenue_product,key=total_revenue_product.get)
    
    summary={
        "revenue per product": total_revenue_product,
        "revenue per category": total_revenue_category,
        "product quantity": product_quantity,
        "best selling product": best_selling_product,
        "highest revenue product ": highest_revenue_product
    }

    with open("sales_summary.json","w") as file:
        json.dump(summary,file,indent=4)
        print("\nSALES SUMMARY")
    print("-" * 40)

    print("\nRevenue Per Product")

    for product, revenue in total_revenue_product.items():

        print(product, ":", revenue)

    print("\nRevenue Per Category")

    for category, revenue in total_revenue_category.items():

        print(category, ":", revenue)

    print("\nBest Selling Product :", best_selling_product)

    print(
        "Highest Revenue Product :",
        highest_revenue_product
    )

SalesDataAnalyzer("sales_data.csv")






# ============================================
# QUESTION 14 - Real World — Log Analyzer
# Date: 10 June 2026
# ============================================

# Build on top of your log_event and read_logs
# functions from the previous file handling set.
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

from datetime import datetime
import json
def log_event(filename, level, message):
    try:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(filename, "a") as file:
            file.write(f"{timestamp} | {level} | {message}\n")
    except OSError as e:
        print("FILE ERROR", e)

def analyze_logs(filename):
    total = 0
    counts = {"INFO": 0, "WARNING": 0, "ERROR": 0}
    first_error = None
    last_error = None

    with open(filename, "r") as file:
        for line in file:
            total += 1
        if "INFO" in line:
            counts["INFO"] += 1
        elif "WARNING" in line:
            counts["WARNING"] += 1
        elif "ERROR" in line:
            counts["ERROR"] += 1
            if first_error is None:
                first_error = line.strip()
            last_error = line.strip()
    summary = {
        "total": total,
        "INFO": counts["INFO"],
        "WARNING": counts["WARNING"],
        "ERROR": counts["ERROR"],
        "first_error": first_error,
        "last_error": last_error
    }

    with open("log_summary.json", "w") as file:
        json.dump(summary, file, indent=4)  # which json function?

    return summary
    
    


# Generate 10 log events first
log_event("pipeline.log", "INFO", "Pipeline started")
log_event("pipeline.log", "INFO", "Connecting to database")
log_event("pipeline.log", "INFO", "Connection successful")
log_event("pipeline.log", "WARNING", "Slow query detected")
log_event("pipeline.log", "INFO", "Data extraction started")
log_event("pipeline.log", "ERROR", "Timeout on table users")
log_event("pipeline.log", "INFO", "Retrying extraction")
log_event("pipeline.log", "WARNING", "Null values found: 12")
log_event("pipeline.log", "ERROR", "Database connection lost")
log_event("pipeline.log", "INFO", "Pipeline failed — exiting")

# Then analyze
summary = analyze_logs("pipeline.log")
print(summary)


# ============================================
# QUESTION 15 - HARDEST — ETL Mini Pipeline
# Date: 10 June 2026
# ============================================

# Build a complete mini ETL pipeline using only
# file handling — no Pandas yet.
#
# STEP 1 — Create raw_sales.csv with this data:
# fields: transaction_id, customer_name, product,
#         quantity, unit_price, date
# Include dirty rows:
# - Some with missing customer_name
# - Some with invalid quantity (negative or text)
# - Some with invalid unit_price (negative or text)
#
# STEP 2 — EXTRACT:
# - Read raw_sales.csv
# - Log "Extraction started" to pipeline.log
# - Log "Extracted X rows" to pipeline.log
#
# STEP 3 — TRANSFORM:
# - Remove rows with missing customer_name
#   log each rejection as WARNING
# - Convert quantity to int — skip if invalid
#   log each rejection as WARNING
# - Convert unit_price to int — skip if invalid
#   log each rejection as WARNING
# - Skip rows where quantity or unit_price is negative
#   log each rejection as WARNING
# - Calculate total_price = quantity * unit_price
# - Add processed_at timestamp column
#
# STEP 4 — LOAD:
# - Write clean rows to "processed_sales.csv"
# - Write rejected rows to "rejected_sales.csv"
#   include a "reason" column
# - Log "Loaded X clean rows" to pipeline.log
# - Log "Rejected X rows" to pipeline.log
#
# STEP 5 — SUMMARY:
# - Calculate total revenue from clean data
# - Write to "pipeline_summary.json":
#   {
#     "pipeline_start": "timestamp",
#     "pipeline_end": "timestamp",
#     "total_extracted": X,
#     "total_loaded": X,
#     "total_rejected": X,
#     "total_revenue": X
#   }
# - Log "Pipeline completed" to pipeline.log
# - Print the summary

# RAW DATA TO USE:
raw_sales = [
    {"transaction_id": 1, "customer_name": "Shikhar",
     "product": "Laptop", "quantity": "2",
     "unit_price": "65000", "date": "2026-06-01"},
    {"transaction_id": 2, "customer_name": "",
     "product": "Mouse", "quantity": "5",
     "unit_price": "500", "date": "2026-06-01"},
    {"transaction_id": 3, "customer_name": "Rahul",
     "product": "Keyboard", "quantity": "abc",
     "unit_price": "1200", "date": "2026-06-02"},
    {"transaction_id": 4, "customer_name": "Aditya",
     "product": "Monitor", "quantity": "3",
     "unit_price": "-5000", "date": "2026-06-02"},
    {"transaction_id": 5, "customer_name": "Priya",
     "product": "Headphones", "quantity": "4",
     "unit_price": "3000", "date": "2026-06-03"},
    {"transaction_id": 6, "customer_name": "Karan",
     "product": "Webcam", "quantity": "-2",
     "unit_price": "2000", "date": "2026-06-03"},
    {"transaction_id": 7, "customer_name": "Sneha",
     "product": "USB Hub", "quantity": "10",
     "unit_price": "800", "date": "2026-06-04"},
    {"transaction_id": 8, "customer_name": "",
     "product": "Mousepad", "quantity": "6",
     "unit_price": "300", "date": "2026-06-04"},
    {"transaction_id": 9, "customer_name": "Vikram",
     "product": "Chair", "quantity": "1",
     "unit_price": "xyz", "date": "2026-06-05"},
    {"transaction_id": 10, "customer_name": "Meera",
     "product": "Desk", "quantity": "1",
     "unit_price": "15000", "date": "2026-06-05"},
]

def log_events(filename,level,message):
    timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(filename,"a") as log_event:
        log_event.write("{} | {} | {}\n".format(timestamp,level,message))


def create_csv(filename):
    try:
        with open(filename,"w",newline="") as file:
            writer=csv.DictWriter(file,fieldnames=["transaction_id","customer_name","product","quantity","unit_price","date"])
            writer.writeheader()
            writer.writerows(raw_sales)
    except OSError as e:
        print("FILE ERROR",e)


def extract(filename):
    log_events("pipeline.log","INFO","Extraction Started")

    with open(filename,"r") as file:
        reader=csv.DictReader(file)
        rows=list(reader)

    log_events("pipeline.log","INFO","Extracted {} rows".format(len(rows)))
    return rows


def transform(filename):
    clean_rows=[]
    rejected_row=[]
    with open(filename,"r") as file:
        reader=csv.DictReader(file)
        for row in reader:
            if row["customer_name"]=="":
                row["reason"]="empty customer name"
                rejected_row.append(row)
                log_events("pipeline.log","WARNING","Rejected Transaction")
                continue

            try:
                quantity=int(row["quantity"])
            except ValueError:
                row["reason"]="invalid quantity"
                rejected_row.append(row)
                log_events("pipeline.log","WARNING","Rejected Transaction")
                continue

            try:
                unit=int(row["unit_price"])
            except ValueError:
                row["reason"]="invalid unit price"
                rejected_row.append(row)
                log_events("pipeline.log","WARNING","Rejected Transaction")
                continue

            if unit<0:
                row["reason"]="negative unit price"
                rejected_row.append(row)
                log_events("pipeline.log","WARNING","Rejected Transaction")
                continue

            if quantity<0:
                row["reason"]="negative quantity"
                rejected_row.append(row)
                log_events("pipeline.log","WARNING","Rejected Transaction")
                continue

            row["quantity"]=quantity
            row["unit_price"]=unit
            row["total_price"]=quantity*unit
            row["processed_at"]=datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            clean_rows.append(row)
    return clean_rows,rejected_row


def load(clean_rows,rejected_row):
    with open("processed_sales.csv","w",newline="") as clean_file:
        writer=csv.DictWriter(clean_file,fieldnames=["transaction_id","customer_name","product","quantity","unit_price","date","total_price","processed_at"])
        writer.writeheader()
        writer.writerows(clean_rows)
    with open("rejected_sales.csv","w",newline="") as rejected_file:
        writer=csv.DictWriter(rejected_file,fieldnames=["transaction_id","customer_name","product","quantity","unit_price","date","reason"])
        writer.writeheader()
        writer.writerows(rejected_row)
    log_events("pipeline.log","INFO","Loaded {} clean rows".format(len(clean_rows)))
    log_events("pipeline.log","INFO","Loaded {} rejected rows".format(len(rejected_row)))
    print("LOAD COMPLETED")


def summary(start_time,rows,clean_rows,rejected_row):
    total_revenue=0
    for row in clean_rows:
        total_revenue+=row["total_price"]
    end_time=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    report={
        "pipeline_start":start_time,
        "pipeline_end":end_time,
        "total_extracted":len(rows),
        "total_loaded":len(clean_rows),
        "total_rejected":len(rejected_row),
        "total_revenue":total_revenue
    }
    with open("pipeline_summary.json","w") as file:
        json.dump(report,file,indent=4)
    log_events("pipeline.log","INFO","PIPELINE COMPLETED")
    print("\nPIPELINE SUMMARY\n")
    print("TOTAL EXTRACTED:",report["total_extracted"])
    print("TOTAL LOADED:",report["total_loaded"])
    print("TOTAL REJECTED:",report["total_rejected"])
    print("TOTAL REVENUE GENERATED:",report["total_revenue"])
    return report




start_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
create_csv("raw_sales.csv")
rows = extract("raw_sales.csv")
clean_rows, rejected_row = transform("raw_sales.csv")
load(clean_rows, rejected_row)
summary(start_time, rows, clean_rows, rejected_row)