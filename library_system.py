class Book:
    def __str__(self, title:str , author: str):
        self.title = title
        self.author = author

    # Return string representation    
    def __str__(self):
        return f"{self.title} by {self.author}"

class EBook(Book):
    def __init__(self, title,author,file_size: int):
        super().__init__(title, author)
        self.file_size = file_size
    # Return string representation
    def __str__(self):
        return f"{self.title} by {self.author} {self.file_size}"

class PrintBook(Book):
    def __init__(self, title, author, page_count: int):
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        return self.__class__.__name__(f"{self.title} by {self.author} {self.page_count}")

class Library:
    def __init__(self):
        self.books = []
    
    def add_book(self, book):
        self.books = self.books.append[book]

    def list_book(self):
        books_list = []
        for book in self.books:
            if(book, Book):
                print(f"Book: {self.title} by {self.author}")
            elif(book, EBook):
                print(f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB")
            elif(book, PrintBook):
                print(f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}")
    
