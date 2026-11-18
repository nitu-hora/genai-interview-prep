"""
OOP DAY 6 — Encapsulation and Properties
==========================================
CONCEPT: Encapsulation = hiding internal data, controlling access through methods.

    Private attributes start with _ (convention: "don't touch directly")
    or __ (name-mangled, harder to access from outside).

    class BankAccount:
        def __init__(self, balance):
            self._balance = balance        ← private (convention)

        def get_balance(self):             ← getter: read it safely
            return self._balance

        def deposit(self, amount):         ← controlled way to change it
            if amount > 0:
                self._balance += amount

CONCEPT: @property — makes a method look like an attribute.

    class Temperature:
        def __init__(self, celsius):
            self._celsius = celsius

        @property
        def fahrenheit(self):              ← called like t.fahrenheit, not t.fahrenheit()
            return self._celsius * 9/5 + 32

        @fahrenheit.setter
        def fahrenheit(self, value):       ← t.fahrenheit = 100 triggers this
            self._celsius = (value - 32) * 5/9

    t = Temperature(0)
    t.fahrenheit         ->  32.0      (no parentheses!)
    t.fahrenheit = 212   (sets celsius to 100)
    t._celsius           ->  100.0

Run:  python oop_day6.py
"""


# Q1. Create a Person class with a private _name attribute.
#     Add a name property (getter) that returns it.
#     Add a name setter that capitalizes before storing.
#     p = Person("nitu")
#     p.name           ->  "Nitu"    (auto-capitalized on set)
#     p.name = "anu"
#     p.name           ->  "Anu"
class Person:
    def __init__(self, name):
        pass  # store as self._name, but use the setter logic


# Q2. Create a Circle class with private _radius.
#     radius property: getter returns _radius; setter rejects negative (keep old value if negative given).
#     diameter property (read-only): returns radius * 2
#     area property (read-only): returns round(3.14159 * radius ** 2, 2)
#     c = Circle(5)
#     c.radius      ->  5
#     c.diameter    ->  10
#     c.area        ->  78.54
#     c.radius = -1
#     c.radius      ->  5    (unchanged — negative rejected)
#     c.radius = 3
#     c.diameter    ->  6
class Circle:
    def __init__(self, radius):
        self._radius = radius


# Q3. Create a BankAccount with private _balance (default 0).
#     balance property: getter only (no setter — balance changes only via deposit/withdraw).
#     deposit(amount)  -> if amount > 0: add; return new balance
#     withdraw(amount) -> if amount > balance: return "Insufficient funds"; else subtract, return new balance
#     b = BankAccount(1000)
#     b.balance        ->  1000
#     b.deposit(500)   ->  1500
#     b.withdraw(200)  ->  1300
#     b.withdraw(9999) ->  "Insufficient funds"
#     b.balance        ->  1300
class BankAccount:
    def __init__(self, balance=0):
        self._balance = balance


# Q4. Create a Student with private _marks list (starts empty).
#     add_mark(mark)  -> append only if 0 <= mark <= 100, else ignore
#     marks property  -> returns copy of the list (so outside code can't mutate it)
#     average property -> round(sum/len, 2); return 0 if no marks
#     grade property   -> "A" if avg>=80, "B" if >=60, "C" if >=40, "F" otherwise
#     s = Student()
#     s.add_mark(85); s.add_mark(72); s.add_mark(150)  # 150 ignored
#     s.marks      ->  [85, 72]
#     s.average    ->  78.5
#     s.grade      ->  "C"   (wait — 78.5 is B range... check the logic above)
#     s.add_mark(90)
#     s.average    ->  82.33
#     s.grade      ->  "A"
class Student:
    def __init__(self):
        self._marks = []


# ---------------------------------------------------------------- self-check
def _check():
    p = Person("nitu")
    p_set = Person("nitu")
    p_set.name = "anu"

    c = Circle(5)
    c_neg = Circle(5)
    c_neg.radius = -1
    c_change = Circle(5)
    c_change.radius = 3

    b = BankAccount(1000)
    b.deposit(500)
    b.withdraw(200)

    s = Student()
    s.add_mark(85); s.add_mark(72); s.add_mark(150)

    tests = [
        ("Q1 Person.name getter",   lambda: p.name == "Nitu"),
        ("Q1 Person.name setter",   lambda: p_set.name == "Anu"),
        ("Q2 Circle.radius",        lambda: c.radius == 5),
        ("Q2 Circle.diameter",      lambda: c.diameter == 10),
        ("Q2 Circle.area",          lambda: c.area == 78.54),
        ("Q2 Circle neg rejected",  lambda: c_neg.radius == 5),
        ("Q2 Circle.diameter after",lambda: c_change.diameter == 6),
        ("Q3 BankAccount.balance",  lambda: b.balance == 1300),
        ("Q3 BankAccount insuff",   lambda: BankAccount(100).withdraw(9999) == "Insufficient funds"),
        ("Q4 Student.marks",        lambda: s.marks == [85, 72]),
        ("Q4 Student.average",      lambda: s.average == 78.5),
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