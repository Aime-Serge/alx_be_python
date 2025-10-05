# library_management.py

from typing import List, Optional

class Book:
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self) -> bool:
        """Return True if the checkout succeeded, False if already checked out."""
        if self._is_checked_out:
            return False
        self._is_checked_out = True
        return True

    def return_book(self) -> bool:
        """Return True if return succeeded, False if not checked out."""
        if not self._is_checked_out:
            return False
        self._is_checked_out = False
        return True

    def is_available(self) -> bool:
        return not self._is_checked_out

    def __str__(self):
        return f"{self.title} by {self.author}"

class Library:
    def __init__(self):
        self._books: List[Book] = []

    def add_book(self, book: Book):
        if not isinstance(book, Book):
            raise TypeError("Only Book instances can be added.")
        self._books.append(book)

    def _find_by_title(self, title: str) -> Optional[Book]:
        for book in self._books:
            if book.title.lower() == title.lower():
                return book
        return None

    def check_out_book(self, title: str) -> bool:
        book = self._find_by_title(title)
        if not book:
            print(f"Book '{title}' not found.")
            return False
        if not book.check_out():
            print(f"Book '{title}' is already checked out.")
            return False
        return True

    def return_book(self, title: str) -> bool:
        book = self._find_by_title(title)
        if not book:
            print(f"Book '{title}' not found.")
            return False
        if not book.return_book():
            print(f"Book '{title}' was not checked out.")
            return False
        return True

    def list_available_books(self):
        available = [b for b in self._books if b.is_available()]
        if not available:
            print("No available books.")
            return
        for b in available:
            print(str(b))
