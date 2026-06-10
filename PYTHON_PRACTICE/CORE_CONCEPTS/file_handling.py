# ============================================
# FILE HANDLING PRACTICE - DAY 10
# Date: 09 June 2026
# ============================================

# QUESTION 1 - Easy
# Write a function write_file(filename, content) that:
# - Opens a file in write mode using 'with'
# - Writes the content to it
# - Prints "File written successfully"
#
# Write a function read_file(filename) that:
# - Opens the file in read mode using 'with'
# - Prints the content
# - Catches FileNotFoundError:
#   prints "File not found: filename"
#
# Test with:
# write_file("test.txt", "Hello Shikhar\nDay 10\nFile Handling")
# read_file("test.txt")
# read_file("missing.txt")  → should catch error

# YOUR CODE HERE:
def write_file(filename , content):
    with open(filename,"w") as file:
        file.write(content)
        print("FILE WRITTEN SUCCESSFULLY")
    
def read_file(filename):
    try:
        with open(filename,"r") as readfile:
            readfile.read()
    except FileNotFoundError():
        print("FILE NOT FOUND:", filename)


write_file("test.txt", "Hello Shikhar\nDay 10\nFile Handling")
read_file("test.txt")
# read_file("missing.txt")
# ============================================

# QUESTION 2 - Easy
# Write a function append_to_file(filename, content) that:
# - Opens file in append mode
# - Appends content on a new line
# - Prints "Content appended"
#
# Test with:
# write_file("log.txt", "First line")
# append_to_file("log.txt", "Second line")
# append_to_file("log.txt", "Third line")
# read_file("log.txt")
# Output should show all 3 lines

# YOUR CODE HERE:
def append_function(filename,content):
    with open(filename,"a")as file_append:
        file_append.write("\n" + content)
        print("CONTENT APPENDED")
write_file("log.txt","FIRST LINE")
append_function("log.txt","SECOND LINE")
append_function("log.txt","THIRD LINE")
read_file("log.txt")

# ============================================

# QUESTION 3 - Medium
# Write a function write_csv(filename, data) that:
# - Takes a list of dictionaries like:
#   [{"name": "Shikhar", "age": 20, "marks": 99},
#    {"name": "Rahul", "age": 21, "marks": 85}]
# - Writes it as a proper CSV file with headers
# - Use csv module — import csv
# - Prints "CSV written successfully"
#
# Write a function read_csv(filename) that:
# - Reads the CSV file
# - Prints each row as a dictionary
# - Catches FileNotFoundError
#
# Test with the data above.

# YOUR CODE HERE:

import csv
def write_csv(filename,data ):
    with open(filename,"w",newline="")as file:
        
        writer=csv.DictWriter(file,fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)
    print("CSV WRITTEN SUCCESSFULLY")

def read_csv(filename):
    try:
        with open(filename,"r")as file:
            reader=csv.DictReader(file)
            for row in reader:
                print(dict(row))
    except FileNotFoundError:
        print("FILE NOT FOUND:",filename)

data = [
    {"name": "Shikhar", "age": 20, "marks": 99},
    {"name": "Rahul", "age": 21, "marks": 85}
]


write_csv("students.csv", data)

read_csv("students.csv")
# ============================================

# QUESTION 4 - Medium
# Write a function write_json(filename, data) that:
# - Takes a dictionary or list
# - Writes it as formatted JSON with indent=4
# - Use json module — import json
# - Prints "JSON written successfully"
#
# Write a function read_json(filename) that:
# - Reads and parses the JSON file
# - Returns the data
# - Catches FileNotFoundError
# - Catches json.JSONDecodeError:
#   prints "Invalid JSON format"
#
# Test with:
# data = {
#     "students": [
#         {"name": "Shikhar", "college": "PSIT", "marks": 99},
#         {"name": "Rahul", "college": "MAIT", "marks": 85}
#     ]
# }
# write_json("students.json", data)
# result = read_json("students.json")
# print(result)

# YOUR CODE HERE:
import json
def write_json(filename , content):
    with open(filename , "w") as file:

def read_json(filename):
    with open(filename,"r")as file:
        reader=json.load(file)
        print(data)

# ============================================

# QUESTION 5 - Harder — DE Relevant
# Build a simple logging system:
#
# Write a function log_event(filename, level, message) that:
# - level can be "INFO", "WARNING", "ERROR"
# - Appends to the log file in this format:
#   "2026-06-08 | INFO | Pipeline started"
# - Use datetime module for timestamp:
#   from datetime import datetime
#   timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
# - Catches any file errors
#
# Write a function read_logs(filename, level=None) that:
# - Reads all logs if level is None
# - Filters by level if provided
# - Prints each matching line
#
# Test with:
# log_event("pipeline.log", "INFO", "Pipeline started")
# log_event("pipeline.log", "INFO", "Data loaded: 1000 rows")
# log_event("pipeline.log", "WARNING", "Null values found: 5")
# log_event("pipeline.log", "ERROR", "Database connection failed")
# log_event("pipeline.log", "INFO", "Pipeline completed")
#
# read_logs("pipeline.log")           → all logs
# read_logs("pipeline.log", "ERROR")  → only errors
# read_logs("pipeline.log", "INFO")   → only info logs

# YOUR CODE HERE: