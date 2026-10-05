class Car:
    def __init__(self, model, wheels, sheets, fuel, colors):
        self.Model = model
        self.no_of_wheels = wheels
        self.no_of_sheets = sheets
        self.fuel_type = fuel
        self.color = colors

    def car_speed(self, speed):
        print(f"Speed of {self} car: ", speed)

    def __str__(self):
        return self.Model

    def __del__(self):
        print("Memory Cleared")
    

honda = Car("Honda", 5, 7, "Disel", "Red")
hyundai = Car("i20", 4, 5, "Petrol", "Black")

print("----Honda-----")
print(honda.color)
print(honda.fuel_type)
print(honda.no_of_sheets)
print(honda.no_of_wheels)
print(honda.Model)
honda.car_speed(360)

print("----Hyundai-----")
print(hyundai.color)
print(hyundai.fuel_type)
print(hyundai.no_of_sheets)
print(hyundai.no_of_wheels)
print(hyundai.Model)
hyundai.car_speed(420)

