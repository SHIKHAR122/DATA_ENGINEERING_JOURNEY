# ============================================================
#         DUNDER METHODS - PRACTICE QUESTIONS (Python)
# ============================================================


# ------------------------------------------------------------
# Q1: __init__ and __str__
# ------------------------------------------------------------
# Create a class `Book` with attributes: title, author, and price.
# - Use __init__ to initialize these attributes.
# - Use __str__ to return a string like:
#   "Title: Harry Potter | Author: J.K. Rowling | Price: $29.99"
#
# Expected Output:
#   print(Book("Harry Potter", "J.K. Rowling", 29.99))
#   >>> Title: Harry Potter | Author: J.K. Rowling | Price: $29.99

# YOUR CODE HERE:
class Book:
    def __init__(self,title,author,price):
        self.price=price
        self.title=title
        self.author=author


    def __str__(self):
        return ("TITLE: {} || AUTHOR {} || PRICE {}".format(self.title , self.author , self.price))
    
print(Book("Harry Potter", "J.K. Rowling", 29.99))


# ------------------------------------------------------------
# Q2: __add__ and __len__
# ------------------------------------------------------------
# Create a class `Playlist` that holds a list of songs.
# - Use __len__ to return the number of songs in the playlist.
# - Use __add__ to combine two playlists and return a new Playlist.
#
# Expected Output:
#   p1 = Playlist(["Song A", "Song B"])
#   p2 = Playlist(["Song C"])
#   p3 = p1 + p2
#   print(len(p3))  >>> 3

# YOUR CODE HERE:
class Playlist:
    def __init__(self,songs):
        self.songs=songs
    def __len__(self):
        return len(self.songs)
    def __add__(self,other):
        combine=self.songs+other.songs
        return Playlist(combine)
    

p1 = Playlist(["Song A", "Song B"])
p2 = Playlist(["Song C"])
p3 = p1 + p2          
print(len(p3))         
print(p3.songs)  
# ------------------------------------------------------------
# Q3: __getitem__ and __setitem__
# ------------------------------------------------------------
# Create a class `StudentRecord` that internally uses a dictionary
# to store subject-score pairs.
# - Use __getitem__ to retrieve a score by subject name.
# - Use __setitem__ to assign/update a score for a subject.
#
# Expected Output:
#   record = StudentRecord()
#   record["Math"] = 95
#   record["Science"] = 88
#   print(record["Math"])     >>> 95
#   print(record["Science"])  >>> 88
# YOUR CODE HERE:
class StudentRecord:
    def __init__(self):
        self.data = {}                        
    def __setitem__(self, subject, score):
        self.data[subject] = score            

    def __getitem__(self, subject):
        return self.data[subject]             


record = StudentRecord()
record["Math"] = 95           
record["Science"] = 88        
print(record["Math"])         
print(record["Science"])      
# ------------------------------------------------------------
# Q4: __eq__ and __lt__ (Comparison Dunder Methods)
# ------------------------------------------------------------
# Create a class `Employee` with attributes: name and salary.
# - Use __eq__ to check if two employees have the same salary.
# - Use __lt__ to check if one employee earns less than another.
#
# Expected Output:
#   e1 = Employee("Alice", 70000)
#   e2 = Employee("Bob", 85000)
#   e3 = Employee("Charlie", 70000)
#   print(e1 == e3)   >>> True
#   print(e1 == e2)   >>> False
#   print(e1 < e2)    >>> True

# YOUR CODE HERE:
class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def __eq__(self,other):
        return self.salary==other.salary
    def __lt__(self,other):
        return self.salary<other.salary
    
e1=Employee("SHIKAR", 2500000)
e2=Employee("ADITYA",400000)
e3=Employee("FARIS",800000)
print(e1==e2)
print(e1==e3)
print(e1<e2)
print(e2<e3)
# ------------------------------------------------------------
# Q5: __enter__ and __exit__ (Context Manager)
# ------------------------------------------------------------
# Create a class `Timer` that acts as a context manager to measure
# the time taken by a block of code.
# - Use __enter__ to record the start time.
# - Use __exit__ to calculate and print the elapsed time.
# Hint: Use the `time` module.
#
# Expected Output:
#   with Timer():
#       total = sum(range(1_000_000))
#   >>> Elapsed time: 0.0523 seconds   (time will vary)

# YOUR CODE HERE:
class Timer:
    def __init__(self,):