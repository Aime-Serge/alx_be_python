class Book:
    """A class representing a book with basic metadata and magic methods."""

    def __init__(self, title, author):
        """Initialize book attributes."""
        self.title = title
        self.author = author

    def __str__(self):
        """Return a user-friendly string representation."""
        return f"{self.title} by {self.author}"

    def __repr__(self):
        """Return an official string representation (useful for debugging)."""
        return f"Book('{self.title}', '{self.author}')"

    def __del__(self):
        """Destructor called when an object is deleted."""
        print(f"Deleting {self.title}")


class EBook(Book):
    """A subclass representing an electronic book."""

    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        """Return a user-friendly string representation."""
        return f"{self.title} by {self.author}, File Size: {self.file_size}KB"

    def __repr__(self):
        """Return an official string representation."""
        return f"EBook('{self.title}', '{self.author}', {self.file_size})"


class PrintBook(Book):
    """A subclass representing a printed book."""

    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        """Return a user-friendly string representation."""
        return f"{self.title} by {self.author}, Page Count: {self.page_count}"

    def __repr__(self):
        """Return an official string representation."""
        return f"PrintBook('{self.title}', '{self.author}', {self.page_count})"


class Library:
    """A class representing a library that manages books."""

    def __init__(self):
        self.books = []

    def add_book(self, book):
        """Add a book instance (Book, EBook, or PrintBook) to the library."""
        if isinstance(book, Book):
            self.books.append(book)
        else:
            raise TypeError("Only Book or its subclasses can be added.")

    def list_books(self):
        """List all books currently in the library."""
        for book in self.books:
            print(book)

