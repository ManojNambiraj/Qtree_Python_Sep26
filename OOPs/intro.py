# OOPs --> Object Oriented Programmings

    # 1. Class --> (Template)
        # --> Data Members
        # --> Member Methods

    # 2. Object
    # 3. Inheritance
    # 4. Encapsulation
    # 5. Abstraction
    # 6. Polymorphism

class Car:
    Model = ""
    no_of_wheels = 0
    no_of_sheets = 0
    fuel_type = ""
    color = ""

    def car_speed(self):
        print("Speed of my car:")

honda = Car() # Object instantiated --> Memory Intializing
hyundai = Car() # Object instantiated --> Memory Intializing

honda.Model = "Honda Civic"
honda.no_of_wheels = 5
honda.no_of_sheets = 6
honda.fuel_type = "Disel"
honda.color = "Brown"

hyundai.Model = "I20"
hyundai.no_of_wheels = 4
hyundai.no_of_sheets = 5
hyundai.fuel_type = "Petrol"
hyundai.color = "Black"

print("-----Honda-------")
print(honda.Model)
print(honda.no_of_wheels)
print(honda.no_of_sheets)
print(honda.fuel_type)
print(honda.color)

print("-----Hyundai-------")
print(hyundai.Model)
print(hyundai.no_of_wheels)
print(hyundai.no_of_sheets)
print(hyundai.fuel_type)
print(hyundai.color)