"""
OOP DAY 4 — Inheritance
========================
CONCEPT: A child class gets everything the parent class has, for free.

    class Animal:                      ← parent
        def __init__(self, name):
            self.name = name
        def eat(self):
            return f"{self.name} is eating"

    class Dog(Animal):                 ← child (inherits from Animal)
        def bark(self):
            return f"{self.name} says Woof!"

    d = Dog("Rex")
    d.eat()    ->  "Rex is eating"    (inherited from Animal)
    d.bark()   ->  "Rex says Woof!"   (Dog's own method)

    To add your OWN __init__ in the child while keeping parent's:
    class Dog(Animal):
        def __init__(self, name, breed):
            super().__init__(name)     ← calls Animal's __init__
            self.breed = breed         ← Dog's own new attribute

Run:  python oop_day4.py
"""

# Q1. Create a Vehicle parent class with make and year.
#     Create a Car child class that inherits Vehicle and adds doors (default 4).
#     Car("Toyota", 2022).make   ->  "Toyota"
#     Car("Toyota", 2022).year   ->  2022
#     Car("Toyota", 2022).doors  ->  4
#     Car("Toyota", 2022, 2).doors -> 2
class Vehicle:
    def __init__(self, make, year):
        self.make = make
        self.year = year

class Car(Vehicle):
    def __init__(self, make, year, doors = 4):
        super().__init__(make, year)
        self.doors = doors

# Q2. Create a Shape parent with color (default "red").
#     Create Square child with side. Add area() method.
#     Create Triangle child with base and height. Add area() method (0.5 * base * height).
#     Square("blue", 4).color    ->  "blue"
#     Square("blue", 4).area()   ->  16
#     Triangle("green", 6, 3).area()  ->  9.0
class Shape:
    def __init__(self, color = 'red'):
        self.color = color

class Square(Shape):
    def __init__(self, color, side):
        super().__init__(color)
        self.side = side

    def area(self):
        return self.side * self.side

class Triangle(Shape):
    def __init__(self, color, base, height):
        super().__init__(color)
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


# Q3. Create an Animal parent with name and sound.
#     Add speak() -> "{name} says {sound}"
#     Create Dog child (sound defaults to "Woof") and Cat child (sound defaults to "Meow").
#     Dog and Cat should work WITHOUT passing sound.
#     Dog("Rex").speak()    ->  "Rex says Woof"
#     Cat("Luna").speak()   ->  "Luna says Meow"
#     Dog("Rex", "Bark").speak()  ->  "Rex says Bark"
class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    
    def speak(self):
        return f'{self.name} says {self.sound}'


class Dog(Animal):
    def __init__(self,name, sound = 'Woof'):
        super().__init__(name, sound)

class Cat(Animal):
    def __init__(self,name, sound = 'Meow'):
        super().__init__(name, sound)

# Q4. Create a Person parent with name and age.
#     Add greeting() -> "Hi, I am {name}"
#     Create Engineer child — adds skill attribute.
#     Add __str__ -> "Engineer {name} ({skill})"
#     Engineer("Nitu", 28, "Python").greeting()  ->  "Hi, I am Nitu"
#     Engineer("Nitu", 28, "Python").skill       ->  "Python"
#     str(Engineer("Nitu", 28, "Python"))        ->  "Engineer Nitu (Python)"
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greeting(self):
        return f"Hi, I am {self.name}"

class Engineer(Person):
    def __init__(self, name, age, skill):
        super().__init__(name, age)
        self.skill = skill

    def __str__(self):
        return f"{self.__class__.__name__} {self.name} ({self.skill})"

# Q5. Create a BankAccount class (no parent).
#     Instance variables: owner, balance (default 0)
#     Methods:
#       deposit(amount)  -> adds to balance, returns new balance
#       withdraw(amount) -> subtracts from balance, returns new balance
#                          if amount > balance, return "Insufficient funds"
#       __str__          -> "Nitu: 500"
#
#     Then create SavingsAccount that inherits BankAccount.
#       Adds: interest_rate (default 0.05)
#       Adds: add_interest() -> balance += balance * interest_rate, returns new balance
#
#     b = SavingsAccount("Nitu", 1000)
#     b.deposit(500)        ->  1500
#     b.add_interest()      ->  1575.0
#     print(b)              ->  "Nitu: 1575.0"
class BankAccount():
    def __init__(self, owner, balance = 0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficinet Funds")
        else:
            self.balance-= amount
            return self.balance
        

    def __str__(self):
        return f"{self.owner}: {self.balance}"

class SavingsAccount(BankAccount):
    def __init__(self,owner, balance,  interest_rate = 0.05):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        self.balance += self.balance * self.interest_rate
        return self.balance

# ---------------------------------------------------------------- self-check
def _check():
    tests = [
        ("Q1 Car inherits make",    lambda: Car("Toyota", 2022).make == "Toyota"),
        ("Q1 Car default doors",    lambda: Car("Toyota", 2022).doors == 4),
        ("Q1 Car custom doors",     lambda: Car("Toyota", 2022, 2).doors == 2),
        ("Q2 Square.color",         lambda: Square("blue", 4).color == "blue"),
        ("Q2 Square.area",          lambda: Square("blue", 4).area() == 16),
        ("Q2 Triangle.area",        lambda: Triangle("green", 6, 3).area() == 9.0),
        ("Q3 Dog.speak default",    lambda: Dog("Rex").speak() == "Rex says Woof"),
        ("Q3 Cat.speak default",    lambda: Cat("Luna").speak() == "Luna says Meow"),
        ("Q3 Dog.speak custom",     lambda: Dog("Rex", "Bark").speak() == "Rex says Bark"),
        ("Q4 Engineer.greeting",    lambda: Engineer("Nitu", 28, "Python").greeting() == "Hi, I am Nitu"),
        ("Q4 Engineer.__str__",     lambda: str(Engineer("Nitu", 28, "Python")) == "Engineer Nitu (Python)"),
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