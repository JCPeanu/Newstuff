from turtle import distance


class Human:
    human_count = 0
    distance = 0
    #constructor. create subjects by specifying name and age.
    def __init__(self, name_given, age_given):
        self.name = name_given
        self.age = age_given
        Human.human_count += 1
    
    #instance method. executes a command on an object
    def walk(self, x):
        print(self.name, "is walking.")
        self.distance += x
        print(self.name, "has walked", self.distance, "meters.")
    
person1 = Human("Jose", 99)
person1.walk(5)
print(Human.human_count)
person2 = Human("Bumgyu", 55)
person2.walk(10)
print(Human.human_count)