# ============================================
# OOP PRACTICE - DAY 6
# Topic: Decorators
# Date: 31 May 2026
# ============================================

# QUESTION 1 - Easy
# Create a decorator called 'logger' that:
# - Prints "Function is starting..." before the function runs
# - Prints "Function has ended..." after the function runs
#
# Apply it to a function called 'greet_user(name)'
# that prints "Hello, name!"
#
# Call greet_user("Shikhar")
# Expected output:
# Function is starting...
# Hello, Shikhar!
# Function has ended...

# YOUR CODE HERE:
# def decorator_function(original_function):
def logger(func):
    def wrapper(*args , **kwargs):
        print("Function is starting...")
        func(*args,**kwargs)
        print("Function has ended...")
    return wrapper



@logger
def greet_user(name):
    print("Hello , {}".format(name))

greet_user("Shikhar")



# ============================================

# QUESTION 2 - Medium
# Create a decorator called 'timer' that:
# - Stores the time before the function runs using:
#   import time
#   start = time.time()
# - Runs the original function
# - Stores time after using:
#   end = time.time()
# - Prints "Function took X seconds to run"
#   where X = end - start
#
# Apply it to a function called 'calculate(n)'
# that adds all numbers from 0 to n using a loop
# and prints the result
#
# Call calculate(1000000)

# YOUR CODE HERE:
def timer(func):
    def wrapper(*args,**kwargs):
        import time 
        start=time.time()
        func(*args,**kwargs)
        end=time.time()
        x=end-start
        print("THE FUNCTION TOOK {} SECONDS".format(x))
    return wrapper


@timer
def calculate(n):
    sum=0
    for i in range(0,n):
        sum+=i
    print(sum)
calculate(10000)

        


# ============================================

# QUESTION 3 - Harder
# Create a decorator called 'require_login' that:
# - Checks if a variable called 'is_logged_in' is True
# - If True: runs the original function
# - If False: prints "Access denied. Please login first."
#   and does NOT run the original function
#
# Apply it to a function called 'view_dashboard(username)'
# that prints "Welcome to your dashboard, username!"
#
# Test it twice:
# - Set is_logged_in = False, call view_dashboard("Shikhar")
# - Set is_logged_in = True, call view_dashboard("Shikhar")
#
# Expected output:
# Access denied. Please login first.
# Welcome to your dashboard, Shikhar!

# YOUR CODE HERE:
is_logged_in=False
def require_login(original_function):
   
    def wrapper(*args,**kwargs):
        if is_logged_in is True:
            original_function(*args,**kwargs)
        else:
            print("ACCESS DENIED . PLEASE LOGIN FIRST")
    return wrapper


@require_login
def view_dashboard(username):
    print("Welcome to dashboard , {} ".format(username))
is_logged_in=True
view_dashboard("SHIKHAR")
    
is_logged_in=False
view_dashboard("SAMARTH")


# ============================================
# DECORATOR PRACTICE — EXTRA
# Date: 3 June 2026
# ============================================

# QUESTION 1
# Create a decorator called 'repeat' that:
# - Runs the decorated function TWICE automatically
#
# Apply it to a function greet(name) that
# prints "Hello name!"
#
# Call greet("Shikhar") once.
# It should print Hello twice.

# YOUR CODE HERE:
def repeat(func):
    def wrapper_function(*args,**kwargs):
        func(*args , **kwargs)
        func (*args , **kwargs)
    return wrapper_function
@repeat
def greet(name):
    print("HELLO {}".format(name))

greet("SHIKHAR ")
# ============================================

# QUESTION 2
# Create a decorator called 'log_args' that:
# - Before running the function prints:
#   "Calling function_name with args: X"
# - After running prints:
#   "function_name finished"
#
# Apply it to add(a, b) that prints a + b
# Apply it to multiply(a, b) that prints a * b
#
# Call both functions.

# YOUR CODE HERE:
def log_args(func):
    def wrapper_function(*args , **kwargs):
        print("CALLING THE FUNCTION WITH ARGS:{}".format(args))
        func(*args,**kwargs)
        print("{} FINISHED".format(func.__name__))
    return wrapper_function
    
@log_args
def add(a,b):
    print("SUM IS :  ",a+b)

@log_args
def mul(a,b):
    print("PRODUCT IS : ",a*b)

add(2,3)
mul(4,8)
# ============================================

# QUESTION 3 — 
# Create TWO decorators:
#
# 'uppercase' that:
# - Captures the return value of the function
# - Converts it to uppercase
# - Returns the uppercase version
#
# 'add_exclamation' that:
# - Captures the return value of the function
# - Adds "!!!" at the end
# - Returns the modified version
#
# Apply BOTH decorators to a function
# get_message(name) that returns "hello name"
#
# Stack them like this:
# @uppercase
# @add_exclamation
# def get_message(name):
#
# Print get_message("shikhar")
# Expected output: HELLO SHIKHAR!!!
#
# Then swap the order:
# @add_exclamation
# @uppercase
# def get_message2(name):
#
# Print get_message2("shikhar")
# Expected output: HELLO SHIKHAR!!!
# Wait — is the output the same or different?
# Write a comment explaining why.

# YOUR CODE HERE:
def uppercase(func):
    def wrapper_function1(*args, **kwargs):
       result=func(*args ,**kwargs)
       return result.upper()
    return wrapper_function1


def add_exclamation(func):
    def wrapper_function2(*args,  **kwargs):
        result=func(*args ,**kwargs)
        return result+"!"
    return wrapper_function2


@uppercase
@add_exclamation
def get_message(name):
    return (" hello {} ".format(name))


@add_exclamation
@uppercase
def get_message2(name):
    return (" hello {} ".format(name))


print(get_message("shikhar"))
print(get_message2("abhay"))