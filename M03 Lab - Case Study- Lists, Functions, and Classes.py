class Vehicle:
    def __init__(self,vehicle_type):
        self.vehicle_type = vehicle_type
    
    def __str__(self):
        self.vehicle_type = input("What vehicle type of vehicle are you using: ")
        return self.vehicle_type

class Automobile(Vehicle): 
    def __init__(self, vehicle_type, year = 0, make = '', model =  " ", doors = 0, roof = ''): 
        super().__init__(vehicle_type)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

    def store_attributes(self): 
        self.year = input("What year was the car made: ")
        self.make = input("What is the make of the car: ")
        self.model = input("What is the model of the car: ")
        self.doors = input("How many doors does your car have: ")
        self.roof = input("What type of roof does it have: ")

    def display_attriutes(self): 
        print(f"\nVehicle Type: {self.vehicle_type}")
        print(f"Year: {self.year}")
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Number of doors : {self.doors}")
        print(f"Type of roof: {self.roof}")



automobile1 = Automobile("Car")                     # -------------->  #instance being created 
automobile1.store_attributes()
automobile1.display_attriutes()




