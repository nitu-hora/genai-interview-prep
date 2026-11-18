"""
OOP DAY 5 — Method Overriding and super()
==========================================
CONCEPT: A child class can REPLACE a parent's method with its own version.
         This is called overriding.

    class Animal:
        def speak(self):
            return "..."

    class Dog(Animal):
        def speak(self):           ← overrides Animal's speak
            return "Woof!"

    class Cat(Animal):
        def speak(self):           ← overrides Animal's speak
            return "Meow!"

    Dog().speak()   ->  "Woof!"   (Dog's version)
    Cat().speak()   ->  "Meow!"   (Cat's version)

CONCEPT: super() calls the PARENT's version of a method.

    class Dog(Animal):
        def speak(self):
            parent_result = super().speak()     ← runs Animal's speak first
            return parent_result + " (loud)"

WHY IT MATTERS for interviews: This is polymorphism — same method name,
different behavior per class. Core OOP concept, asked in every interview.

Run:  python oop_day5.py
"""


# Q1. Override speak() in each child.
#     Dog.speak()  ->  "Woof!"
#     Cat.speak()  ->  "Meow!"
#     Bird.speak() ->  "Tweet!"
class Animal:
    def speak(self):
        return "..."

class Dog(Animal):
    pass  # override speak()

class Cat(Animal):
    pass

class Bird(Animal):
    pass


# Q2. Parent Employee has work() -> "Working..."
#     Engineer overrides: "Writing code..."
#     Manager overrides:  "Managing team..."
#     But both should ALSO include the parent message.
#     Engineer().work()  ->  "Working... Writing code..."
#     Manager().work()   ->  "Working... Managing team..."
#     HINT: use super().work() + " " + your addition
class Employee:
    def work(self):
        return "Working..."

class Engineer(Employee):
    pass

class Manager(Employee):
    pass


# Q3. Shape has area() -> 0 (default).
#     Override in each child:
#     Circle(5).area()      ->  78.54   (pi=3.14159, round to 2)
#     Rectangle(4, 6).area()->  24
#     Triangle(3, 8).area() ->  12.0    (0.5 * base * height)
class Shape:
    def area(self):
        return 0

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height


# Q4. Notification base class has send() -> "Sending notification..."
#     EmailNotification overrides: "Sending email to {email}..."
#     SMSNotification overrides:   "Sending SMS to {phone}..."
#     Both should include the base message first (use super()).
#     EmailNotification("nitu@gmail.com").send()
#         ->  "Sending notification... Sending email to nitu@gmail.com..."
#     SMSNotification("9876543210").send()
#         ->  "Sending notification... Sending SMS to 9876543210..."
class Notification:
    def send(self):
        return "Sending notification..."

class EmailNotification(Notification):
    def __init__(self, email):
        self.email = email

class SMSNotification(Notification):
    def __init__(self, phone):
        self.phone = phone


# ---------------------------------------------------------------- self-check
def _check():
    tests = [
        ("Q1 Dog.speak",          lambda: Dog().speak() == "Woof!"),
        ("Q1 Cat.speak",          lambda: Cat().speak() == "Meow!"),
        ("Q1 Bird.speak",         lambda: Bird().speak() == "Tweet!"),
        ("Q2 Engineer.work",      lambda: Engineer().work() == "Working... Writing code..."),
        ("Q2 Manager.work",       lambda: Manager().work() == "Working... Managing team..."),
        ("Q3 Circle.area",        lambda: Circle(5).area() == 78.54),
        ("Q3 Rectangle.area",     lambda: Rectangle(4, 6).area() == 24),
        ("Q3 Triangle.area",      lambda: Triangle(3, 8).area() == 12.0),
        ("Q4 EmailNotification",  lambda: EmailNotification("nitu@gmail.com").send() == "Sending notification... Sending email to nitu@gmail.com..."),
        ("Q4 SMSNotification",    lambda: SMSNotification("9876543210").send() == "Sending notification... Sending SMS to 9876543210..."),
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