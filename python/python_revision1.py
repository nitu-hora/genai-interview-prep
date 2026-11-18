"""
PYTHON REVISION — COMPLETE REFERENCE + PRACTICE
=================================================
Every concept from your course, with:
  - WHY it exists
  - HOW it works
  - YOUR solution (already written)
  - A memory hook so it sticks

Run at the end:  python python_revision_final.py
All checks are at the bottom. Nothing interrupts the reading.
"""
import sys
sys.stdout.reconfigure(encoding='utf-8')
from functools import wraps
from collections import defaultdict
from itertools import islice
from typing import Optional
import time
import logging

logging.basicConfig(level=logging.INFO)


# ══════════════════════════════════════════════════════════════════
#  SECTION 1 — FUNDAMENTALS
# ══════════════════════════════════════════════════════════════════
#
#  WHY: These are the patterns that show up in 80% of real problems.
#  No library needed — just loops, dicts, and sets.
# ──────────────────────────────────────────────────────────────────

# Q1. Word frequency counter
# WHY dict: you need to track counts. dict maps word → count.
# MEMORY HOOK: "dict is a tally sheet"
def word_frequency(text: str) -> dict:
    result = {}
    for word in text.lower().split():
        if word not in result:
            result[word] = 1
        else:
            result[word] += 1
    return result
# word_frequency("the cat and The dog") → {"the": 2, "cat": 1, "and": 1, "dog": 1}
# word_frequency("") → {}


# Q2. Group anagrams
# WHY sorted key: anagrams share the same sorted letters → same key
# WHY defaultdict: avoids KeyError when first adding to a new list
# MEMORY HOOK: "sort the letters → same key = same anagram group"
def group_anagrams(words: list) -> dict:
    result = defaultdict(list)          # defaultdict(list) = auto-creates [] for new keys
    for word in words:
        result[''.join(sorted(word))].append(word)
    return dict(result)
# group_anagrams(["eat","tea","tan","ate","nat","bat"])
# → {"aet": ["eat","tea","ate"], "ant": ["tan","nat"], "abt": ["bat"]}


# Q3. Compress consecutive runs
# WHY loop not Counter: "abba" → a1b2a1, NOT a2b2. Runs reset when char changes.
# Counter counts total occurrences — wrong here.
# MEMORY HOOK: "track the CURRENT run, flush when it breaks"
def compress(s: str) -> str:
    if not s:
        return ""
    parts = []
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            count += 1
        else:
            parts.append(s[i-1] + str(count))
            count = 1
    parts.append(s[-1] + str(count))   # ← flush the last run (outside the loop!)
    return "".join(parts)
# compress("aaabbc") → "a3b2c1"
# compress("abba")   → "a1b2a1"    ← NOT "a2b2"


# Q4. Chunk a list
# WHY range(0, len, size): step by size to get start of each chunk
# MEMORY HOOK: "step by chunk size, slice forward"
def chunk_list(items: list, size: int) -> list:
    return [items[i:i+size] for i in range(0, len(items), size)]
# chunk_list([1,2,3,4,5], 2) → [[1,2],[3,4],[5]]
# chunk_list([], 4) → []


# Q5. Second largest distinct value
# WHY set: removes duplicates first. sorted(set(...)) gives unique sorted values.
# MEMORY HOOK: "unique → sort → index 1"
def second_largest(nums: list) -> int | None:
    unique = sorted(set(nums), reverse=True)
    return unique[1] if len(unique) >= 2 else None
# second_largest([5,5,2]) → 2
# second_largest([5,5])   → None


# ══════════════════════════════════════════════════════════════════
#  SECTION 2 — LAMBDAS & COMPREHENSIONS
# ══════════════════════════════════════════════════════════════════
#
#  WHY lambdas: one-line anonymous functions, perfect as sort keys
#  WHY comprehensions: faster, more readable than for-loop + append
#  RULE: if you need side effects or multiple lines → use def, not lambda
# ──────────────────────────────────────────────────────────────────

# Q6. Sort with multi-key lambda
# WHY -x[1]: negate score so highest score sorts first (sorted is ascending by default)
# WHY x[2]: age ascending = youngest first on ties
# MEMORY HOOK: "negate what you want descending"
def sort_students(students: list) -> list:
    return [x[0] for x in sorted(students, key=lambda x: (-x[1], x[2]))]
