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
def write_json(filename, data):
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)
    print("JSON written successfully")

def read_json(filename):
    try:
        with open(filename, "r") as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print("File not found:", filename)
    except json.JSONDecodeError:
        print("Invalid JSON format")

data = {
    "students": [
        {
            "name": "Shikhar",
            "college": "PSIT",
            "marks": 99
        },
        {
            "name": "Rahul",
            "college": "MAIT",
            "marks": 85
        }
    ]
}


write_json("students.json", data)
result = read_json("students.json")
print(result)
# ============================================

