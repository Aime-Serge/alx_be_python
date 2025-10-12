class Book:
    """A class representing a book with basic metadata and magic methods."""

    def __init__(self, title, author, year):
        """Constructor to initialize book attributes."""
        self.title = title
        self.author = author
        self.year = year
        # Removed print statement to match expected output

    def __str__(self):
        """Return a user-friendly string representation."""
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """Return an official string representation (useful for debugging)."""
        return f"Book('{self.title}', '{self.author}', {self.year})"

    def __del__(self):
        """Destructor called when an object is deleted."""
        print(f"Deleting {self.title}")
