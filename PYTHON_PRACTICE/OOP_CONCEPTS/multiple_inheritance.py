# ============================================
# OOP PRACTICE - DAY 4
# Topic: Multiple Inheritance
# Date: 29 May 2026
# ============================================

# QUESTION 1 - Easy
# Create two parent classes:
#
# Father with:
# - Attribute: fathers_surname
# - Method skills() that prints "Father is good at cricket"
#
# Mother with:
# - Attribute: mothers_surname
# - Method skills() that prints "Mother is good at painting"
#
# Create a child class Child that inherits from BOTH Father and Mother:
# - Attributes: name + both parents surnames (use super().__init__())
# - Method display() that prints name, fathers_surname, mothers_surname
#
# Create 1 Child object.
# Call skills() — which parent's skills() gets called? note it down.
# Call display().
# Print Child.__mro__ and observe the output.

# YOUR CODE HERE:
class Father:
    def __init__(self,fathers_surname):
        self.fathers_surname=fathers_surname
    def skills(self):
        print("FATHER IS GOOD AT CRICKET")

class Mother:
    def __init__(self,mothers_surname):
        self.mothers_surname=mothers_surname
    def skills(self):
        print("MOTHER IS GOOD AT PAINTING")
    
class child(Father,Mother):
    def __init__(self,fathers_surname,mothers_surname,name):
        Father.__init__(self, fathers_surname)
        Mother.__init__(self, mothers_surname)
        self.name=name
        
    def display_info(self):
        print("NAME OF THE CHILD IS :{} {} {}".format(self.name,self.fathers_surname,self.mothers_surname))

child1=child("Mathew","Jonnes","Gabriel")
child1.skills()
child1.display_info()
  


# ============================================

# QUESTION 2 - Medium
# Create two parent classes:
#
# Flyable with:
# - Method fly() that prints "This object can fly"
#
# Swimmable with:
# - Method swim() that prints "This object can swim"
#
# Create a child class Duck that inherits from BOTH:
# - Attribute: name
# - Method display_abilities() that calls both fly() and swim()
#       using the inherited methods
# - Override fly() to print "Duck flies low"
# - Keep swim() as inherited from Swimmable
#
# Create 2 Duck objects.
# Call display_abilities() on both.
# Call fly() and swim() individually on both.

# YOUR CODE HERE:
class Flyable:
    def fly(self):
        print("THIS OBJECT CAN FLY")

class Swimmable:
    def swim(self):
        print("THIS OBJECT CAN SWIM ")

class Duck(Flyable,Swimmable):    
    def __init__(self,name):
        self.name=name
        
    def fly(self):
        print("DUCK FLIES LOW ")

    def display_abilities(self):
        print("Abilities of", self.name)
        self.fly()
        self.swim()

    
d1=Duck("donald duck")
d2 = Duck("Daisy")

d1.display_abilities()
d2.display_abilities()

d1.fly()
d1.swim()

d2.fly()
d2.swim()
        

# ============================================

# QUESTION 3 - Harder
# Create three classes:
#
# Person with:
# - Attributes: name, age
# - Method display_info() that prints name and age
#
# Employee with:
# - Attributes: company, salary
# - Method display_info() that prints company and salary
#
# Create a child class Manager that inherits from BOTH Person and Employee:
# - Additional attribute: department
# - Use super() properly to initialise both parents
# - Override display_info() to print ALL attributes:
#       name, age, company, salary, department
#       hint: you cannot use super() alone here
#             call Person.display_info(self) and
#             Employee.display_info(self) explicitly
#
# Create 1 Manager object.
# Call display_info() — should print everything.
# Print Manager.__mro__ and write a comment explaining
# the order Python follows.

# YOUR CODE HERE:

class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display_info(self):
        print("EMPLOYEE  NAME IS  {}  AND THEIR AGE IS {} ".format(self.name,self.age))

class Employee:
    def __init__(self,company,salary):
        self.company=company
        self.salary=salary
    def display_info(self):
        print("THE COMPANY NAME IS : {} AND THE SALARY IS : {} ".format(self.company,self.salary))
    

class manager(person,Employee):
    def __init__(self,name,age,company,salary,dept):  
            person.__init__(self, name, age)
            Employee.__init__(self, company, salary)
            self.dept=dept

    def display_info(self):
        person.display_info(self)
        Employee.display_info(self)
        print("THE DEPARTMENT IS {}".format(self.dept))
    
m1=manager("SHIKHAR",20,"GOOGLE",120000,"AI DEPT.")
m1.display_info()
print(manager.__mro__)
