# ============================================
# OOP PRACTICE - DAY 5
# Topic: Multilevel Inheritance
# Date: 30 May 2026
# ============================================

# QUESTION 1 - Medium
# Create a 3 level chain:
#
# Vehicle with:
# - Attributes: brand, fuel_type
# - Method display_info() that prints brand and fuel_type
#
# Car(Vehicle) with:
# - Additional attribute: num_doors
# - Use super().__init__() to pass brand and fuel_type up
# - Method display_info() that prints num_doors
#   PLUS calls Vehicle.display_info() using super()
#
# SportsCar(Car) with:
# - Additional attribute: turbo (True or False)
# - Use super().__init__() to pass everything up the chain
# - Method display_info() that prints turbo
#   PLUS calls Car.display_info() using super()
#
# Create 1 SportsCar object.
# Call display_info() — output should print:
#   turbo → num_doors → brand and fuel_type
#   child to grandparent order
# Print SportsCar.__mro__ and write a comment
# explaining the order.

# YOUR CODE HERE:
class Vehicle:
    def __init__(self,brand,fuel_type,**kwargs):
        super().__init__(**kwargs)
        self.brand=brand
        self.fuel_type=fuel_type
    def display_info(self):
        print("{} IS THE BRAND AND THE FUEL TYPE IS {} ".format(self.brand,self.fuel_type))

class Car(Vehicle):
    def __init__(self,num_doors,**kwargs):
        super().__init__(**kwargs)  
        self.num_doors=num_doors
    def display_info(self):
        super().display_info()
        print("THERE ARE {} NUMBER OF DOORS IN THE VEHICLE".format(self.num_doors))       

class SuperCar(Car):
    def __init__(self,turbo,**kwargs):
        super().__init__(**kwargs)
        self.turbo=turbo
    def display_info(self):
       print("IS TURBO PRESENT IN THE CAR? {}".format(self.turbo))
       super().display_info()

sc=SuperCar(brand="Merecedes",fuel_type="Petrol",num_doors=4,turbo="True")
sc.display_info()

# ============================================
# QUESTION 2 - Harder
# Create a 4 level chain:
#
# LivingThing with:
# - Attributes: is_alive (True by default)
# - Method describe() that prints "This is a living thing: True/False"
#
# Animal(LivingThing) with:
# - Attributes: name, sound
# - Use super().__init__() to pass is_alive up
# - Method describe() that prints name and sound
#   PLUS calls super().describe()
#
# Pet(Animal) with:
# - Attributes: owner
# - Use super().__init__() to pass name, sound, is_alive up
# - Method describe() that prints owner
#   PLUS calls super().describe()
#
# TrainedPet(Pet) with:
# - Attributes: trick (e.g "sit", "shake hands")
# - Use super().__init__() to pass everything up
# - Method describe() that prints trick
#   PLUS calls super().describe()
#
# Create 1 TrainedPet object.
# Call describe() — output should print:
#   trick → owner → name and sound → is_alive
#   child to great-grandparent order
# Print TrainedPet.__mro__ and write a comment
# explaining what the order means.

# YOUR CODE HERE:

class LivingThing:
    def __init__(self,is_alive=True,**kwargs):
        super().__init__(**kwargs)
        self.is_alive=is_alive
    def describe(self):
        print("THIS IS A LIVING THING {} ".format(self.is_alive))

class Animal(LivingThing):
    def __init__(self,name,sound,**kwargs):
        super().__init__(**kwargs)
        self.name=name
        self.sound=sound
    def describe(self):
        print("THE NAME IS {} AND THE SOUND IT MAKES IS {} ".format(self.name,self.sound))
        super().describe()

class Pet(Animal):
    def __init__(self,owner,**kwargs):
        super().__init__(**kwargs)
        self.owner=owner
    def describe(self):
        print(" {} IS THE OWNER OF THE PET ".format(self.owner))
        super().describe() 
        
class TrainedPet(Pet):
    def __init__(self,trick,**kwargs):
        super().__init__(**kwargs)
        self.trick=trick
    def describe(self):
        print("THE TRICK IT CAN PERFORM IS {}".format(self.trick))
        super().describe()



tp=TrainedPet(is_alive=True,name="JAMES",sound="BARKS",owner="STEVE",trick="ROLL BACK")
tp.describe()
print(TrainedPet.__mro__)