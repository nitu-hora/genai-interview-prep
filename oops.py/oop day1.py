"""
OOP DAY 1 — Classes, __init__, and Attributes
==============================================
CONCEPT: A class is a blueprint. An object is the thing built from it.

    class Dog:                  ← blueprint
        def __init__(self, name, age):
            self.name = name    ← attribute (data stored on the object)
            self.age = age

    d = Dog("Rex", 3)           ← object (instance)
    d.name                      ← "Rex"
    d.age                       ← 3

    __init__ runs automatically when you create an object.
    'self' always refers to the object being created.

Run:  python oop_day1.py
"""


# Q1. Create a class Point that stores x and y coordinates.
#     Point(3, 4).x  ->  3
#     Point(3, 4).y  ->  4
#     Point(0, 0).x  ->  0
class Point:
    def __init__(self, x,  y):
        self.x = x
        self.y = y


# Q2. Create a class Rectangle with width and height.
#     Rectangle(5, 3).width   ->  5
#     Rectangle(5, 3).height  ->  3
class Rectangle:
    def __init__(self, width, height):
        self.width  = width
        self.height = height


# Q3. Create a class Student with name and grade (0-100).
#     Student("Nitu", 92).name   ->  "Nitu"
#     Student("Nitu", 92).grade  ->  92
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

# Q4. Create a class BankAccount with owner and balance.
#     Default balance should be 0 if not provided.
#     BankAccount("Nitu", 1000).owner    ->  "Nitu"
#     BankAccount("Nitu", 1000).balance  ->  1000
#     BankAccount("Nitu").balance        ->  0
class BankAccount:
    def __init__(self, owner, balance = 0):
        self.owner = owner
        self.balance = balance



# Q5. Create a class Temperature with celsius value.
#     Add a property fahrenheit that converts on the fly (F = C * 9/5 + 32).
#     Temperature(0).celsius      ->  0
#     Temperature(0).fahrenheit   ->  32.0
#     Temperature(100).fahrenheit ->  212.0
#     HINT: just store celsius in __init__, compute fahrenheit as a method or property
class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    @property
    def fahrenheit(self):
        return self.celsius * 9/5 + 32
    

# ---------------------------------------------------------------- self-check
def _check():
    tests = [
        ("Q1 Point.x",        lambda: Point(3, 4).x == 3),
        ("Q1 Point.y",        lambda: Point(3, 4).y == 4),
        ("Q2 Rectangle",      lambda: Rectangle(5, 3).width == 5 and Rectangle(5, 3).height == 3),
        ("Q3 Student",        lambda: Student("Nitu", 92).name == "Nitu" and Student("Nitu", 92).grade == 92),
        ("Q4 BankAccount",    lambda: BankAccount("Nitu", 1000).balance == 1000 and BankAccount("Nitu").balance == 0),
        ("Q5 Temperature.c",  lambda: Temperature(0).celsius == 0),
        ("Q5 Temperature.f",  lambda: Temperature(0).fahrenheit == 32.0 and Temperature(100).fahrenheit == 212.0),
    ]
    passed = 0
    for name, fn in tests:
        try:
            ok = bool(fn())
        except Exception as e:
            ok = False
            name += f"  (error: {type(e).__name__}: {e})"
        print(("PASS  " if ok else "FAIL  ") + name)
        passed += ok
    print(f"\n{passed}/{len(tests)} passed")

if __name__ == "__main__":
    _check()