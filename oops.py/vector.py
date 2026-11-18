import math
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __len__(self):
        return len((self.x, self.y))

    def __add__(self, other):
        return (self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return (self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        return (self.x * scalar, self.y * scalar)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def __abs__(self):  
        return round(math.sqrt(self.x**2 + self.y**2), 2)

v1 = Vector(3, 4)
v2 = Vector(1, 2)

print(repr(v1))       # Vector(3, 4)
print(str(v1))        # (3, 4)
print(len(v1))        # 2
print(v1 + v2)        # Vector(4, 6)
print(v1 - v2)        # Vector(2, 2)
print(v1 * 3)         # Vector(9, 12)
print(v1 == v2)       # False
print(v1 == Vector(3,4))  # True
print(abs(v1))        # 5.0  (3²+4²=25, √25=5)