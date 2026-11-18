"""
OOP DAY 2 — Methods and __str__
================================
CONCEPT: Methods are functions that belong to a class.

    class Dog:
        def __init__(self, name):
            self.name = name

        def bark(self):             ← method (always takes self as first arg)
            return f"{self.name} says Woof!"

        def __str__(self):          ← special method: controls print(dog)
            return f"Dog named {self.name}"

    d = Dog("Rex")
    d.bark()       ->  "Rex says Woof!"
    print(d)       ->  "Dog named Rex"      (uses __str__ automatically)
    str(d)         ->  "Dog named Rex"

Run:  python oop_day2.py
"""


# Q1. Add an area() method to Rectangle.
#     Rectangle(5, 3).area()      ->  15
#     Rectangle(10, 2).area()     ->  20
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def __str__(self):
        return f"Rectangle({self.width}x{self.height})"



# Q2. Add a __str__ method to Rectangle.
#     str(Rectangle(5, 3))   ->  "Rectangle(5x3)"
#     str(Rectangle(10, 2))  ->  "Rectangle(10x2)"
#     HINT: modify the Rectangle class above, add __str__ there



# Q3. Create a Circle class with radius.
#     Add area() -> round to 2 decimal places (use 3.14159 for pi)
#     Add __str__ -> "Circle(r=5)"
#     Circle(5).area()      ->  78.54
#     str(Circle(5))        ->  "Circle(r=5)"
#     Circle(1).area()      ->  3.14
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return round(self.radius*self.radius*3.14159,2)

    def __str__(self):
        return f"Circle(r={self.radius})"


# Q4. Create a BankAccount with owner and balance (default 0).
#     Add deposit(amount)  -> adds to balance, returns new balance
#     Add withdraw(amount) -> subtracts, returns new balance; if amount > balance return "Insufficient funds"
#     Add __str__          -> "Account[Nitu]: ₹1000"
#     b = BankAccount("Nitu", 500)
#     b.deposit(200)       ->  700
#     b.withdraw(100)      ->  600
#     b.withdraw(9999)     ->  "Insufficient funds"
#     str(b)               ->  "Account[Nitu]: ₹600"
class BankAccount:
    def __init__(self, owner, balance = 0):
        self.owner = owner
        self.balance = balance

    def deposit(self,amount):
        self.balance += amount
        return self.balance
    
    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds"
        self.balance -= amount
        return self.balance
    
    def __str__(self):
        return f"Account[{self.owner}]: ₹{self.balance}"


# Q5. Create a Counter class starting at 0.
#     increment() -> adds 1, returns new value
#     decrement() -> subtracts 1, returns new value
#     reset()     -> sets back to 0, returns 0
#     __str__     -> "Counter: 3"
#     c = Counter()
#     c.increment()  ->  1
#     c.increment()  ->  2
#     c.decrement()  ->  1
#     c.reset()      ->  0
#     str(c)         ->  "Counter: 0"
class Counter:
    def __init__(self, value = 0):
        self.value = value

    def increment(self):
        self.value+=1
        return self.value

    def decrement(self):
        self.value-=1
        return self.value

    def reset(self):
        self.value = 0
        return self.value

    def __str__(self):
        return f"Counter: {self.value}"





# ---------------------------------------------------------------- self-check
def _check():
    import math
    r = Rectangle(5, 3)
    b = BankAccount("Nitu", 500)
    b.deposit(200)
    b.withdraw(100)
    c = Counter()
    c.increment(); c.increment(); c.decrement(); c.reset()

    tests = [
        ("Q1 Rectangle.area",      lambda: Rectangle(5, 3).area() == 15 and Rectangle(10, 2).area() == 20),
        ("Q2 Rectangle.__str__",   lambda: str(Rectangle(5, 3)) == "Rectangle(5x3)"),
        ("Q3 Circle.area",         lambda: Circle(5).area() == 78.54 and Circle(1).area() == 3.14),
        ("Q3 Circle.__str__",      lambda: str(Circle(5)) == "Circle(r=5)"),
        ("Q4 BankAccount.deposit", lambda: BankAccount("x", 500).deposit(200) == 700),
        ("Q4 BankAccount.withdraw",lambda: BankAccount("x", 500).withdraw(100) == 400),
        ("Q4 BankAccount.insuff",  lambda: BankAccount("x", 100).withdraw(9999) == "Insufficient funds"),
        ("Q4 BankAccount.__str__", lambda: str(b) == "Account[Nitu]: ₹600"),
        ("Q5 Counter",             lambda: str(c) == "Counter: 0"),
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