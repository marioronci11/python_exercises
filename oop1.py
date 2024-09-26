
#Classes contain characteristics called Attributes like a private dictionary
#an instance is another name for an object
#blueprint to create objects class creates a class
#Yes, "instantiation" in object-oriented programming means the act of creating a new object from a class, essentially "bringing a class to life" by creating a concrete instance of it; so, when you create an object within a class, you are "instantiating" that class.
class Car:

#: Constructors trigger Python's instantiation process, which runs through two main steps: instance creation and instance initialization. 
#init is a constructor - meaning everytime a "Car" object is create __init__ will run automatically 
#it constructs the object in this case ie. "make" and assign a value to the object's members
#self is the object itself

    def __init__(self, make, model, year, tires, color ):
        self.make = make
        self.model = model
        self.year = year
        self.tires = tires
        self.color = color


# the object self is refrencing itself and this is the attributes
my_car = Car ("Toyota", "Camry", 2020, 4, "black")

def start_car():
        print(f"Car starting... {my_car.make, my_car.model, my_car.year}")
       
start_car()

#scopes are important here, functions are global wherever it is defined