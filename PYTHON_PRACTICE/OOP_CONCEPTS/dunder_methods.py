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



# ============================================
# OOP PRACTICE - DAY 8
# Topic: Dunder Methods
# Date: 5 June 2026
# ============================================

# QUESTION 1 - Easy
# Create a class Book with:
# - Attributes: title, author, pages
# - __str__ that returns:
#   "title by author"
# - __repr__ that returns:
#   "Book('title', 'author', pages)"
# - __len__ that returns number of pages
#
# Create 2 Book objects.
# Print both using print() — calls __str__
# Print both using repr() — calls __repr__
# Print len() of both — calls __len__

# YOUR CODE HERE:
class Book:
    def __init__(self,title,author,pages):
        self.title=title
        self.author=author
        self.pages=pages
    def __str__(self):
        return ("{}  BY {}".format(self.author,self.title))
    def __repr__(self):
        return "Book('{}', '{}', {})".format(self.title, self.author, self.pages)
    def __len__(self):
        return self.pages
    
book1= Book("Dark Matter" , "BLAKE COUCH" , 500)
book2=Book("Flowers for Algernon" ,  "Daniel Keyes" , 311)
print("FIRST BOOK IS : ",book1)
print("SECOND BOOK IS :",book2)
print(repr(book1))
print(repr(book2))
print("LENGTH OF PAGES IN BOOK 1 IS : ",len(book1))
print("LENGTH OF PAGES IN BOOK 2 IS : ",len(book2))
# ============================================

# QUESTION 2 - Medium
# Create a class Cart with:
# - Attribute: items — empty list by default
# - Attribute: owner
# - Method add_item(item) that appends to items list
# - __len__ that returns number of items in cart
# - __str__ that returns:
#   "owner's cart has X items: [item1, item2...]"
# - __repr__ that returns:
#   "Cart(owner='owner', items=X)"
#
# Create 1 cart.
# Add 3 items.
# Print the cart — calls __str__
# Print repr(cart) — calls __repr__
# Print len(cart) — calls __len__

# YOUR CODE HERE:
class Cart:
    
    def __init__(self,owner):
        self.items=[]
        self.owner=owner
    def add_item(self,item):
        self.items.append(item)
     
    def __len__(self):
        return len(self.items)

    def __str__(self):
        return ("{} CART HAS {} ITEMS".format(self.owner , self.items))
    
    def __repr__(self):
        return "Cart(owner='{}', items={})".format(self.owner, len(self.items))
cart1=Cart("shikhar",)
cart1.add_item("APPLE")
cart1.add_item("COFFEE BEANS")
cart1.add_item("BANANA")
cart1.add_item("MUG")
print(str(cart1))
print(repr(cart1))
print(len(cart1))

    



# ============================================

# QUESTION 3 - Medium
# Create a class Team with:
# - Attribute: team_name
# - Attribute: members — empty list by default
# - Method add_member(name) that appends to members 
# - __len__ that returns number of members//
# - __str__ that returns:
#   "Team team_name has X members"
# - __repr__ that returns:
#   "Team('team_name', members=X)"
# - __contains__ that checks if a name is in members
#   this is called when you do: "Shikhar" in team
#
# Create 1 team.
# Add 4 members.
# Print the team.
# Print repr(team).
# Print len(team).
# Check if "Shikhar" is in team — print the result.
# Check if "Random" is in team — print the result.

# YOUR CODE HERE:
class Team:
    def __init__(self, team_name):
        self.team_name = team_name
        self.members = []

    def add_member(self, name):
        self.members.append(name)

    def __len__(self):
        return len(self.members)

    def __str__(self):
        return f"Team {self.team_name} has {len(self)} members"

    def __repr__(self):
        return f"Team('{self.team_name}', members={len(self)})"

    def __contains__(self, name):
        return name in self.members


team = Team("Risers")
team.add_member("Shikhar")
team.add_member("Rohit")
team.add_member("Virat")
team.add_member("Hardik")

print(team)                        
print(repr(team))                  
print(len(team))                   
print("Shikhar" in team)           
print("Random" in team)            



    
# ============================================

# QUESTION 4 - Harder
# Create a class StudentGrades with:
# - Attribute: student_name
# - Attribute: grades — empty list by default
# - Method add_grade(grade) that appends to grades
# - __len__ that returns number of grades
# - __str__ that returns:
#   "student_name has X grades. Average: Y"
#   where Y is the average rounded to 2 decimal places
# - __repr__ that returns:
#   "StudentGrades('student_name', grades=X)"
# - __getitem__ that returns grade at a given index
#   this is called when you do: student[0]
# - @property average that calculates and returns
#   sum of grades divided by number of grades
#   if no grades: return 0
#
# Create 1 StudentGrades object.
# Add 5 grades.
# Print the object — calls __str__
# Print repr — calls __repr__
# Print len — calls __len__
# Access individual grades using indexing:
#   print(student[0])
#   print(student[2])

# YOUR CODE HERE:
class StudentGrades:
    def __init__(self,student_name):
        self.student_name=student_name
        self.grades=[]
    def add_grade(self,grade):
        self.grades.append(grade)
    def __len__(self):
        return len(self.grades)
    def __str__(self):
        return ("{} HAS {} GRADES AND AVG. SCORE IS {} ".format(self.student_name,len(self.grades),self.average))
    def __repr__(self):
        return "StudentGrades('{}'   ' GRADES = {}')".format(self.student_name, len(self.grades))
    def  __getitem__(self, key):
        return self.grades[key]
    @property
    def average(self):
        if len(self.grades)==0:
            return 0
        else:
            return sum(self.grades)/len(self.grades)



student = StudentGrades("Alice")
student.add_grade(85)
student.add_grade(92)
student.add_grade(78)
student.add_grade(96)
student.add_grade(88)


print(student)          
print(repr(student))    
print(len(student))     
print(student[0])       
print(student[2])       

            