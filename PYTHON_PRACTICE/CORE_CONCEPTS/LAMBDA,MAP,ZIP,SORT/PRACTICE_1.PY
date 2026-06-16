# ============================================
# PRACTICE - DAY 15
# Topic: Lambda, Map, Filter, Zip
# Date: 15 June 2026
# ============================================

# QUESTION 1 - Easy — Lambda Basics
# Create lambda functions for:
# - Square of a number
# - Cube of a number
# - Check if a number is even (returns True/False)
# - Convert celsius to fahrenheit: (c * 9/5) + 32
#
# Test each lambda with 2-3 values.
# Print results.

# YOUR CODE HERE:

square=lambda x : x*x 
print(square(5))
print(square(8))

cube=lambda y: y*y*y
print(cube(3))
print(cube(4))

check_even= lambda num : True if num%2==0 else False
print(check_even(2))
print(check_even(9))

convert= lambda temp : (temp * 9/5) + 32
print(convert(0))
print(convert(22))

# ============================================

# QUESTION 2 - Easy — Map
# You have this list:
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# Using map():
# - Square all numbers
# - Convert all numbers to strings
# - Multiply all numbers by 10
#
# You have this list:
names = ["shikhar", "rahul", "prakhar", "aditya"]
# - Capitalize all names using map()
#
# Print all results as lists.

# YOUR CODE HERE:
solution = list(map((lambda num : str(num*num*10)),numbers))
print(solution)

capital= list(map(lambda ch: ch.upper(),names))
print(capital)

# ============================================

# QUESTION 3 - Easy — Filter
# Using the same numbers list above:
# - Filter only even numbers
# - Filter only numbers greater than 5
# - Filter only numbers divisible by 3
#
# Using this list:
words = ["python", "data", "engineering",
         "sql", "pandas", "spark", "ai"]
# - Filter words longer than 4 characters
# - Filter words that start with "p"
#
# Print all results as lists.

# YOUR CODE HERE:
filter1= list(filter(lambda num : num % 2 ==0 ,numbers))
print(filter1)

filter2 = list(filter(lambda num : num > 5 , numbers))
print(filter2)

filter3 = list(filter(lambda num : num % 3==0 , numbers))
print(filter3) 

filter4= list(filter(lambda char : len(char)>4,words))
print(filter4)
# ============================================

# QUESTION 4 - Medium — Zip
# You have:
student_names = ["Shikhar", "Rahul", "Priya",
                 "Aditya", "Sneha"]
student_marks = [92, 45, 78, 33, 88]
student_colleges = ["PSIT", "MAIT", "PSIT",
                    "DTU", "PSIT"]
#
# Using zip():
# - Combine names and marks into a list of tuples
# - Combine all three into a list of tuples
# - Create a list of dictionaries using zip:
#   [{"name": "Shikhar", "marks": 92, "college": "PSIT"}...]
# - Find the student with highest marks using zip
#
# Print all results.
# YOUR CODE HERE:
NamesMarks= zip(student_names,student_colleges)
print(list(NamesMarks))

Result=zip(student_names,student_marks,student_colleges)
print(list(Result))

students = [
    {
        "name": name,
        "marks": marks,
        "college": college
    }
    for name, marks, college in zip(student_names,student_marks,student_colleges)
]


print("\nStudent Dictionaries:")
print(students)

maximum_marks = max(zip(student_names,student_marks,student_colleges),key=lambda student : student[1])
print("\n TOP STUDENTS ")
print(maximum_marks)
# ============================================

# QUESTION 5 - Medium — Combining All Four
# You have this employee data:
employees = [
    {"name": "Shikhar", "salary": 90000,
     "department": "Data"},
    {"name": "Rahul", "salary": 45000,
     "department": "IT"},
    {"name": "Priya", "salary": 120000,
     "department": "Data"},
    {"name": "Aditya", "salary": 30000,
     "department": "HR"},
    {"name": "Sneha", "salary": 95000,
     "department": "Data"},
    {"name": "Karan", "salary": 60000,
     "department": "IT"},
]
# Using map, filter, lambda, zip — NOT list comprehensions:
# - Get names of all Data department employees
#   using filter() + lambda
# - Give every Data employee a 10% raise
#   using map() + lambda
# - Get (name, salary) tuples for employees
#   earning above 60000 using filter() + zip()
# - Get just the salaries as a list using map()
#
# Print all results.

# YOUR CODE HERE:
data_employees =  filter((lambda emp : emp["department"]=="Data" , employees))
data_employees_name= list((map(lambda emp : emp["name"] , data_employees)))
print("EMPLOYEES OF DATA DEPARTMENT : ", data_employees_name)


raise_salary= list(map(lambda emp :{ **emp  , "salary": emp["salary"]*1.10} if emp["department"]=="Data " else emp , employees))
print("SALARY WITH RAISE OF 10% IS :",raise_salary)

high_earners = list(filter(lambda pair: pair[1] > 60000,zip(map(lambda emp: emp["name"], employees),map(lambda emp: emp["salary"], employees))))
print(high_earners)

salaries = list(map( lambda emp : emp["salary"] , employees))
print(salaries)
# ============================================

# QUESTION 6 - Hard — DE Real World
# You have raw pipeline data:
pipeline_data = [
    {"table": "users", "rows": "15420",
     "status": "success", "duration": "12.5"},
    {"table": "orders", "rows": "abc",
     "status": "failed", "duration": "0"},
    {"table": "products", "rows": "8930",
     "status": "success", "duration": "8.2"},
    {"table": "payments", "rows": "-500",
     "status": "success", "duration": "15.1"},
    {"table": "inventory", "rows": "22100",
     "status": "success", "duration": "20.3"},
    {"table": "returns", "rows": "1200",
     "status": "failed", "duration": "3.1"},
]
# Using map, filter, lambda, zip:
# - Filter only successful pipeline runs
# - Filter runs where rows is a valid positive number
#   use a helper function for validation
# - Map rows and duration to integers/floats
#   for valid runs only
# - Calculate total rows processed using map + sum
# - Create a summary list of tuples:
#   (table, rows, duration) for successful valid runs
# - Find the longest running table using max() + lambda
# Print all results.
# YOUR CODE HERE:

successful_pipeline = list(filter(lambda pipe: pipe["status"] == "success",pipeline_data))
print("THE SUCCESSFULL PIPELINES IN THE GIVEN TABLES ARE  :",successful_pipeline)

positive_pipeline = list(filter(lambda pipe: pipe["rows"].lstrip("-").isdigit() and int(pipe["rows"]) > 0 ,pipeline_data))
print("POSITIVE PIPLELINES ARE : ",positive_pipeline)


converted_runs = list(map(lambda pipe: {**pipe,"rows": int(pipe["rows"]),"duration": float(pipe["duration"])},positive_pipeline))
print("\nConverted Runs:")
print(converted_runs) 


total_rows = sum(map(lambda pipe: pipe["rows"],converted_runs))
print(total_rows)

summary_list=  zip(
    map(lambda pipe : pipe["table"],converted_runs),
    map(lambda pipe : pipe["rows"],converted_runs),
    map(lambda pipe : pipe["duration"],converted_runs))   
            
print(list(summary_list))



longest_running = max(converted_runs,key=lambda pipe: pipe["duration"])

print("\nLongest Running Table:")
print(longest_running)
