# ============================================
# OOP PRACTICE - DAY 5
# Topic: **kwargs in Inheritance
# Date: 30 May 2026
# ============================================

# QUESTION 1 - Easy
# Create a parent class Person with:
# - Attributes: name, age
# - Use **kwargs in __init__
# - Method display_info() that prints name and age
#
# Create a child class Student that inherits from Person with:
# - Additional attributes: college, marks
# - Use **kwargs in __init__ and pass remaining kwargs to Person
# - Method display_info() that prints college and marks
#   PLUS calls parent display_info() using super()
#
# Create 1 Student object passing all 4 values as keyword arguments.
# Call display_info() on it.

# YOUR CODE HERE:
class Person:
    def __init__(self,name,age,**kwargs):
        self.name=name
        self.age=age
    def display_info(self):
        print("{} IS  {} YEARS OLD".format(self.name,self.age))


class Student(Person):
    def __init__(self,college,marks,**kwargs):
        super().__init__(**kwargs)
        self.college=college
        self.marks=marks

    def display_info(self):
         super().display_info()
         print("{} IS THE NAME OF THE COLLEGE AND THE MARKS IS : {} ".format(self.college,self.marks))


student1 = Student(college="PSIT",marks=99,name="SHIKHAR",age=20)
student1.display_info()


# ============================================

# QUESTION 2 - Medium
# Create two parent classes:
#
# Vehicle with:
# - Attributes: brand, speed
# - Use **kwargs in __init__
# - Method display_info() that prints brand and speed
#
# Electric with:
# - Attributes: battery_capacity
# - Use **kwargs in __init__
# - Method display_info() that prints battery_capacity
#
# Create a child class ElectricCar that inherits from BOTH:
# - Additional attribute: model
# - Use **kwargs to cleanly initialise all parents
# - Method display_info() that prints everything —
#   call both parent display_info() methods explicitly
#
# Create 1 ElectricCar object passing all values as keyword arguments.
# Call display_info() on it.

# YOUR CODE HERE:
class Vehicle:
    def __init__(self,brand,speed,**kwargs):
        super().__init__(**kwargs)
        self.brand=brand
        self.speed=speed
    def display_info(self):
        print("THE BRAND IS {} AND ITS SPEED IS   {}".format(self.brand,self.speed))

class Electric:
    def __init__(self,battery_capacity,**kwargs):
        super().__init__(**kwargs)
        self.battery_capacity=battery_capacity
    
    def display_info(self):
        print("{} IS THE BATTERY CAPACITY".format(self.battery_capacity))

class Electric_Car(Vehicle,Electric):
    def __init__(self,model,**kwargs):
        super().__init__(**kwargs)
        self.model=model
    def display_info(self):
        Vehicle.display_info(self)
        Electric.display_info(self)
        print("{} IS THE MODEL OF THE CAR".format(self.model))

ec=Electric_Car(brand="TESLA",speed="200km/hr",battery_capacity="50KW",model="MODEL Y")
ec.display_info()


# ============================================

# QUESTION 3 - Harder
# Create three classes:
# Animal with:
# - Attributes: name, age
# - Use **kwargs
# - Method describe() that prints "name is age years old"
#
# Pet with:
# - Attributes: owner
# - Use **kwargs and pass remaining to Animal
# - Method describe() that prints owner PLUS calls Animal.describe()
#
# ServiceAnimal with:
# - Attributes: service_type
# - Inherits from Pet
# - Use **kwargs and pass remaining up the chain
# - Method describe() that prints service_type
#   PLUS calls Pet.describe() using super()
#
# Create 1 ServiceAnimal object.
# Call describe() — output should print:
#   service_type → owner → name and age
#   in that order (child to grandparent)

# YOUR CODE HERE:

class Animal:
    def __init__(self,name,age,**kwargs):
        super().__init__(**kwargs)
        self.name=name
        self.age=age
    def describe(self):
        print("{} IS THE NAME OF THE ANIMAL AND ITS AGE IS : {}".format(self.name,self.age))

class Pet(Animal):
    def __init__(self,owner,**kwargs):
        super().__init__(**kwargs)
        self.owner=owner
    def describe(self):
        super().describe()
        print("{} IS THE OWNER ".format(self.owner))
    
class Service_animal(Pet):
    def __init__(self,service_type,**kwargs):
        super().__init__(**kwargs)
        self.service_type=service_type
    def describe(self):
        super().describe()
        print("{} IS THE SERVICE TYPE ".format(self.service_type))

sa=Service_animal(age=5,name="Buzzo",owner="shikhar",service_type="guard dog")
sa.describe()