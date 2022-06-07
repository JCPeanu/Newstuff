class Numbers:
    MULTIPLIER = 0
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def add(self):
        return self.x + self.y
    @classmethod
    def multiply(cls, a):
        return a * cls.MULTIPLIER
    @staticmethod
    def subtract(b, c):
        return b - c
    @property
    def value(self):
        tup = (self.x, self.y)
        return tup
    @value.setter
    def value(self, value):
        self.x, self.y = value[0], value[1]
    @value.deleter
    def value(self):
        del self.x
        del self.y

two = Numbers(2, 3)
print(two.add())
print(two.multiply(20))
print(Numbers.subtract(3, 2))
print(two.value)
two.value = (1, 2)
print(two.value)
del two.value
