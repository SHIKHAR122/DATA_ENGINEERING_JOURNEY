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





# ============================================
# OOP PRACTICE - DAY 2 - QUESTION 3
# Topic: Classes and Objects
# Date: 26 May 2026
# ============================================

# Create a Library class with the following:
# - Attributes: book_name, author, is_available (True by default)
# - Method display_info() that prints all three attributes
# - Method borrow_book() that:
#       checks if book is available
#       if yes: marks it unavailable and prints "Book borrowed successfully"
#       if no: prints "Sorry, book is not available"
# - Method return_book() that:
#       marks the book as available again
#       prints "Book returned successfully"

# Create 2 book objects.
# Borrow the first book.
# Try borrowing the first book again (should show not available).
# Return the first book.
# Borrow it again (should work now).
# Display info of both books at the end.

# YOUR CODE HERE:
class Library:
    def __init__(self,book_name , author ,is_available=True):
        self.book_name= book_name 
        self.author=author 
        self.is_available=is_available
    def display_info(self):
        print("BOOK NAME IS :",self.book_name)
        print("BOOK'S AUTHOR NAME IS :", self.author)
    def borrow_book(self):
        if self.is_available is True:
            self.is_available=False
            print("Book Borrowed successfully")
        else:
            print("Sorry, Book Not Available ")

    def return_book(self):
        self.is_available = True
        print("Book Returned Successfully")
book1= Library("HAMLET","WILLIAM SHAKESPEARE")
book2=Library("HARRY POTTERS","J.K. ROWLING ")
book1.borrow_book()
book1.borrow_book()
book1.return_book()
book1.borrow_book()
book1.display_info()
# ============================================
# OOP PRACTICE - DAY 2 - QUESTION 4 
# Topic: Classes and Objects
# Date: 26 May 2026
# ============================================

# Create a Cart class for an online shopping cart:
# - Attributes: user_name, items (empty list by default), total_price (0 by default)
# - Method add_item(item_name, price) that:
#       adds item_name to the items list
#       adds price to total_price
#       prints "item_name added to cart"
# - Method remove_item(item_name, price) that:
#       checks if item is in the list
#       if yes: removes it, subtracts price, prints "item_name removed from cart"
#       if no: prints "item_name not found in cart"
# - Method display_cart() that:
#       prints user_name
#       prints all items in the cart
#       prints total price

# Create 1 cart object for yourself.
# Add 3 items with prices.
# Remove 1 item that exists.
# Try removing 1 item that doesn't exist.
# Display the final cart.

# YOUR CODE HERE:
class Cart:
    def __init__(self,user_name, items=[],total_price=0):
        self.user_name=user_name 
        self.items=items
        self.total_price=total_price
    def add_item(self,item_name , price):
        self.price=price
        self.item_name=item_name
        self.items.append(item_name)
        self.total_price+=price
    def remove_item(self, item_name, price):
        if item_name in self.items:
            self.items.remove(item_name)
            self.total_price -= price
            print(f"{item_name} removed from cart")
        else:
            print(f"{item_name} not found in cart")
    def display_cart(self):
        print("USER NAME IS : ",self.user_name)
        print("ITEMS IN THE CART ARE : ",self.items)
        print("THE TOTAL PRICE IS : ",self.total_price) 



my_cart = Cart("Shikhar")
my_cart.add_item("Laptop", 45000)
my_cart.add_item("Mouse", 800)
my_cart.add_item("Keyboard", 1500)
my_cart.remove_item("Mouse", 800)
my_cart.remove_item("Headphones", 2000)
my_cart.display_cart()