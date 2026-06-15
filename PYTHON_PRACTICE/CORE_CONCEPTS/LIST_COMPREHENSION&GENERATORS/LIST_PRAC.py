# ============================================
# PRACTICE - DAY 14
# Topic: List Comprehensions + Generator Expressions
# Date: 14 June 2026
# ============================================

# QUESTION 1 - Easy
# Using list comprehension:
# - Create a list of squares of numbers 1 to 10
# - Create a list of even numbers from 1 to 20
# - Create a list of words in UPPERCASE from:
#   words = ["python", "data", "engineering", "sql"]
# - Create a list of lengths of each word from the same list
#
# Print all four lists.
# No loops allowed — list comprehension only.

# YOUR CODE HERE:
squares=[x*x for x in range(10)]
print(squares)
even_number=[x for x in range(20) if x%2==0]
print(even_number)
words=["python", "data", "engineering", "sql"]
capital_letters=[word.upper() for word in words ]
print(capital_letters)
length=[len(word) for word in words]
print(length)
# ============================================

# QUESTION 2 - Easy
# You have this list of student dictionaries:
students = [
    {"name": "Shikhar", "marks": 92, "college": "PSIT"},
    {"name": "Rahul", "marks": 45, "college": "MAIT"},
    {"name": "Priya", "marks": 78, "college": "PSIT"},
    {"name": "Aditya", "marks": 33, "college": "DTU"},
    {"name": "Sneha", "marks": 88, "college": "PSIT"},
    {"name": "Karan", "marks": 61, "college": "MAIT"},
]
# Using list comprehensions:
# - Get names of all students who scored above 60
# - Get names of all PSIT students
# - Get marks of students who scored below 50
# - Get name and marks as tuples for all students:
#   [("Shikhar", 92), ("Rahul", 45)...]
#
# Print all four results.

# YOUR CODE HERE:
names=[student["name"] for student in students]
print(names )
college=[student["name"] for student in students if student["college"] == "PSIT"]
print(college)
marks=[student["marks"] for student in students if student["marks"]>60]
print(marks)
marks2=[student["name"] for student in students if student["marks"]<60]
print(marks2)
names_tuple=[(student["name"],student["marks"]) for student in students]
print(names_tuple)
# ============================================

# QUESTION 3 - Medium
# You have this raw sales data:
sales = [
    {"product": "Laptop", "price": "65000", "quantity": "2"},
    {"product": "Mouse", "price": "500", "quantity": "abc"},
    {"product": "Keyboard", "price": "-1200", "quantity": "5"},
    {"product": "Monitor", "price": "15000", "quantity": "3"},
    {"product": "Headphones", "price": "3000", "quantity": "-1"},
    {"product": "Webcam", "price": "xyz", "quantity": "4"},
]
# Using list comprehensions:
# - Get all products where price is a valid positive number
#   hint: you'll need a helper function for try/except
#   since you can't use try/except inside comprehension directly
# - Calculate revenue (price * quantity) for valid rows only
# - Get products with invalid price or quantity
#
# Print all three results.

# YOUR CODE HERE:
valid=[sale["product"] for sale in sales if sale["price"].isdigit() and int(sale["price"])>0 ]
print(valid)
revenues = [
    int(sale["price"]) * int(sale["quantity"])
    for sale in sales
    if sale["price"].isdigit()and sale["quantity"].isdigit()and int(sale["price"]) > 0 and int(sale["quantity"]) > 0]

print(revenues)
# ============================================

# QUESTION 4 - Medium
# Using list comprehensions with nested loops:
#
# - Create a multiplication table as a list of tuples:
#   [(1,1,1), (1,2,2), (1,3,3)... (5,5,25)]
#   format: (i, j, i*j) for i in 1-5, j in 1-5
#
# - Flatten this nested list into a single list:
#   matrix = [[1,2,3], [4,5,6], [7,8,9]]
#   result should be: [1,2,3,4,5,6,7,8,9]
#
# - Create pairs of (student_name, subject) for all
#   combinations:
#   names = ["Shikhar", "Rahul"]
#   subjects = ["Python", "SQL", "Pandas"]
#   result: [("Shikhar","Python"), ("Shikhar","SQL")...]
#
# Print all three.

# YOUR CODE HERE:

table=[(i,j,i*j)for i in range(1,6) for j in range (1,6)]
print(table)
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flatten=[num for row in matrix for num in row ]
print(flatten)
names = ["Shikhar", "Rahul"]
subjects = ["Python", "SQL", "Pandas"]
result=[(names , subjects)for name in names for subject in subjects]
print(result)

# ============================================

# QUESTION 5 - Medium — Generator Expressions
# - Create a generator that yields squares of 1 to 10
# - Print each value using a for loop
#
# - Create a generator that yields only even numbers
#   from 1 to 20
# - Convert it to a list and print
#
# - Create a generator that reads a large range
#   range(1, 10000000) and yields only multiples of 7
# - Print first 10 values using next() or islice
#   from itertools import islice
#
# Show the memory difference between list and generator:
# import sys
# list_size = sys.getsizeof([x for x in range(10000)])
# gen_size = sys.getsizeof(x for x in range(10000))
# print("List size:", list_size, "bytes")
# print("Generator size:", gen_size, "bytes")

# YOUR CODE HERE:
generator=(x*x for x in range(11))
for num in generator:
    print(num)

even=(x for x in range (1,21) if x%2==0)
even_list=list(even)
print(even_list)
from itertools import islice
large_data=(x for x in range( 1, 10000000) if x%7==0)
print(list(islice(large_data,10)))

def large_data():
    for num in range(1 , 10000000):
        if num%7==0:
            yield num
generate=large_data()
print(list(islice(generate,10)))


import sys
list_size = sys.getsizeof([x for x in range(10000)])
gen_size = sys.getsizeof(x for x in range(10000))
print("List size:", list_size, "bytes")       #85176 bytes
print("Generator size:", gen_size, "bytes")   #192 bytes

# ============================================

# QUESTION 6 - Hard — DE Real World
# You have a large CSV file simulation:
# Use this data generator instead of actual file:
# - Create a generator of valid customers:
#   age between 18 and 60, salary above 0
# - From valid customers, create a generator of
#   Delhi customers only
# - From Delhi customers, calculate average salary
#   using the generator — don't convert to list
# - Count how many valid customers there are
#   without loading all into memory
#
# Print Delhi customer count and average salary.
# Print total valid customer count.

import random
random.seed(42)
large_data = [
    {
        "id": i,
        "name": f"Customer_{i}",
        "age": random.randint(15, 70),
        "salary": random.randint(-5000, 150000),
        "city": random.choice(["Delhi", "Mumbai",
                               "Bangalore", "Kanpur"])
    }
    for i in range(1, 10001)   
]
valid_customer=(customer for customer in large_data if 18<=customer["age"]<=60 and customer["salary"]>0  )

valid_count=0
delhi_count=0
salary_sum=0

for customer in valid_customer:
    valid_count+=1
    if customer["city"]=="Delhi":
        delhi_count+=1
        salary_sum+=customer["salary"]
average_salary=(salary_sum/delhi_count if delhi_count>0 else 0)


print("DELHI CUSTOMERS:", delhi_count)
print("AVERAGE SALARY OF DELHI CUSTOMER IS :", salary_sum)
print("TOTAL VALID CUSTOMERS :", valid_count)


