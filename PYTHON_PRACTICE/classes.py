# ============================================
# OOP PRACTICE - DAY 1
# Topic: Classes and Objects
# Date: 25 May 2026
# ============================================


# QUESTION 1 
# Create a Student class with the following:
# - Attributes: name, roll_number, marks
# - Method display() that prints all three attributes
# - Method is_passed() that returns True if marks >= 40, False otherwise
# Create 3 student objects with different values
# and print whether each one passed or failed.

# YOUR CODE HERE:

class Student:
    def __init__(self,name,roll_num,marks):
        self.name=name
        self.roll_num=roll_num
        self.marks=marks
    def display(self):
        print("NAME:",self.name)
        print("ROLL NUMBER: ",self.roll_num)
        print("MARKS: ",self.marks)
    def is_passed(self):
        if self.marks>=40:
            return True
        else:
            return False
Student1=Student("SHIKHAR",166,100)
Student2=Student("ADITYA", 109, 89)
Student3=Student("SHIVAM",168,19)
print(Student1.name, Student1.is_passed())
print(Student2.name, Student2.is_passed())
print(Student3.name, Student3.is_passed())     

# ============================================

# QUESTION 2 
# Create an Employee class with the following:
# - Attributes: name, company, salary
# - Method display_info() that prints all details
# - Method appraisal() that increases salary by 10%
#   and prints the new salary
# Create 2 employee objects.
# Give one of them an appraisal and display
# both employees info after.

# YOUR CODE HERE:
class Employee:
    def __init__(self,name,company,salary):
        self.name=name
        self.company=company
        self.salary=salary
    def display_info(self):
        print("EMPLOYEE NAME IS :",self.name)
        print("EMPLOYEE WORKS IN:",self.company)
        print("EMPLOYEE'S SALARY IS : ",self.salary)
    def appraisal(self):
        self.salary = self.salary + (10/100 * self.salary)
        print("THE INCREMENTED SALARY IS:",self.salary)
        print("*******************")
emp1=Employee("shikhar","amazon",90000)
emp2=Employee("atharv","oracle",80000)
emp1.display_info()
emp1.appraisal()
emp2.display_info()
emp2.appraisal()