# sort_students([("Anu",90,25), ("Ravi",90,22), ("Bala",80,30)]) → ["Ravi","Anu","Bala"]


# Q7. Dict comprehension with zip + filter
# WHY zip: pairs two lists together element by element
# MEMORY HOOK: "zip = like a zipper, pairs them up"
def filter_zip_dict(keys: list, values: list) -> dict:
    return {k: v for k, v in zip(keys, values) if v > 50}
# filter_zip_dict(["a","b","c","d"], [10,60,90,30]) → {"b":60, "c":90}


# Q8. Generator vs List Comprehension
# WHY generator uses less memory:
#   List:      builds ALL values in RAM first, then sums → holds 500,000 numbers at once
#   Generator: produces ONE value, adds to sum, discards it → holds 1 number at a time
# MEMORY HOOK: "generator = conveyor belt. list = warehouse."

def sum_odd_squares_list(n: int) -> int:
    return sum([x**2 for x in range(n) if x % 2 != 0])   # builds full list in RAM

def sum_odd_squares_gen(n: int) -> int:
    return sum(x**2 for x in range(n) if x % 2 != 0)     # no [] = generator expression


# ══════════════════════════════════════════════════════════════════
#  SECTION 3 — DECORATORS
# ══════════════════════════════════════════════════════════════════
#
#  WHAT a decorator is: a function that takes a function and returns
#  a new function that wraps it — adds behaviour before/after.
#
#  WHY @wraps: preserves the original function's __name__ and __doc__
#  so debugging tools don't see "wrapper" everywhere.
#
#  PATTERN to memorize:
#    def my_decorator(func):
#        @wraps(func)
#        def wrapper(*args, **kwargs):
#            # do stuff before
#            result = func(*args, **kwargs)
#            # do stuff after
#            return result
#        return wrapper
# ──────────────────────────────────────────────────────────────────

# Q9. Timer decorator
def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        logging.info("%s took %.4f seconds", func.__name__, elapsed)
        return result
    return wrapper

@timer
def slow():
    time.sleep(0.05)
    return "done"


# Q10. Retry decorator (parametrized — decorator factory)
# WHY 3 levels: retry(times) returns decorator, decorator returns wrapper
# MEMORY HOOK: "parametrized decorator = decorator factory = one extra def"
def retry(times: int):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(times):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"attempt {attempt+1} failed: {e}")
            raise e     # re-raise last exception after all attempts exhausted
        return wrapper
    return decorator

_call_count = 0

@retry(times=3)
def flaky():
    global _call_count
    _call_count += 1
    if _call_count < 3:
        raise ValueError("not ready yet")
    return "ok"


# ══════════════════════════════════════════════════════════════════
#  SECTION 4 — ERROR HANDLING
# ══════════════════════════════════════════════════════════════════
#
#  WHAT: structured way to handle failure without crashing
#
#  PATTERN:
#    try:
#        risky code
#    except SpecificError as e:
#        handle it
#    except AnotherError:
#        handle it
#    else:
#        runs only if NO exception
#    finally:
#        ALWAYS runs (cleanup — close files, DB connections)
#
#  WHY custom exceptions: lets callers catch YOUR specific error
#  vs catching a generic Exception that could mean anything
# ──────────────────────────────────────────────────────────────────

# Q11. Custom exceptions + process_payment
class InsufficientFundsError(Exception):
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        super().__init__(f"Balance {balance} is insufficient for withdrawal of {amount}")

class InvalidCardError(Exception):
    def __init__(self, card_number):
        super().__init__(f"card number {card_number} is invalid")

def process_payment(balance: int, amount: int, card_number: str) -> str:
    if not card_number.startswith(('4', '5')):
        raise InvalidCardError(card_number)
    if amount > balance:
        raise InsufficientFundsError(balance, amount)
    return f"payment of {amount} successful. remaining balance : {balance - amount}"


