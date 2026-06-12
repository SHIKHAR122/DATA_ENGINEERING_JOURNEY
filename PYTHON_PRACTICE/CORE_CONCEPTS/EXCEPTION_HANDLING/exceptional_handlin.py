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
def function(a , b):
    try:
        result= a / b
        print(result)

    except ZeroDivisionError:
        print("Cannot divide by Zero")

    except TypeError:
        print("Invalid input — numbers only")

    finally:
        print("Division attempted")

function(10,2)
function(10,0)
function("10" , 2)
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
def get_elements(lst , index):
    try:
        print(lst[index])
    except IndexError:
        print("Index Out of Range")
    except TypeError:
        print("Index must be an integer")
    finally:
        print("Operation complete")
get_elements([1, 2, 3], 1)

get_elements([1, 2, 3], 10)

get_elements([1, 2, 3], "one")
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
def read_age(value):
    try:
        try:
            age = int(value)
        except ValueError:
            raise ValueError("Age must be number ")
        
        if age <0 or age>120:
            raise ValueError("Age out of valid range")
        print("Valid age : {}".format(age))

    except ValueError as e  :
        print(e)
    
    finally:
        print("Age validation complete ")

read_age("25")    
read_age("abc")   
read_age("-5")    
read_age("150")    
       
    

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
class InsufficientFundsError(Exception):
    def __init__(self,amount,balance):
        self.amount=amount
        self.balance=balance
        super().__init__("CANNOT WITHDRAW {} AVAILABLE BALANCE {}".format(self.amount , self.balance))

class BankAccount:
    def __init__(self,balance):
        self.balance=balance
    
    def withdraw(self,amount):
        if amount>self.balance:
            raise InsufficientFundsError(amount,self.balance)
        else:
            self.balance-=amount
            print("NEW BALANCE: {}".format(self.balance))
account=BankAccount(50000)
try:
    account.withdraw(10000)
    account.withdraw(99999)
except InsufficientFundsError as e:
    print(e)
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
class InvalidGradeException(Exception):
    def __init__(self,subject,grade):
        super().__init__("INVALID GRADES {} FOR SUBJECT {}".format(grade,subject))



class GradeBook:
    def __init__(self,student_name):
        self.student_name=student_name
        self.grades={}
        
    def add_grade(self,subject,grade):
        if grade<0 or grade>100:
            raise InvalidGradeException(grade,subject)
        
            self.grades[subject]=grade
    def get_grade(self , subject):
        if subject not in self.grades:
            raise KeyError("Subject not found....")
    def average(self ):
        if len(self.grades)==0:
            raise ValueError("No Grades Available")
        else: avg =sum(self.grades.values())/len(self.grades) 
        return round(avg,2)

gb=GradeBook("shikhar")
try:
    print(gb.average())
except ValueError as e:
    print(e)

try:
    gb.add_grade("MATHS", 1290)
except InvalidGradeException as e:
    print(e)

gb.add_grade("Maths", 95)

gb.add_grade("Physics", 88)

gb.add_grade("Chemistry", 92)

print("Maths Grade:", gb.get_grade("Maths"))

print("Average:", gb.average())
# ============================================
# EXCEPTION HANDLING EXTRA PRACTICE
# Date: 7 June 2026
# ============================================

# QUESTION A
# Create custom exception: NegativeValueError(Exception)
# Create a class Inventory with:
# - Attribute: items — empty dict
# - Method add_item(name, quantity) that:
#       raises NegativeValueError if quantity < 0
#       with message "Quantity cannot be negative: X"
#       otherwise adds to items dict
# - Method remove_item(name, quantity) that:
#       raises KeyError if item not in inventory
#       raises NegativeValueError if quantity > available
#       with message "Not enough stock for name"
#       otherwise reduces quantity
# - Method display() that prints all items
#
# Test all error cases plus valid cases.

# YOUR CODE HERE:
class NegativeValueException(Exception):
    def __init__(self,quantity):
        super().__init__("QUANTITY CANNOT BE NEGATIVE :{}".format(quantity))
class Inventory:
    def __init__(self,items):
        self.items={}
    def add_items(self , name,quantity):
        if quantity<0:
            raise NegativeValueException(quantity)
        else: self.items[name]=quantity

    def remove_item(self,name,quantity):
        if name not in self.items:
            raise  KeyError("{} NOT FOUND IN THE INVENTORY ".format(name))
        if quantity>self.items[name]:
            raise  NegativeValueException("NOT ENOUGH STOCK FOR {}".format(name))
        else : self.items[name]-=quantity
    def display(self):
        for item , quantity in self.items.items():
            print("{} : {}".format(item, quantity))

inventory = Inventory()

try:

    inventory.add_item("Laptop", 10)

    inventory.add_item("Mouse", 20)

    inventory.remove_item("Laptop", 5)

    inventory.display()

except NegativeValueException as e:

    print(e)

except KeyError as e:

    print(e)