#!/usr/bin/python3
"""
Library system demonstrating inheritance, composition, and __str__ methods
"""

class Book:
    """Base class for books"""

    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"Book: {self.title} by {self.author}"

    def details(self):
        """Optional: same as __str__ for compatibility"""
        return str(self)


class EBook(Book):
    """Derived class for eBooks"""

    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"

    def details(self):
        return str(self)


class PrintBook(Book):
    """Derived class for Print books"""

    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"

    def details(self):
        return str(self)


class Library:
    """Library class demonstrating composition"""

    def __init__(self):
        self.books = []

    def add_book(self, book):
        """Add a Book, EBook, or PrintBook instance"""
        self.books.append(book)

    def list_books(self):
        """Print details of all books in the library"""
        for book in self.books:
            print(book)  # print() will automatically call __str__()