# Q12. Context manager using __enter__ / __exit__
# WHY context managers: guarantee cleanup (connection closed, file saved)
# even if an exception happens inside the with block.
# MEMORY HOOK: "__enter__ = setup, __exit__ = teardown, always"
class DatabaseConnection:
    def __init__(self):
        self.connected = False

    def __enter__(self):
        print("opening DB connection")
        self.connected = True
        return self                         # ← what 'as db' receives

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("closing DB connection")
        self.connected = False
        return False                        # ← False = don't suppress exceptions

    def query(self, sql: str):
        if not self.connected:
            raise RuntimeError("No active connection")
        print(f"Running query: {sql}")


# ══════════════════════════════════════════════════════════════════
#  SECTION 5 — OOP
# ══════════════════════════════════════════════════════════════════
#
#  4 PILLARS (memorize with: EPIA)
#    Encapsulation  → hide internal state (_x, __x, @property)
#    Polymorphism   → same method name, different behavior per class
#    Inheritance    → child class reuses parent code
#    Abstraction    → expose only what's needed, hide complexity
#
#  KEY SYNTAX:
#    __init__   → constructor, runs when object is created
#    self       → the instance itself (like 'this' in Java)
#    super()    → call the parent class's method
#    @property  → getter — access like an attribute, not a method call
#    @x.setter  → setter — called when you do obj.x = value
# ──────────────────────────────────────────────────────────────────

# Q13. BankAccount
class BankAccount:
    def __init__(self, owner: str, balance: int = 0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount: int) -> int:
        self.balance += amount
        return self.balance

    def withdraw(self, amount: int):
        if amount > self.balance:
            return "Insufficient funds"
        self.balance -= amount
        return self.balance

    def __str__(self) -> str:
        return f"Account[{self.owner}]: ₹{self.balance}"


# Q14. SavingsAccount inherits BankAccount
# WHY super().__init__: reuses parent's __init__ instead of rewriting it
# MEMORY HOOK: "super() = call mom's recipe, then add your own spice"
class SavingsAccount(BankAccount):
    def __init__(self, owner: str, balance: int = 0, interest_rate: float = 0.05):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def add_interest(self) -> float:
        self.balance += self.balance * self.interest_rate
        return self.balance


# Q15. Temperature with @property
# WHY @property: lets you write t.fahrenheit (looks like attribute)
# but it actually runs a function — so you can add conversion logic
# MEMORY HOOK: "@property = smart attribute"
class Temperature:
    def __init__(self, celsius: float):
        self._celsius = celsius

    @property
    def fahrenheit(self) -> float:
        return self._celsius * 9/5 + 32

    @fahrenheit.setter
    def fahrenheit(self, f: float):
        self._celsius = (f - 32) * 5/9


# Q16. Circle with encapsulation
# WHY reject negative radius in setter: maintain invariant (circle can't have -radius)
# _radius (single underscore) = "please don't touch this directly" (convention, not enforced)
class Circle:
    def __init__(self, radius: float):
        self._radius = radius

    @property
    def radius(self) -> float:
        return self._radius

    @radius.setter
    def radius(self, value: float):
        if value >= 0:                  # silently ignore negatives
            self._radius = value

    @property
    def diameter(self) -> float:
        return self._radius * 2

    @property
    def area(self) -> float:
        return round(3.14159 * self._radius ** 2, 2)


# ══════════════════════════════════════════════════════════════════
#  SECTION 6 — OOP MINI PROJECT (Library System)
# ══════════════════════════════════════════════════════════════════
#
#  Shows class variables vs instance variables (Q20 too)
#  CLASS variable:    shared by ALL instances  → Book.total_books
#  INSTANCE variable: unique to each object    → self.title
# ──────────────────────────────────────────────────────────────────

# Q17. Book
class Book:
    total_books = 0                         # CLASS variable — shared

    def __init__(self, title: str, author: str, pages: int):
        self.title = title
        self.author = author
        self.pages = pages
        Book.total_books += 1               # increment CLASS var, not self.total_books

    def __str__(self) -> str:
        return f"'{self.title}' by {self.author} ({self.pages} pages)"

    @property
    def is_long(self) -> bool:
        return self.pages > 300


