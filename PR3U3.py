class Vehicle:
    def speed(self):
        pass

class Car(Vehicle):
    def speed(self):
        return "The car is speeding at 100 km/h."

class Bike(Vehicle):
    def speed(self):
        return "The bike is speeding at 80 km/h."

class Train(Vehicle):
    def speed(self):
        return "The train is speeding at 120 km/h."

def show_speed(vehicle):
    print(vehicle.speed())

vehicle_type = input("Enter vehicle type (Car/Bike/Train): ")

if vehicle_type.lower() == "car":
    vehicle = Car()
elif vehicle_type.lower() == "bike":
    vehicle = Bike()
elif vehicle_type.lower() == "train":
    vehicle = Train()
else:
    print("Invalid vehicle type!")
    exit()

show_speed(vehicle)
