# ============================================
# OOP PRACTICE - DAY 6
# Topic: @classmethod
# Date: 31 May 2026
# ============================================

# QUESTION 1 - Easy
# Create a class Dog with:
# - Class variable: species = "Canis Familiaris"
# - Attributes: name, breed
# - Regular method display_info() that prints name and breed
# - Class method change_species(cls, new_species) that
#   changes the species class variable
#
# Create 2 Dog objects.
# Print species for both before changing.
# Call change_species("Canis Lupus").
# Print species for both after changing.
# Both should reflect the new species.

# YOUR CODE HERE:
class Dog:
    species="Canis Familiaris"
    def __init__(self,name, breed):
        self.name=name
        self.breed=breed
    def display_info(self):
        print("{}  IS THE NAME OF THE DOG AND ITS BREED IS : {} ".format(self.name , self.breed))
    
    @classmethod
    def change_species(cls,new_species):
        cls.species=new_species
dog1=Dog("BUZZO","LABRADOR")
dog2=Dog("JAMES","PITBULL")
Dog.change_species("Canis Lupus")
dog1.display_info()
print(dog1.species)
dog2.display_info()
print(dog2.species)
# ============================================

# QUESTION 2 - Easy
# Create a class Counter with:
# - Class variable: count = 0
# - __init__ that increments count by 1
#   every time a new object is created
# - Class method get_count(cls) that
#   prints "Total objects created: X"
#
# Create 4 Counter objects.
# Call get_count() — should print 4.

# YOUR CODE HERE:
class Counter:
    count=0
    def __init__(self):
        Counter.count+=1
    
    @classmethod
    def get_count(cls):
        print("TOTAL NUMBER OF OBJECTS CREATED IS :{}".format(cls.count))
c1=Counter()
c2=Counter()
c3=Counter()
c4=Counter()
Counter.get_count()
# ============================================

# QUESTION 3 - Medium
# Create a class Student with:
# - Attributes: name, marks
# - Regular method display_info() that prints name and marks
# - Class method from_string(cls, student_string) that:
#   takes a string like "Shikhar-99"
#   splits it by "-"
#   returns a Student object with name and marks
#
# Create 1 Student normally.
# Create 1 Student using from_string("Rahul-85").
# Call display_info() on both.

# YOUR CODE HERE:
class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def display_info(self):
        print(" NAME OF THE STUDENT IS  {} AND THE MARKS THEY SCORED IS {}".format(self.name  , self.marks ))
    

    @classmethod
    def from_string(cls,student_string):
        name , marks = student_string.split("-")
        return cls(name , int(marks))
    
student1=student("SHIKHAR",90)
student2=student.from_string("ABHAY-78")
student1.display_info()
student2.display_info()
# ============================================

# QUESTION 4 - Medium
# Create a class BankAccount with:
# - Class variable: bank_name = "SBI"
# - Attributes: owner, balance
# - Regular method display_info() that prints
#   bank_name, owner and balance
# - Class method change_bank(cls, new_name) that
#   changes the bank_name
# - Class method from_dict(cls, data) that:
#   takes a dictionary like:
#   {"owner": "Shikhar", "balance": 90000}
#   and returns a BankAccount object
#
# Create 1 account normally.
# Create 1 account using from_dict.
# Change bank name to "HDFC".
# Display both accounts — both should show HDFC.

# YOUR CODE HERE:
class BankAccount:
    bank_name="SBI"
    def __init__(self,owner ,balance):
        self.owner=owner
        self.balance=balance
    def display_info(self):
        print("{} IS THE NAME OF THE BANK AND THE CUSTOMER'S NAME IS {} AND THE BALANCE IS {}".format(self.bank_name,self.owner,self.balance))
    
    @classmethod
    def change_bank(cls,new_name):
       cls.bank_name=new_name


    @classmethod
    def from_dict(cls,data):
        owner=data["owner"]
        balance=data["balance"]
        return cls(owner , balance)
BankAccount.change_bank("HDFC")
acc1=BankAccount("SHIKHAR SHARMA", 9000000)
acc2=BankAccount.from_dict({"owner": "RAHUL", "balance": 50000})
acc1.display_info()
acc2.display_info()
# ============================================

# QUESTION 5 - Harder
# Create a class Employee with:
# - Class variable: company = "Google"
# - Class variable: employee_count = 0
# - Attributes: name, salary
# - __init__ increments employee_count by 1
#   every time a new object is created
# - Regular method display_info() that prints
#   name, salary and company
# - Class method from_string(cls, emp_string) that:
#   takes a string like "Shikhar-90000"
#   and returns an Employee object
# - Class method get_employee_count(cls) that
#   prints "Total employees: X"
# - Class method change_company(cls, new_company)
#   that changes the company name
#
# Create 2 employees normally.
# Create 1 employee using from_string("Rahul-75000").
# Call get_employee_count() — should print 3.
# Change company to "Amazon".
# Display all 3 employees — all should show Amazon.

# YOUR CODE HERE:
class Employee:
    company="GOOGLE"
    employee_count=0
    def __init__(self , name , salary):
        self.name=name
        self.salary=salary
        Employee.employee_count+=1
    def display_info(self):
        print("{} IS THE NAME OF THE EMPLOYEE , THEY WORK AT  {} AND THEY EARN {}".format(self.name , self.company , self.salary))
    
    @classmethod
    def get_employee_count(cls):
        print("TOTAL EMPLOYEES ARE {}".format(cls.employee_count))
    
    @classmethod
    def change_company(cls,new_company):
        cls.company=new_company

    @classmethod
    def from_string(cls,emp_string):
        name , salary = emp_string.split("-")
        return cls(name ,salary)

emp1=Employee("SHIKHAR" , 900000)
emp2=Employee("ADITYA", 700000)
emp3=Employee.from_string("RAHUL-75000")
emp4=Employee.from_string("ABHAY-60000")
Employee.change_company("AMAZON")
emp1.display_info()
emp2.display_info()
emp3.display_info()
emp4.display_info()
Employee.get_employee_count()



