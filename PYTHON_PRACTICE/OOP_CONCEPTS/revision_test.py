# ============================================
# OOP REVISION TEST
# Date: 2 June 2026
# ============================================

# CODING QUESTION 1
# Create a class Hospital with:
# - Class variable: hospital_name = "AIIMS"
# - Class variable: patient_count = 0
# - Attributes: patient_name, age, disease
# - __init__ increments patient_count every time
#   a new patient is admitted
# - @property full_details that returns:
#   "patient_name | age years old | disease"
# - @classmethod change_hospital(cls, name)
#   that updates hospital name
# - @classmethod get_patient_count(cls)
#   that prints total patients admitted
# - @staticmethod is_valid_age(age)
#   returns True if 0 <= age <= 120
# - Regular method display() that prints
#   hospital_name and full_details
#
# Create 3 patients — validate age before creating each.
# Print patient count.
# Change hospital name to "PGI".
# Display all 3 patients — all should show PGI.

# YOUR CODE HERE:
class Hospital:
    hospital_name="AIIMS"
    patient_count=0
    def __init__(self,patient_name, age, disease):
        self.patient_name=patient_name
        self.age=age
        self.disease=disease
        Hospital.patient_count+=1
    @property
    def details(self):
        return ("{} | {} years old | {}".format(self.patient_name,self.age,self.disease))
    

    @classmethod
    def change_hospital(cls, name):
        cls.hospital_name=name

    @classmethod
    def get_patient_count(cls):
        print("TOTAL PATIENTS ADMITTED IN THE HOSPITALS ARE {}".format(cls.patient_count))

    @staticmethod
    def is_valid_age(age):
        if age >=0 or age<=120:
            return True 
        else: return False
    def display(self):
        print("HOSPITAL NAME IS {} AND THE DETAILS OF THE PATIENT ARE :{} | {} YEARS OLD | {} IS THE DISEASE".format(self.hospital_name,self.patient_name,self.age,self.disease))


pt1=Hospital("SHIKHAR", 21 , "TYPHOID")
pt2=Hospital("JESSE", 45, "TB")
pt3=Hospital("NICHOLAS",36,"ASTHMA")
Hospital.get_patient_count()
Hospital.change_hospital("PGI")
pt1.display()
pt2.display()
pt3.display()

# ============================================


# CODING QUESTION 2
# Create a 3 level inheritance chain:
#
# Vehicle with:
# - Attributes: brand, speed using **kwargs
# - Method describe() that prints brand and speed
#
# Car(Vehicle) with:
# - Attribute: num_doors using **kwargs
# - Method describe() prints num_doors
#   then calls super().describe()
#
# ElectricCar(Car) with:
# - Attribute: battery using **kwargs
# - Method describe() prints battery
#   then calls super().describe()
# - @property range_km that returns battery * 6
# - @staticmethod is_eco_friendly() that returns True
#
# Create 1 ElectricCar using all keyword arguments.
# Call describe() — battery → doors → brand and speed order.
# Print range_km as attribute.
# Print is_eco_friendly().

# YOUR CODE HERE:
class Vehicle:
    def __init__(self,brand, speed,**kwargs):
        super().__init__(**kwargs)
        self.brand=brand
        self.speed=speed
        
    def display(self):
        print("THE BRAND IS {} AND THE SPEED IS {}".format(self.brand,self.speed))
    
class  Car(Vehicle):
    def __init__(self,num_doors,**kwargs):
        super().__init__(**kwargs)
        self.num_doors=num_doors
    def display(self):
        super().display()
        print("NUMBER OF DOORS ARE - {}".format(self.num_doors))

class ElectricCar(Car):
    def __init__(self,battery,**kwargs):
        super().__init__(**kwargs)
        self.battery=battery
    def display(self):
        super().display()
        print("THE BATTERY IS :{}".format(self.battery))
    @property
    def range_km(self):
        return self.battery*6
    @staticmethod
    def is_eco_friendly():
        return True
    