# Q18. Member
class Member:
    def __init__(self, name: str):
        self.name = name
        self._borrowed = []                 # private list

    @property
    def borrowed(self) -> list:
        return self._borrowed.copy()        # return copy, not reference — caller can't mutate

    def borrow(self, book: Book) -> str:
        if len(self._borrowed) >= 3:
            return "Borrow limit reached"
        self._borrowed.append(book)
        return f"Borrowed '{book.title}'"

    def return_book(self, book: Book) -> str:
        if book in self._borrowed:
            self._borrowed.remove(book)
            return f"Returned '{book.title}'"
        return "Book not found"

    def __str__(self) -> str:
        return f"Member {self.name} ({len(self._borrowed)} books borrowed)"


# Q19. PremiumMember — override only what changes
# WHY not rewrite everything: call super().borrow() with a different limit
# Clean pattern: override the limit, reuse parent logic
class PremiumMember(Member):
    def borrow(self, book: Book) -> str:
        if len(self._borrowed) >= 10:
            return "Borrow limit reached"
        self._borrowed.append(book)
        return f"Borrowed '{book.title}'"

    def __str__(self) -> str:
        return f"Premium Member {self.name} ({len(self._borrowed)} books borrowed)"


# ══════════════════════════════════════════════════════════════════
#  SECTION 7 — TRICKY CONCEPT: Class var vs Instance var
# ══════════════════════════════════════════════════════════════════
#
#  Version A:  Counter.count += 1  → modifies the CLASS variable
#              Both instances share it. Counter.count = 2. ✓
#
#  Version B:  self.count += 1
#              Python reads self.count (falls back to class var = 0)
#              then CREATES a new instance variable self.count = 1
#              The class variable is untouched. Counter.count stays 0.
#              Each instance gets its own count = 1.
#
#  MEMORY HOOK: "self.x = value always creates/updates INSTANCE variable.
#               To touch the class variable, use ClassName.x"
# ──────────────────────────────────────────────────────────────────

class _CounterA:
    count = 0
    def __init__(self):
        _CounterA.count += 1            # ← class variable modified

class _CounterB:
    count = 0
    def __init__(self):
        self.count += 1                 # ← reads class var (0), creates instance var (1)


# ══════════════════════════════════════════════════════════════════
#  SECTION 8 — GENERATORS & ITERATORS
# ══════════════════════════════════════════════════════════════════
#
#  WHAT: a function that uses yield instead of return.
#  Produces values ONE AT A TIME. Pauses at each yield.
#  Only computes the next value when you ask for it.
#
#  WHY less memory:
#    List comprehension: builds everything in RAM at once
#    Generator: holds only the CURRENT value in memory
#    For 1 million items: list = ~8MB, generator = ~200 bytes
#
#  MEMORY HOOK: "yield = pause and hand off. resume when next() is called."
#
#  A generator object has __next__ — that's what for loops call.
# ──────────────────────────────────────────────────────────────────

# Q21a. countdown — yield each number down to 1
def countdown(n: int):
    while n >= 1:
        yield n
        n -= 1
# list(countdown(5)) → [5, 4, 3, 2, 1]


# Q21b. infinite generator — runs forever, use islice to take N
def infinite_squares():
    n = 1
    while True:
        yield n * n
        n += 1
# list(islice(infinite_squares(), 5)) → [1, 4, 9, 16, 25]


# Q21c. chunked string reader
def read_in_chunks(text: str, size: int):
    for i in range(0, len(text), size):
        yield text[i:i+size]
# list(read_in_chunks("abcdefg", 3)) → ["abc", "def", "g"]


# ══════════════════════════════════════════════════════════════════
#  SECTION 9 — TYPE HINTS
# ══════════════════════════════════════════════════════════════════
#
#  WHAT: annotations that describe what types a function expects/returns.
#  Python does NOT enforce them at runtime — they're for readability + mypy.
#
#  SYNTAX:
#    def func(x: int, y: str = "hi") -> bool:
#
#  COMMON TYPES:
#    list[int]          → list of ints (Python 3.9+)
#    dict[str, int]     → dict mapping str keys to int values
#    int | None         → either int or None (Python 3.10+)
#    Optional[int]      → same as int | None (needs: from typing import Optional)
#    tuple[int, str]    → tuple with specific types
#    **kwargs: str      → all keyword args are strings
#
#  Optional[int] means: this can be an int OR None.
#  Python 3.10+: write int | None instead of Optional[int] (no import needed)
# ──────────────────────────────────────────────────────────────────

