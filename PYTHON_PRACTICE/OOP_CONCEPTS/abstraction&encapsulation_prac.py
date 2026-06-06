# ============================================
# OOP PRACTICE - DAY 9
# Topic: Encapsulation + Abstraction
# Date: 6 June 2026
# ============================================

# QUESTION 1 - Encapsulation Easy
# Create a class BankAccount with:
# - Private attribute: __balance
# - Private attribute: __pin
# - __init__ sets both
# - @property balance that returns __balance
# - Method deposit(amount) that adds to __balance
# - Method withdraw(amount, pin) that:
#       checks if pin matches __pin
#       if yes: checks if enough balance
#               if yes: subtracts and prints new balance
#               if no: prints "Insufficient funds"
#       if no: prints "Wrong PIN"
# - No direct access to __balance or __pin from outside
#
# Create 1 account with balance 50000 and pin 1234.
# Deposit 20000.
# Withdraw 10000 with correct pin.
# Withdraw 5000 with wrong pin.
# Try accessing __balance directly — observe the error.
# Access balance through the property instead.

# YOUR CODE HERE:
class BankAccount:
    def __init__(self,balance,pin):
        self.__balance=balance
        self.__pin=pin
    @property
    def balance(self):
        return "BANK BALANCE IS : ",self.__balance
    
    def deposit(self,amount):
        self.__balance+=amount

    def withdraw(self,amount,pin):
        if self.__pin==pin:
            if self.__balance>amount:
                self.__balance-=amount
                print("{} IS WITHDRAWN FROM THE BANK".format(amount))
                print("THE REMAINING BALANCE IS : {}".format(self.__balance))
            else:print("NOT SUFFICIENT BANK BALANCE ")
        else:print("WRONG PIN ...TRY AGAIN...")

balance1=BankAccount(50000,1234)
balance1.deposit(20000)
balance1.withdraw(5000,1234)
print(balance1.balance)
# ============================================

# QUESTION 2 - Encapsulation Medium
# Create a class Student with:
# - Private: __name, __age, __marks
# - @property for each — name, age, marks
# - @name.setter that validates:
#       name cannot be empty string
# - @age.setter that validates:
#       age must be between 5 and 30
# - @marks.setter that validates:
#       marks must be between 0 and 100
# - Regular method display() that prints all three
#
# Create 1 Student.
# Try setting invalid age — should print error message
# Try setting invalid marks — should print error message
# Try setting invalid name — should print error message
# Set all valid values and display.

# YOUR CODE HERE:
class Student:
    def __init__(self,name,age,marks):
        self.__name=name
        self.__age=age
        self.__marks=marks
    @property
    def name(self):
        return "NAME IS : {}".format(self.__name)
    @property
    def age(self):
        return "THE AGE IS : {}".format(self.__age)
    @property
    def marks(self):
        return "THE MARKS ARE : {}".format(self.__marks)
    
    @name.setter
    def name(self,name):
        if len(name==0):
            raise ValueError("NAME CANNOT BE BLANK ... TRY AGAIN ..")
        self.__name=name
    
    @age.setter
    def age(self,value):
        if 5<=value<=30:
            self.__age=value
        else:
            raise ValueError("INVALID AGE ...")
    

    @marks.setter
    def marks(self,value):
        if 0<=value<=100:
            self.__marks=value
        else: 
            raise ValueError("MARKS ENTERED ARE INVALID ...TRY AGAIN...")
    
    def display(self):
        print("{} IS {} YEARS OLD AND HAS SCORED {} MARKS".format(self.__name , self.__age  , self.__marks))



student=Student("SHIKHAR", 20 , 99)   # invalid
student.display()
# ============================================

# QUESTION 3 - Abstraction Easy
# Create an abstract class Shape with:
# - Abstract method area() 
# - Abstract method perimeter()
# - Regular method describe() that prints:
#   "This shape has area X and perimeter Y"
#   where X and Y come from area() and perimeter()
#
# Create 3 concrete classes:
#
# Circle(Shape) with:
# - Attribute: radius
# - Implement area() → 3.14 * radius ** 2
# - Implement perimeter() → 2 * 3.14 * radius
#
# Rectangle(Shape) with:
# - Attributes: length, width
# - Implement area() → length * width
# - Implement perimeter() → 2 * (length + width)
#
# Triangle(Shape) with:
# - Attributes: a, b, c (three sides)
# - Attribute: height
# - Implement area() → 0.5 * base * height (use a as base)
# - Implement perimeter() → a + b + c
#
# Create 1 object of each.
# Call describe() on all three.

# YOUR CODE HERE:
from abc import ABC , abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass

    def describe(self):
        print("THIS SHAPE HAS {} AREA AND {} PERIMETER ".format(self.area(),self.perimeter()))


class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
    

    def area(self):
        return 3.14 * self.radius ** 2
    
    def perimeter(self):
        return 2 * 3.14 * self.radius
    
class Rectangle(Shape):
    def __init__(self,length,width):
        self.length=length
        self.width=width

    def area(self):
        return 2 * self.length * self.width
    
    def perimeter(self):
        return 2 * (self.length + self. width)
    

class Triangle(Shape):

    def __init__(self, a, b, c, height):
        self.a = a
        self.b = b
        self.c = c
        self.height = height

    def area(self):
        return 0.5 * self.a * self.height

    def perimeter(self):
        return self.a + self.b + self.c


circle = Circle(5)
rectangle = Rectangle(10, 5)
triangle = Triangle(6, 8, 10, 4)
circle.describe()
rectangle.describe()
triangle.describe()
# ============================================

# QUESTION 4 - Abstraction + Encapsulation Combined
# Create an abstract class Vehicle with:
# - Abstract method start_engine()
# - Abstract method stop_engine()
# - Regular method status() that prints:
#   "Engine started: True/False"
#
# Create 2 concrete classes:
#
# Car(Vehicle) with:
# - Private attribute: __engine_on = False
# - Implement start_engine():
#       sets __engine_on to True
#       prints "Car engine started"
# - Implement stop_engine():
#       sets __engine_on to False
#       prints "Car engine stopped"
# - Override status() to print:
#   "Car engine on: True/False"
#
# Bike(Vehicle) with:
# - Private attribute: __engine_on = False
# - Implement start_engine():
#       sets __engine_on to True
#       prints "Bike engine started"
# - Implement stop_engine():
#       sets __engine_on to False
#       prints "Bike engine stopped"
# - Override status() to print:
#   "Bike engine on: True/False"
#
# Create 1 Car and 1 Bike.
# Start both engines.
# Print status of both.
# Stop both engines.
# Print status of both again.

# YOUR CODE HERE:

from abc import ABC, abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass
    @abstractmethod
    def stop_engine(self):
        pass
    def status(self):
        pass

class Car(Vehicle):
    def __init__(self):
        self.__engine_on = False
    def start_engine(self):
        self.__engine_on = True
        print("Car engine started")
    def stop_engine(self):
        self.__engine_on = False
        print("Car engine stopped")
    def status(self):
        print("Car engine on:", self.__engine_on)

class Bike(Vehicle):
    def __init__(self):
        self.__engine_on = False
    def start_engine(self):
        self.__engine_on = True
        print("Bike engine started")
    def stop_engine(self):
        self.__engine_on = False
        print("Bike engine stopped")
    def status(self):
        print("Bike engine on:", self.__engine_on)

car1 = Car()
bike1 = Bike()
car1.start_engine()
bike1.start_engine()
car1.status()
bike1.status()
car1.stop_engine()
bike1.stop_engine()
car1.status()
bike1.status()