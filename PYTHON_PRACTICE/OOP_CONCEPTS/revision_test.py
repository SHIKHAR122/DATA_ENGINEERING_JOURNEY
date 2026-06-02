# ============================================
# OOP REVISION TEST
# Date: 2 June 2026
# No Googling. No scrolling up. Timer on.
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


# ============================================

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