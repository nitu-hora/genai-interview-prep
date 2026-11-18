class Library:
    def __init__(self):
        self.books=[]

    def add_book(self, book):
        return self.books.append(book)

    def borrow_book(self, title):
        for book in self.books:
            if book.title == title:
                if book.is_borrowed == False:
                    book.is_borrowed = True
                    print("borrowed successfully")
                else:
                    print("book not available")
                return
        print("book not found in library")

    def return_book(self,title):
        for book in self.books:
            if book.title == title:
                    book.is_borrowed = False
                    print("returned succesfully")
            

    def show_available(self):
        for book in self.books:
            if book.is_borrowed == False:
                print(book.title)


class Books:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False


lib = Library()
b1 = Books("Atomic Habits", "James Clear")
b2 = Books("The Alchemist", "Paulo Coelho")
b3 = Books("Deep Work", "Cal Newport")
b4 = Books("1984", "George Orwell")
b5 = Books("Thinking, Fast and Slow", "Daniel Kahneman")

lib.add_book(b1)
lib.add_book(b2)
lib.add_book(b3)
print(lib.books)
lib.borrow_book("Atomic Habits")
lib.show_available()
lib.return_book("Atomic Habits")
lib.show_available()
lib.borrow_book('“1984”')