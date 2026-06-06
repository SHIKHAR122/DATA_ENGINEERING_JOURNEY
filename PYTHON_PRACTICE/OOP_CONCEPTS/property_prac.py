# ============================================
# OOP PRACTICE - DAY 7
# Topic: @property
# Date: 2 June 2026
# ============================================

# QUESTION 1 - Easy
# Create a class Circle with:
# - Attribute: radius
# - @property method area that returns 3.14 * radius ** 2
# - @property method circumference that returns 2 * 3.14 * radius
#
# Create 2 Circle objects with different radii.
# Access area and circumference like attributes — no parentheses.
# Print both for each object.

# YOUR CODE HERE:
class Circle:
    def __init__(self,radius):
        self.radius=radius

    @property
    def area(self):
        return 3.14*self.radius**2
    @property
    def circum(self):
        return 2 * 3.14 * self.radius **2
c1=Circle(2)
c2=Circle(3)
print(c1.area)
print(c1.circum)
print(c2.area)
print(c2.circum)


# =====================================================================================================

# QUESTION 2 - Medium
# Create a class Employee with:
# - Attributes: first_name, last_name, salary
# - @property fullname that returns "first_name last_name"
# - @property annual_salary that returns salary * 12
# - @fullname.setter that:
#       takes a full name string like "Shikhar Sharma"
#       splits it and updates first_name and last_name
#
# Create 1 Employee object.
# Print fullname and annual_salary as attributes.
# Change fullname using the setter.
# Print fullname again — should reflect the change.

# YOUR CODE HERE:
class Employee:
    def __init__(self,first_name,last_name, salary):
        self.first_name=first_name
        self.last_name=last_name
        self.salary=salary
    @property
    def f_name(self):
        return ("{}  {}".format(self.first_name,self.last_name))
    @property
    def annual_salary(self):
        return self.salary*12
    
    @f_name.setter
    def f_name(self,name):
        self.first_name , self.last_name = name.split(" ")

emp1=Employee("SHIKHAR","SHARMA",2100000) 
print(emp1.first_name)
print(emp1.salary)
print(emp1.annual_salary)
print(emp1.f_name)
emp1.f_name="SHIVAM YADAV"
print(emp1.f_name)
# ====================================================================================================

# QUESTION 3 - Medium
# Create a class Temperature with:
# - Store temperature internally in Celsius using _celsius
# - @property celsius that returns _celsius
# - @celsius.setter that:
#       validates the value — if below -273.15 (absolute zero)
#       raise a ValueError: "Temperature below absolute zero"
#       otherwise set _celsius
# - @property fahrenheit that converts and returns:
#       (_celsius * 9/5) + 32
# - @property kelvin that returns:
#       _celsius + 273.15
#
# Create 1 Temperature object with 25 degrees.
# Print celsius, fahrenheit and kelvin as attributes.
# Change celsius to 100 using the setter.
# Print all three again.
# Try setting celsius to -300 — should raise ValueError.
# YOUR CODE HERE:
class Temperature:
    def __init__(self,celcius):
        self.celcius=celcius
    @property
    def celcius(self):
        return self._celcius
    
    @celcius.setter
    def celcius(self, value):
        if value < -273.15:
            raise ValueError("Temperature below absolute zero")
        self._celcius = value

    @property
    def fahr(self):
        return (self._celcius * 9/5) + 32
    @property
    def kelvin(self):
        return (self._celcius+273.15)
temp=Temperature(25)
print(temp.celcius)
print(temp.fahr)
print(temp.kelvin)
temp.celcius=100
print(temp.celcius)
print(temp.fahr)
print(temp.kelvin)
# temp.celcius=-500      #it raises ValueError 

# =========================================================================================================

# QUESTION 4 - Harder
# Create a class BankAccount with:
# - Store balance internally as _balance
# - Attribute: owner
# - @property balance that returns _balance
# - @balance.setter that:
#       validates — balance cannot be negative
#       if negative: print "Invalid balance" and don't update
#       otherwise update _balance
# - @property status that returns:
#       "Rich" if balance >= 100000
#       "Moderate" if balance >= 10000
#       "Low" if balance < 10000
# - Regular method deposit(amount) that adds to _balance
# - Regular method withdraw(amount) that:
#       checks if amount <= _balance
#       if yes: subtracts and prints new balance
#       if no: prints "Insufficient funds"
#
# Create 1 BankAccount with balance 50000.
# Print balance and status.
# Deposit 60000 — print balance and status again.
# Withdraw 20000 — print balance and status.
# Try setting balance to -5000 — should print invalid.
# Try withdrawing 200000 — should print insufficient funds.

# YOUR CODE HERE:
class BankAccount:
    def __init__(self,balance,owner):
        self.balance=balance
        self.owner=owner
    @property
    def balance(self):
        return self._balance
    @balance.setter
    def balance(self,value):
        if value<0:
            raise ValueError("INVALID BALANCE")
        else:
            self._balance=value
    @property
    def status(self):
            if self._balance >= 100000:
             return "RICH"
            elif self._balance >= 10000:
                return "MODERATE"
            else:
                return "LOW"         
    def deposit(self,amount):
        self.balance+=amount

    def withdraw(self,amount):
        if  amount<=self.balance:
            self.balance=self.balance-amount
        else:
            print("INSUFFICIENT BALANCE")
            

    
ba=BankAccount(50000,"SHIKHAR")
print(ba.balance)
print(ba.status)
ba.deposit(60000)
print(ba.balance)
print(ba.status)
ba.withdraw(200000)
print(ba.balance)
try:
    ba.balance = -5000
except ValueError as e:
    print(e)