def greet(name: str) -> str:
    return f"Hello, {name}!"

def total(numbers: list[int]) -> int:
    return sum(numbers)

def lookup(data: dict[str, int], key: str) -> int | None:
    return data.get(key)

def describe_model(name: str, **kwargs: str) -> str:
    params = ", ".join(f"{k}={v}" for k, v in kwargs.items())
    return f"Model: {name}, params: {params}"


# ══════════════════════════════════════════════════════════════════
#  DUNDER METHODS — QUICK REFERENCE
# ══════════════════════════════════════════════════════════════════
#
#  These make your class work with Python's built-in operators/functions.
#
#  __str__    → str(obj), print(obj)           — human-readable string
#  __repr__   → repr(obj), shown in debugger   — developer-readable string
#  __len__    → len(obj)
#  __eq__     → obj1 == obj2
#  __add__    → obj1 + obj2
#  __lt__     → obj1 < obj2  (enables sorting)
#  __getitem__→ obj[key]
#  __iter__   → for x in obj
#  __enter__  → with obj as x   (context manager setup)
#  __exit__   → end of with block (context manager teardown)
#
#  MEMORY HOOK: "dunder = double underscore = magic = Python protocol"
#
# Example:
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    def __repr__(self):
        return f"Vector({self.x}, {self.y})"
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
# Vector(1,2) + Vector(3,4) → Vector(4,6)
# Vector(1,2) == Vector(1,2) → True


# ══════════════════════════════════════════════════════════════════
#  MRO — METHOD RESOLUTION ORDER
# ══════════════════════════════════════════════════════════════════
#
#  When you call a method, Python searches in this order:
#    1. The instance itself
#    2. The class
#    3. Parent classes (left to right, depth first, C3 linearization)
#
#  Check it: ClassName.__mro__
#
#  Example:
#    class A: pass
#    class B(A): pass
#    class C(B): pass
#    C.__mro__ → (C, B, A, object)
#
#  MEMORY HOOK: "Python walks UP the family tree, left to right"


# ══════════════════════════════════════════════════════════════════
#  FINAL SCORE — ALL CHECKS HERE
# ══════════════════════════════════════════════════════════════════

passed = 0
failed = 0
skipped = 0

def check(label, got, expected):
    global passed, failed
    if got == expected:
        print(f"  ✓  {label}")
        passed += 1
    else:
        print(f"  ✗  {label}")
        print(f"       expected : {expected!r}")
        print(f"       you got  : {got!r}")
        failed += 1

def not_done(label):
    global skipped
    print(f"  -  {label}  (not written yet)")
    skipped += 1


print("\n── SECTION 1 : Fundamentals ─────────────────────────────────")
check("Q1a word_frequency basic",     word_frequency("the cat and The dog"), {"the":2,"cat":1,"and":1,"dog":1})
check("Q1b word_frequency repeat",    word_frequency("hi hi hi"),            {"hi":3})
check("Q1c word_frequency empty",     word_frequency(""),                    {})

check("Q2a group_anagrams",           group_anagrams(["eat","tea","tan","ate","nat","bat"]),
                                      {"aet":["eat","tea","ate"],"ant":["tan","nat"],"abt":["bat"]})
check("Q2b group_anagrams empty",     group_anagrams([]),                    {})

check("Q3a compress runs",            compress("aaabbc"),                    "a3b2c1")
check("Q3b compress no repeats",      compress("abc"),                       "a1b1c1")
check("Q3c compress empty",           compress(""),                          "")
check("Q3d compress resets",          compress("abba"),                      "a1b2a1")

check("Q4a chunk_list",               chunk_list([1,2,3,4,5], 2),            [[1,2],[3,4],[5]])
check("Q4b chunk_list exact",         chunk_list([1,2,3], 3),                [[1,2,3]])
check("Q4c chunk_list empty",         chunk_list([], 4),                     [])

check("Q5a second_largest",           second_largest([4,1,7,3]),             4)
check("Q5b second_largest dupes",     second_largest([5,5,2]),               2)
check("Q5c second_largest none",      second_largest([5,5]),                 None)