ec1=ElectricCar(brand="TESLA",speed="200km/hr",num_doors=4,battery=50)
ec1.display()
print(ec1.range_km)
print(ElectricCar.is_eco_friendly())

# ===========================================

# CODING QUESTION 3
# Create a class Student with:
# - Store marks internally as _marks
# - Attributes: name, college
# - @property marks that returns _marks
# - @marks.setter that validates:
#       marks must be between 0 and 100
#       if invalid: raise ValueError "Invalid marks"
# - @property grade that returns:
#       "A" if marks >= 90
#       "B" if marks >= 75
#       "C" if marks >= 60
#       "D" if marks >= 40
#       "F" if marks < 40
# - @classmethod from_dict(cls, data) that creates
#   a Student from a dictionary:
#   {"name": "Shikhar", "college": "PSIT", "marks": 95}
# - Regular method display() that prints
#   name, college, marks and grade
#
# Create 1 student normally.
# Create 1 student using from_dict.
# Display both.
# Try setting marks to 150 — should raise ValueError.

# YOUR CODE HERE:
class Student:
    def __init__(self,name,college,marks):
        self.marks=marks
        self.name=name
        self.college=college
    @property
    def marks(self):
        return self._marks
    @marks.setter
    def marks(self, marks):
        if 0 <= marks <= 100:
            self._marks = marks
        else:
            raise ValueError("INVALID MARKS")
    @property
    def grade(self):
        if self.marks>=90:
            return "A"
        elif self.marks>=75:
            return"B"
        elif self.marks>=60:
            return "C"
        elif self.marks>=40:
            return "D"
        else: return "F"
    @classmethod
    def from_dict(cls,data):
        name=data["name"]
        college=data["college"]
        marks=data["marks"]
        return cls(name,college,marks)
        
    def display(self):
        print("NAME OF THE STUDENT {} | COLLEGE NAME IS {} |  MARKS ARE {} | AND GRADES ARE {}".format(self.name,self.college,self.marks,self.grade))

st1=Student("ADITYA" , "MAIT"  , 99 )
st2=Student.from_dict({"name": "Shikhar", "college": "PSIT", "marks": 95})
st1.display()
st2.display()


# ============================================

# CODING QUESTION 4
# Create two parent classes:
#
# Flyable with:
# - Attribute: max_altitude using **kwargs
# - Method abilities() that prints max_altitude
#
# Swimmable with:
# - Attribute: max_depth using **kwargs
# - Method abilities() that prints max_depth
#
# Create child class FlyingFish that inherits BOTH:
# - Attribute: name using **kwargs
# - Method abilities() that prints name
#   then calls Flyable.abilities(self)
#   then calls Swimmable.abilities(self)
# - @property description that returns:
#   "name can fly up to max_altitude and swim to max_depth"
#
# Create 1 FlyingFish object.
# Call abilities().
# Print description as attribute.
# Print FlyingFish.__mro__ and write a comment.

# YOUR CODE HERE:
class Flyable:
    def __init__(self,max_altitude,**kwargs):
        super().__init__(**kwargs)
        self.max_altitude=max_altitude

    def abilities(self):
        print("THE MAXIMUM ALTITUDE IS : {}".format(self.max_altitude))

class Swimmable:
    def __init__(self,max_depth,**kwargs):
        super().__init__(**kwargs)
        self.max_depth=max_depth
    def abilities(self):
        print("THE MAXIMUM DEPTH IS : {}".format(self.max_depth))

class FlyingFish(Flyable , Swimmable):
    def __init__(self,name, **kwargs):
        super().__init__(**kwargs)
        self.name=name 
    def abilities(self):
         print("NAME IS {}".format(self.name))
         Flyable.abilities(self)
         Swimmable.abilities(self)
    @property
    def description(self):
        return ("{} CAN FLY UPTO {} AND SWIM UPTO {}".format(self.name , self.max_altitude , self.max_depth))
    
