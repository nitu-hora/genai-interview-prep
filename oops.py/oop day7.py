"""
OOP DAY 7 — Mini Project: Library System
=========================================
CONCEPT REVIEW (everything from Day 1-6):
    Day 1: __init__, attributes
    Day 2: methods, __str__
    Day 3: class variables
    Day 4: inheritance
    Day 5: method overriding, super()
    Day 6: encapsulation, @property

TODAY: Build a small library system using all of it.
No starter code — read the spec and build from scratch.
This is interview style.

Run:  python oop_day7.py
"""


# ============================================================
# PART 1: Book class
# ============================================================
# Attributes: title, author, pages
# Class variable: total_books (count of all Book objects ever created)
# __str__: "'{title}' by {author} ({pages} pages)"
# is_long property: True if pages > 300, else False
#
# Book("Dune", "Herbert", 412).title      ->  "Dune"
# str(Book("Dune", "Herbert", 412))       ->  "'Dune' by Herbert (412 pages)"
# Book("Dune", "Herbert", 412).is_long    ->  True
# Book("Hi", "X", 100).is_long            ->  False
# Book.total_books  (after creating 2)    ->  2

class Book:
    pass


# ============================================================
# PART 2: Member class
# ============================================================
# Attributes: name, _borrowed (private list, starts empty)
# borrowed property: returns copy of _borrowed list
# borrow(book) -> adds Book object to _borrowed; max 3 books allowed
#                 if already 3: return "Borrow limit reached"
#                 else: return f"Borrowed '{book.title}'"
# return_book(book) -> removes from _borrowed if present
#                      return f"Returned '{book.title}'"
#                      if not in list: return "Book not found"
# __str__: "Member {name} ({len} books borrowed)"
#
# m = Member("Nitu")
# b1 = Book("Dune", "Herbert", 412)
# m.borrow(b1)     ->  "Borrowed 'Dune'"
# m.borrowed       ->  [b1]
# m.return_book(b1)->  "Returned 'Dune'"
# m.borrowed       ->  []

class Member:
    pass


# ============================================================
# PART 3: PremiumMember (inherits Member)
# ============================================================
# Same as Member but borrow limit is 10 instead of 3.
# Override borrow() to use limit 10.
# __str__: "Premium Member {name} ({len} books borrowed)"
#
# pm = PremiumMember("Anu")
# (can borrow up to 10 books)

class PremiumMember(Member):
    pass


# ============================================================
# PART 4: Library class
# ============================================================
# Attributes: name, _books (private list of Book objects)
# add_book(book)     -> adds to _books; return f"Added '{book.title}'"
# remove_book(book)  -> removes if present; return f"Removed '{book.title}'"
#                       if not found: return "Book not found"
# search(title)      -> returns Book object if found (case-insensitive), else None
# books property     -> returns copy of _books
# __str__: "Library '{name}': {count} books"
#
# lib = Library("City Library")
# b = Book("Dune", "Herbert", 412)
# lib.add_book(b)          ->  "Added 'Dune'"
# lib.search("dune")       ->  b   (the Book object)
# lib.search("xyz")        ->  None
# str(lib)                 ->  "Library 'City Library': 1 books"

class Library:
    pass


# ---------------------------------------------------------------- self-check
def _check():
    # reset class counter for clean test
    Book.total_books = 0

    b1 = Book("Dune", "Herbert", 412)
    b2 = Book("Hi", "X", 100)
    b3 = Book("A", "B", 50)
    b4 = Book("C", "D", 200)

    m = Member("Nitu")
    m.borrow(b1)
    borrow2 = m.borrow(b2)
    m.borrow(b3)
    borrow_limit = m.borrow(b4)
    ret = m.return_book(b1)
    ret_missing = m.return_book(b1)

    pm = PremiumMember("Anu")
    for book in [b1, b2, b3, b4]:
        pm.borrow(book)

    lib = Library("City Library")
    lib.add_book(b1)
    lib.add_book(b2)

    tests = [
        ("P1 Book.title",         lambda: b1.title == "Dune"),
        ("P1 Book.__str__",       lambda: str(b1) == "'Dune' by Herbert (412 pages)"),
        ("P1 Book.is_long True",  lambda: b1.is_long == True),
        ("P1 Book.is_long False", lambda: b2.is_long == False),
        ("P1 Book.total_books",   lambda: Book.total_books == 4),
        ("P2 Member.borrow",      lambda: borrow2 == "Borrowed 'Hi'"),
        ("P2 Member limit",       lambda: borrow_limit == "Borrow limit reached"),
        ("P2 Member.return_book", lambda: ret == "Returned 'Dune'"),
        ("P2 Member not found",   lambda: ret_missing == "Book not found"),
        ("P2 Member.__str__",     lambda: str(m) == "Member Nitu (2 books borrowed)"),
        ("P3 Premium limit 10",   lambda: len(pm.borrowed) == 4),
        ("P3 Premium.__str__",    lambda: "Premium Member Anu" in str(pm)),
        ("P4 Library.add_book",   lambda: lib.add_book(b3) == "Added 'A'"),
        ("P4 Library.search",     lambda: lib.search("dune") == b1),
        ("P4 Library.search None",lambda: lib.search("xyz") is None),
        ("P4 Library.__str__",    lambda: "City Library" in str(lib)),
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
    if passed == len(tests):
        print("\n🎉 Full OOP week complete. You built a working library system from scratch.")

if __name__ == "__main__":
    _check()