print("\n── SECTION 2 : Lambdas / Comprehensions ─────────────────────")
check("Q6  sort_students",            sort_students([("Anu",90,25),("Ravi",90,22),("Bala",80,30)]),
                                      ["Ravi","Anu","Bala"])
check("Q7  filter_zip_dict",          filter_zip_dict(["a","b","c","d"],[10,60,90,30]),
                                      {"b":60,"c":90})
check("Q8a sum list == gen",          sum_odd_squares_list(1_000_000),
                                      sum_odd_squares_gen(1_000_000))

print("\n── SECTION 3 : Decorators ───────────────────────────────────")
check("Q9  timer preserves name",     slow.__name__,                         "slow")
_call_count = 0
check("Q10 retry succeeds on 3rd",    flaky(),                               "ok")

print("\n── SECTION 4 : Error Handling ───────────────────────────────")
try:
    check("Q11a valid payment",       process_payment(1000, 500, "4111111111111111"),
                                      "payment of 500 successful. remaining balance : 500")
    try:
        process_payment(1000, 1500, "5200000000000000")
        check("Q11b insufficient", False, True)
    except InsufficientFundsError as e:
        check("Q11b balance stored",  e.balance,  1000)
        check("Q11c amount stored",   e.amount,   1500)
    try:
        process_payment(1000, 500, "9999999999999999")
        check("Q11d invalid card", False, True)
    except InvalidCardError:
        check("Q11d invalid card raised", True, True)
except Exception as e:
    not_done(f"Q11 custom exceptions — error: {e}")

try:
    with DatabaseConnection() as db:
        db.query("SELECT * FROM users")
    check("Q12a connected=False after with", db.connected, False)
    try:
        db.query("SELECT * FROM products")
        check("Q12b RuntimeError outside with", False, True)
    except RuntimeError:
        check("Q12b RuntimeError raised", True, True)
except Exception as e:
    not_done(f"Q12 context manager — error: {e}")

print("\n── SECTION 5 : OOP ──────────────────────────────────────────")
try:
    b = BankAccount("Nitu", 500)
    check("Q13a deposit",             b.deposit(200),                        700)
    check("Q13b withdraw",            b.withdraw(100),                       600)
    check("Q13c insufficient",        b.withdraw(9999),                      "Insufficient funds")
    check("Q13d __str__",             str(b),                                "Account[Nitu]: ₹600")
except Exception as e:
    not_done(f"Q13 BankAccount — {e}")

try:
    s = SavingsAccount("Nitu", 1000)
    check("Q14a deposit inherited",   s.deposit(500),                        1500)
    check("Q14b add_interest",        s.add_interest(),                      1575.0)
    check("Q14c __str__ inherited",   str(s),                                "Account[Nitu]: ₹1575.0")
except Exception as e:
    not_done(f"Q14 SavingsAccount — {e}")

try:
    t = Temperature(0)
    check("Q15a fahrenheit 0°C",      t.fahrenheit,                          32.0)
    t2 = Temperature(100)
    check("Q15b fahrenheit 100°C",    t2.fahrenheit,                         212.0)
    t.fahrenheit = 212
    check("Q15c setter → celsius",    round(t._celsius, 2),                  100.0)
except Exception as e:
    not_done(f"Q15 Temperature — {e}")

try:
    c = Circle(5)
    check("Q16a radius",              c.radius,                              5)
    check("Q16b diameter",            c.diameter,                            10)
    check("Q16c area",                c.area,                                78.54)
    c.radius = -1
    check("Q16d negative rejected",   c.radius,                              5)
    c.radius = 3
    check("Q16e diameter updates",    c.diameter,                            6)
except Exception as e:
    not_done(f"Q16 Circle — {e}")

print("\n── SECTION 6 : OOP Mini Project ─────────────────────────────")
try:
    Book.total_books = 0
    b1 = Book("Dune", "Herbert", 412)
    b2 = Book("Hi", "X", 100)
    check("Q17a title",               b1.title,                              "Dune")
    check("Q17b __str__",             str(b1),                               "'Dune' by Herbert (412 pages)")
    check("Q17c is_long True",        b1.is_long,                            True)
    check("Q17d is_long False",       b2.is_long,                            False)
    check("Q17e total_books",         Book.total_books,                      2)
except Exception as e:
    not_done(f"Q17 Book — {e}")

