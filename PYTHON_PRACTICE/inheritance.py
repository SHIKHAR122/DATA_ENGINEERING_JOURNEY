# ============================================
# OOP PRACTICE - DAY 3
# Topic: Single Inheritance
# Date: 28 May 2026
# ============================================

# QUESTION 1 - Easy
# Create a parent class Animal with:
# - Attributes: name, age
# - Method speak() that prints "Animal makes a sound"
# - Method display_info() that prints name and age
#
# Create a child class Dog that inherits from Animal with:
# - Additional attribute: breed
# - Override speak() to print "Dog barks"
# - Method fetch() that prints "dog_name is fetching the ball"
#
# Create 2 Dog objects and:
# - Call speak() on both — should print "Dog barks" not "Animal makes a sound"
# - Call display_info() on both — inherited from Animal, should still work
# - Call fetch() on both

# YOUR CODE HERE:
class Animal:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def speak(self):
        print("ANIMAL MAKES A SOUND")
    def display_info(self):
        print("THE NAME OF THE ANIMAL IS :",self.name)
        print("THE AGE OF THE ANIMAL IS : ",self.age)
class Dog(Animal):
    def __init__(self,name,age,breed):
        super().__init__(name,age)
        self.breed=breed
    def speak(self):
        print("DOG BARKS")
    def fetch(self):
        print("{} IS FETCHING THE BALL..".format(self.name))
dog1 =Dog("BUZZO",2,"LABRA")
dog2=Dog("JACK",4,"HUSKY")
dog1.speak()
dog2.speak()
dog1.display_info()
dog2.display_info()
dog1.fetch()
dog2.fetch()

# ============================================

# QUESTION 2 - Medium
# Create a parent class BankAccount with:
# - Attributes: owner, balance
# - Method deposit(amount) that adds to balance and prints new balance
# - Method display_info() that prints owner and balance
#
# Create a child class SavingsAccount that inherits from BankAccount with:
# - Additional attribute: interest_rate (e.g 5 for 5%)
# - Method add_interest() that:
#       calculates interest on current balance
#       adds it to balance
#       prints "Interest added. New balance is: X"
# - Override display_info() to also print interest_rate
#       along with owner and balance
#
# Create 1 SavingsAccount object.
# Deposit some money.
# Add interest.
# Display info.

# YOUR CODE HERE:
class BankAccount:
    def __init__(self,owner,balance):
        self.owner=owner
        self.balance=balance

    def deposit(self,amount):
        self.balance+=amount
        print("{}  IS THE BALANCE".format(self.balance))

    def display_info(self):
        print("{}  IS THE OWNER OF THE ACCOUNT AND THE BALANCE IS {}".format(self.owner,self.balance))


class SavingsAccount(BankAccount):
    def __init__(self,owner,balance,interest_rate):
        super().__init__(owner,balance)
        self.interest_rate=interest_rate


    def add_interest(self):
        interest = (self.balance * self.interest_rate) / 100
        self.balance += interest
        print("Interest added. New balance is:{}".format(self.balance))
    def display_info(self):
        print("THE INTEREST RATE IS : ",self.interest_rate)
        super().display_info()
account1=SavingsAccount("shikhar",10000,5)
account1.deposit(12000)
account1.add_interest()
account1.display_info()

