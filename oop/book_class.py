class Book:
    """A class representing a book with title, author, and publication year."""

    def __init__(self, title, author, year):
        """Constructor to initialize the book attributes."""
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        """User-friendly string representation of the book."""
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """Official string representation of the book."""
        return f"Book('{self.title}', '{self.author}', {self.year})"

    def __del__(self):
        """Destructor method called when a Book instance is deleted."""
        print(f"Deleting {self.title}")