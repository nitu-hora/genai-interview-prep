"""
OOP DAY 3 — Class Variables vs Instance Variables
==================================================
CONCEPT:
    Instance variable  → belongs to ONE object (set with self.x = ...)
    Class variable     → shared by ALL objects of the class

    class Dog:
        species = "Canis familiaris"   ← class variable (same for every dog)

        def __init__(self, name):
            self.name = name           ← instance variable (different per dog)

    d1 = Dog("Rex")
    d2 = Dog("Bella")

    d1.name        ->  "Rex"           (own)
    d2.name        ->  "Bella"         (own)
    d1.species     ->  "Canis familiaris"   (shared)
    Dog.species    ->  "Canis familiaris"   (access from class directly)

    Changing Dog.species changes it for ALL dogs.
    Changing d1.species only changes it for d1.

Run:  python oop_day3.py
"""


# Q1. Create a Dog class.
#     Class variable: species = "Canis familiaris"
#     Instance variables: name, breed
#     Dog("Rex", "Labrador").name     ->  "Rex"
#     Dog("Rex", "Labrador").breed    ->  "Labrador"
#     Dog("Rex", "Labrador").species  ->  "Canis familiaris"
#     Dog.species                     ->  "Canis familiaris"
class Dog:
    species = "Canis familiaris"
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed


# Q2. Create an Employee class that tracks how many employees exist.
#     Class variable: count = 0  (increases by 1 each time a new Employee is created)
#     Instance variables: name, role
#     HINT: in __init__, do Employee.count += 1
#     e1 = Employee("Nitu", "Engineer")
#     e2 = Employee("Anu", "Manager")
#     Employee.count   ->  2
#     e1.name          ->  "Nitu"
class Employee:
    count = 0
    def __init__(self, name, role):
        self.name = name
        self.role = role
        Employee.count+=1

# Q3. Create a Product class.
#     Class variable: tax_rate = 0.18
#     Instance variables: name, price
#     Add method price_with_tax() -> price + (price * tax_rate), rounded to 2 decimals
#     Product("Laptop", 50000).price_with_tax()  ->  59000.0
#     Product("Phone", 20000).price_with_tax()   ->  23600.0
#     Product.tax_rate                            ->  0.18
class Product:
    tax_rate = 0.18
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def price_with_tax(self):
        return round(self.price+(self.price*Product.tax_rate),2)

# Q4. Create a Student class.
#     Class variable: school = "IIT KGP"
#     Instance variables: name, marks (a list of numbers)
#     Method: average() -> average of marks, rounded to 2 decimals
#     Method: passed()  -> True if average >= 40, else False
#     s = Student("Nitu", [80, 90, 70])
#     s.average()   ->  80.0
#     s.passed()    ->  True
#     Student.school ->  "IIT KGP"
#     s2 = Student("X", [30, 20, 10])
#     s2.passed()   ->  False
class Student:
    school = "IIT KGP"
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def average(self):
        return round(sum(self.marks)/len(self.marks),2)

    def passed(self):
        return self.average() >= 40


# ---------------------------------------------------------------- self-check
def _check():
    e1 = Employee("Nitu", "Engineer")
    e2 = Employee("Anu", "Manager")
    s1 = Student("Nitu", [80, 90, 70])
    s2 = Student("X", [30, 20, 10])

    tests = [
        ("Q1 Dog instance vars",   lambda: Dog("Rex", "Lab").name == "Rex" and Dog("Rex", "Lab").breed == "Lab"),
        ("Q1 Dog class var",       lambda: Dog.species == "Canis familiaris" and Dog("Rex","Lab").species == "Canis familiaris"),
        ("Q2 Employee.count",      lambda: Employee.count == 2),
        ("Q2 Employee.name",       lambda: e1.name == "Nitu"),
        ("Q3 price_with_tax",      lambda: Product("Laptop", 50000).price_with_tax() == 59000.0),
        ("Q3 tax_rate",            lambda: Product.tax_rate == 0.18),
        ("Q4 Student.average",     lambda: s1.average() == 80.0),
        ("Q4 Student.passed True", lambda: s1.passed() == True),
        ("Q4 Student.passed False",lambda: s2.passed() == False),
        ("Q4 Student.school",      lambda: Student.school == "IIT KGP"),
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