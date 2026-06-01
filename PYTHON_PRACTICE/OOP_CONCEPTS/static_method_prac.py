# ============================================
# OOP PRACTICE - DAY 7
# Topic: @staticmethod
# Date: 01 JUNE 2026
# ============================================

# QUESTION 1 - Easy
# Create a class MathHelper with:
# - Static method add(a, b) that returns a + b
# - Static method subtract(a, b) that returns a - b
# - Static method multiply(a, b) that returns a * b
# - Static method is_even(n) that returns True if n is even
#
# Call all 4 methods directly on the class.
# No object creation needed.

# YOUR CODE HERE:
class MathHelper:
    @staticmethod
    def add(a,b):
        return a+b

    @staticmethod
    def subtract(a,b):
        return a-b

    @staticmethod
    def multiply(a,b):
        return a*b 

    @staticmethod
    def is_even(n):
        if n%2==0:
            return True 
        else : return False
    
print(MathHelper.add(2,3))
print(MathHelper.subtract(6,4))
print(MathHelper.multiply(3,4))
print(MathHelper.is_even(3))
print(MathHelper.is_even(8))


# ============================================

# QUESTION 2 - Medium
# Create a class Employee with:
# - Attributes: name, age, salary
# - Regular method display_info() that prints all three
# - Static method is_eligible(age) that:
#       returns True if age >= 18
#       returns False otherwise
# - Static method is_valid_salary(salary) that:
#       returns True if salary > 0
#       returns False otherwise
#
# Create 2 Employee objects.
# Before creating check eligibility using is_eligible()
# Before creating check salary using is_valid_salary()
# Print the checks then create the objects and display info.

# YOUR CODE HERE:
class Employee:
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary

    def display_info(self):
        print("THE NAME OF THE EMPLOYEE IS {} AND THEY ARE {} YEARS OLD AND THEY HAVE A MONTHLY WAGE OF {}".format(self.name , self.age,self.salary))

    @staticmethod
    def is_eligible(age):
        if age>18 :
            return True
        else: return False

    @staticmethod
    def is_valid_salary(salary):
        if salary>0:
            return True 
        else : return False

print(Employee.is_eligible(19))
print(Employee.is_valid_salary(10000))
print(Employee.is_eligible(17))
print(Employee.is_valid_salary(0))
emp1=Employee("SHIKHAR", 20 , 190000)
emp2=Employee("ADITYA",21 ,230000)
emp1.display_info()
emp2.display_info()

# ============================================


# QUESTION 3 - Medium
# Create a class DateHelper with:
# - Static method is_leap_year(year) that:
#       returns True if year is divisible by 4
#       AND not divisible by 100
#       OR divisible by 400
# - Static method days_in_month(month, year) that:
#       returns the number of days in that month
#       hint: months with 30 days: 4,6,9,11
#             months with 31 days: all others except february
#             february: 28 days normally, 29 in leap year
#             use is_leap_year() inside this method
#
# Test with:
# is_leap_year(2024) → True
# is_leap_year(2026) → False
# days_in_month(2, 2024) → 29
# days_in_month(2, 2026) → 28
# days_in_month(4, 2026) → 30

# YOUR CODE HERE:
class DateHelper:
    @staticmethod
    def is_leap_year(year):
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            return True 
        else: return False
    
    @staticmethod
    def days_in_month(month, year):
        if month in [4, 6, 9, 11]:
          return 30
        elif month == 2:
            if DateHelper.is_leap_year(year):
              return 29
            else:
             return 28
        else:
           return 31
print(DateHelper.is_leap_year(2024))
print(DateHelper.is_leap_year(2026))
print(DateHelper.days_in_month(2,2024))
print(DateHelper.days_in_month(4,2026))



    

# ============================================

# QUESTION 4 - Harder
# Create a class Student with:
# - Class variable: passing_marks = 40
# - Attributes: name, marks
# - Regular method display_info() that prints name and marks
# - Static method validate_marks(marks) that:
#       returns True if 0 <= marks <= 100
#       returns False otherwise
# - Class method set_passing_marks(cls, new_marks) that:
#       updates passing_marks class variable
# - Regular method is_passed(self) that:
#       returns True if self.marks >= passing_marks
#
# Create 2 Student objects — validate marks before creating.
# Call is_passed() on both.
# Change passing marks to 50 using set_passing_marks().
# Call is_passed() on both again — results may change.

# YOUR CODE HERE:

class Student:
    passing_marks=40
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def display_info(self):
        print("{} is the name and they got {} marks ".format(self.name , self.marks))
    @staticmethod
    def valid_marks(marks):
        if 0 <= marks and marks <= 100:
            return True 
        else : return False
    @classmethod
    def set_passed_marks(cls,new_marks):
        cls.passing_marks=new_marks

    def is_passed(self):
        if self.marks >=self.passing_marks:
            return True 
        else : return False

student1=Student("SHIHKAR", 41)
student2=Student("ADITYA",40)
print(student1.is_passed())
print(student2.is_passed())
Student.set_passed_marks(50)
print(student1.is_passed())
print(student2.is_passed())


    
    
    


