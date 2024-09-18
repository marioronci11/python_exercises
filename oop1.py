
#blueprint to create objects 
class Car:


#init is a constructor - meaning everytime a "Car" object is create __init__ will run automatically 
    
    def __init__(self, make, model, year, tires, color ):
        self.make = make
        self.model = model
        self.year = year
        self.tires = tires
        self.color = color

