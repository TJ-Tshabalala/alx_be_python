class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def is_checked_out(self):
        return self.is_checked_out
class Library:
    def __init__(self):
        self._books =[]

    def AddBook(self,book):
        self._books.append(book)
    
    def check_out(self,title):

        for book in self._books:
            if book.title == title and not book._is_checked_out():
                book._is_checked_out = True
                return f"Successfully checked out '{title}'"
            return f"Sorry, '{title}' is not available for checkout."
    def return_book(self):

        for book in self._books:
            if book.title == title and not book.is_checked_out():
                book._is_checked_out = False
                return f"Successfully returned '{self.title}'"
        return f"Sorry, '{self.title}' is not currently checked out."
    def list_available_books(self):

        available_books = []
        for book in self._books:
            if not book.is_checked_out():
                available_books.append(book.title)
            return available_books