try:
    Book.total_books = 0
    bk1 = Book("Dune","H",412); bk2 = Book("A","B",50)
    bk3 = Book("C","D",200);    bk4 = Book("E","F",100)
    m = Member("Nitu")
    check("Q18a borrow",              m.borrow(bk1),                         "Borrowed 'Dune'")
    m.borrow(bk2); m.borrow(bk3)
    check("Q18b borrow limit",        m.borrow(bk4),                         "Borrow limit reached")
    check("Q18c return book",         m.return_book(bk1),                    "Returned 'Dune'")
    check("Q18d book not found",      m.return_book(bk1),                    "Book not found")
    check("Q18e __str__",             str(m),                                "Member Nitu (2 books borrowed)")
except Exception as e:
    not_done(f"Q18 Member — {e}")

try:
    Book.total_books = 0
    books = [Book(f"Book{i}", "X", 100) for i in range(10)]
    pm = PremiumMember("Anu")
    for bk in books:
        pm.borrow(bk)
    check("Q19a premium limit 10",    len(pm.borrowed),                      10)
    check("Q19b premium limit hit",   pm.borrow(Book("Extra","X",50)),       "Borrow limit reached")
    check("Q19c premium __str__",     str(pm),                               "Premium Member Anu (10 books borrowed)")
except Exception as e:
    not_done(f"Q19 PremiumMember — {e}")

print("\n── SECTION 7 : Tricky Concept ───────────────────────────────")
_CounterA.count = 0
ca1 = _CounterA(); ca2 = _CounterA()
check("Q20a Version A class count",   _CounterA.count,                       2)

_CounterB.count = 0
cb1 = _CounterB(); cb2 = _CounterB()
check("Q20b Version B class unchanged", _CounterB.count,                     0)
check("Q20c Version B instance count",  cb1.count,                           1)
check("Q20d Version B each own",        cb2.count,                           1)

print("\n── SECTION 8 : Generators ───────────────────────────────────")
try:
    check("Q21a countdown(5)",          list(countdown(5)),                  [5,4,3,2,1])
    check("Q21b countdown(1)",          list(countdown(1)),                  [1])
    check("Q21c infinite_squares 5",    list(islice(infinite_squares(),5)),  [1,4,9,16,25])
    check("Q21d read_in_chunks",        list(read_in_chunks("abcdefg",3)),   ["abc","def","g"])
    check("Q21e read_in_chunks exact",  list(read_in_chunks("abcdef",3)),    ["abc","def"])
    check("Q21f countdown is generator",hasattr(countdown(3),'__next__'),    True)
    check("Q21g infinite is generator", hasattr(infinite_squares(),'__next__'), True)
except Exception as e:
    not_done(f"Q21 generators — {e}")

print("\n── SECTION 9 : Type Hints ───────────────────────────────────")
try:
    check("Q22a greet",               greet("Nitu"),                         "Hello, Nitu!")
    check("Q22b total",               total([1,2,3,4]),                      10)
    check("Q22c lookup found",        lookup({"a":1,"b":2}, "a"),            1)
    check("Q22d lookup missing",      lookup({"a":1}, "z"),                  None)
    check("Q22e describe_model",      describe_model("GPT-4", temperature="0.7", max_tokens="512"),
                                      "Model: GPT-4, params: temperature=0.7, max_tokens=512")
    check("Q22f describe no kwargs",  describe_model("Llama"),               "Model: Llama, params: ")
    check("Q22g greet has annotation",'return' in greet.__annotations__,     True)
    check("Q22h total has annotation", len(total.__annotations__) >= 2,      True)
except Exception as e:
    not_done(f"Q22 type hints — {e}")


# ── FINAL SCORE ───────────────────────────────────────────────────
total_q = passed + failed
print(f"\n{'═'*58}")
print(f"  RESULT : {passed} passed  /  {total_q} attempted  /  {skipped} skipped")
if failed == 0 and skipped == 0:
    print("  🎉 Full marks. Python is solid. Move on.")
elif failed == 0:
    print(f"  ✓ No failures — fill in the {skipped} skipped question(s) next.")
else:
    print(f"  Fix the {failed} failing question(s). Work section by section.")
print('═'*58)