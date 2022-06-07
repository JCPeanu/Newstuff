class Chair:
    canSitInIt = True
    def __init__(self, x, y, z):
        self.volume = x * y * z
a = Chair(2, 3, 4)
print(a.volume)