ff1=FlyingFish(name="MARIO" , max_depth=120 , max_altitude=500)
ff1.abilities()
print(ff1.description)
print(FlyingFish.__mro__)


  
# ============================================

# CODING QUESTION 5 — HARDEST
# Create a decorator called 'validate_input' that:
# - Checks if all arguments passed to a function are positive numbers
# - If all positive: runs the function normally
# - If any argument is negative or zero:
#   prints "Invalid input — all values must be positive"
#   and does NOT run the function
#
# Apply it to a function calculate_area(length, breadth)
# that prints length * breadth
#
# Apply it to a function calculate_volume(l, b, h)
# that prints l * b * h
#
# Test with:
# calculate_area(5, 10)      → should work
# calculate_area(-5, 10)     → should print invalid
# calculate_volume(2, 3, 4)  → should work
# calculate_volume(2, -3, 4) → should print invalid

# YOUR CODE HERE:
def validate_input(func):
    def wrapper_function(*args ,**kwargs):
        for value in args:
            if value<=0:
                print("Invalid input — all values must be positive")
                return 
        return func(*args,**kwargs)
    return wrapper_function



@validate_input
def calculate_area(length,breadth,**kwargs):
    print("AREA IS :",length*breadth)

@validate_input
def calculate_volume(l,b,h):
    print("VOLUME IS :",l*b*h)



calculate_area(5, 10)

calculate_area(-5, 10)

calculate_volume(2, 3, 4)

calculate_volume(2, -3, 4)


# BLANK FILE TEST — OOP
# Time limit: 20 minutes
# Rules: No notes, no reference, no Google

# Build the following from scratch:

# 1. A BankAccount class with:
#    - owner name and balance as attributes
#    - deposit() method with validation (no negative deposits)
#    - withdraw() method with validation (no negative balance)
#    - __str__ that prints account details cleanly

# 2. A SavingsAccount that:
#    - inherits from BankAccount
#    - adds an interest_rate attribute
#    - has an apply_interest() method that adds interest to balance
#    - overrides __str__ to include interest rate

# 3. A classmethod on BankAccount that:
#    - creates an account from a dictionary
#    - dict format: {"owner": "Shikhar", "balance": 5000}

# YOUR CODE STARTS BELOW THIS LINE

class BankAccount:
    def __init__(self,name,balance,**kwargs):
        super().__init__(**kwargs)
        self.name=name
        self.balance=balance
    def deposit(self,amount):
        try:
            self.balance+=amount
            print("{} AMOUNT ADDED TO THE BANK ACCOUNT".format(amount))
        except ValueError as e:
            print("NEGATIVE VALUE",e)

    def withdraw(self,amount):
        if amount<0 or amount>self.balance:
            raise ValueError("INSUFFICIENT BALANCE")
        else : self.balance-=amount
        print("{} AMOUNT WITHDRAWED FROM ACCOUNT".format(amount))
    def __str__(self):
        return ("OWNER {}  HAS BALANCE {}".format(self.name,self.balance))
    @classmethod
    def from_dict(cls,data):
        return cls(data["owner"],data["balance"])

class SavingAccount(BankAccount):
    def __init__(self,rate_interest,**kwargs):
        super().__init__(**kwargs)
        self.rate_interest=rate_interest

    def apply_interest(self):
        interest=self.balance*(self.rate_interest/100)
        self.balance+=interest
    def __str__(self):
        return("OWNER : {}  BALANCE {}  ROI {}  ".format(self.name,self.balance,self.rate_interest))

# BankAccount
acc1 = BankAccount("Shikhar", 5000)

acc1.deposit(1000)
acc1.withdraw(2000)

print(acc1)

# SavingsAccount
savings = SavingAccount()

print("\nBefore Interest:")
print(savings)

savings.apply_interest()

print("\nAfter Interest:")
print(savings)

# Classmethod Test
data = {
    "owner": "Aman",
    "balance": 7500
}
acc2 = BankAccount.from_dict(data)

print("\nCreated using classmethod:")
print(acc2)