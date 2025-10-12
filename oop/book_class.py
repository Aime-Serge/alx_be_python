class Book:
    """A class representing a book with basic metadata and magic methods."""

    def __init__(self, title: str, author: str, year: int):
        """Constructor to initialize book attributes."""
        self.title = title
        self.author = author
        self.year = year
        print(f"Book '{self.title}' created successfully!")

    def __str__(self) -> str:
        """Return a user-friendly string representation."""
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self) -> str:
        """Return an official string representation (useful for debugging)."""
        return f"Book('{self.title}', '{self.author}', {self.year})"

    def __del__(self):
        """Destructor called when an object is deleted."""
        print(f"Deleting {self.title}")
