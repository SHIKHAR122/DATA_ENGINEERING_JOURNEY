# ============================================
# OOP PRACTICE - DAY 9
# Topic: Exception Handling
# Date: 6 June 2026
# ============================================

# QUESTION 1 - Easy
# Write a function divide(a, b) that:
# - Tries to divide a by b
# - If b is 0: catches ZeroDivisionError
#   and prints "Cannot divide by zero"
# - If a or b is not a number: catches TypeError
#   and prints "Invalid input — numbers only"
# - Finally: prints "Division attempted"
#
# Test with:
# divide(10, 2)    → 5.0
# divide(10, 0)    → Cannot divide by zero
# divide("10", 2)  → Invalid input — numbers only

# YOUR CODE HERE:


# ============================================

# QUESTION 2 - Easy
# Write a function get_element(lst, index) that:
# - Tries to return element at given index
# - Catches IndexError if index is out of range
#   prints "Index out of range"
# - Catches TypeError if index is not an integer
#   prints "Index must be an integer"
# - Finally: prints "Operation complete"
#
# Test with:
# get_element([1,2,3], 1)     → 2
# get_element([1,2,3], 10)    → Index out of range
# get_element([1,2,3], "one") → Index must be an integer

# YOUR CODE HERE:


# ============================================

# QUESTION 3 - Medium
# Write a function read_age(value) that:
# - Tries to convert value to integer
# - If conversion fails: raises ValueError
#   "Age must be a number"
# - If age < 0 or age > 120: raises ValueError
#   "Age out of valid range"
# - If valid: prints "Valid age: X"
# - Use try-except-finally
# - Finally prints "Age validation complete"
#
# Test with:
# read_age("25")    → Valid age: 25
# read_age("abc")   → Age must be a number
# read_age("-5")    → Age out of valid range
# read_age("150")   → Age out of valid range

# YOUR CODE HERE:


# ============================================

# QUESTION 4 - Medium
# Create a custom exception class:
# InsufficientFundsError(Exception) with:
# - __init__(self, amount, balance) that:
#   stores both values
#   calls super().__init__ with message:
#   "Cannot withdraw X. Available balance: Y"
#
# Create a BankAccount class with:
# - Attribute: balance
# - Method withdraw(amount) that:
#   raises InsufficientFundsError if amount > balance
#   otherwise subtracts and prints new balance
#
# Test with:
# try:
#     account.withdraw(10000)   → should work
#     account.withdraw(999999)  → should raise custom error
# except InsufficientFundsError as e:
#     print(e)

# YOUR CODE HERE:


# ============================================

# QUESTION 5 - Harder
# Create a custom exception: InvalidGradeError(Exception)
#
# Create a class Gradebook with:
# - Attribute: student_name
# - Attribute: grades — empty dict
# - Method add_grade(subject, grade) that:
#       raises InvalidGradeError if grade < 0 or grade > 100
#       with message "Invalid grade X for subject Y"
#       otherwise adds to grades dict
# - Method get_grade(subject) that:
#       raises KeyError if subject not found
#       otherwise returns the grade
# - Method average() that:
#       raises ValueError if no grades added yet
#       with message "No grades available"
#       otherwise returns average rounded to 2 decimals
#
# Test all three error cases plus valid cases.

# YOUR CODE HERE: