from posixpath import supports_unicode_filenames


class Cars:
    def __init__(self, model_given, color_given, age_given, oil_change):
        self.model = model_given
        self.color = color_given
        self.age = age_given
        self.oil_change = oil_change
    
    def changeColor(self, newColor):
        self.color = newColor
    
    def __init__(self):
        return f"This car is a {self.model}, with a {self.color} color, and it is {self.age} years old. ", "It needs a refill of oil." if self.oil_change else print("It's good. ")

    def prDetails(self):
        print(f"This car is a {self.model}, with a {self.color} color, and it is {self.age} years old. ")
        print("It needs a refill of oil.") if self.oil_change else print("It's good. ")

car1 = Cars("Maserati", "silver", 64, True)
print(car1)
car1.changeColor("Rainbow")
print(car1)

car2 = Cars("Honda", "green", 1, False)
print(car2)