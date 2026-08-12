class Book:
    def __init__(self,title,author,is_borrowed=False):
        self.title = title
        self.author = author
        self.is_borrowed = is_borrowed

    def borrow(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            print(f"You have borrowed '{self.title}' by {self.author}.")
        else:
            print(f"Sorry, '{self.title}' is already borrowed.")

    def return_book(self):
        if self.is_borrowed:
            self.is_borrowed = False
            print(f"You have returned '{self.title}' by {self.author}.")
        else:
            print(f"'{self.title}' was not borrowed.")

book1 = Book("1984", "George Orwell")
book1.borrow()
book1.return_book()

book2 = Book("To Kill a Mockingbird", "Harper Lee")
book2.borrow()
book2.return_book()

book3 = Book("To kill a crime", "master law")
book3.borrow()
book3.return_book()