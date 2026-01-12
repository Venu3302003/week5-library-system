from library_system.book import Book

def test_book_creation():
    book = Book("Test", "Author", "123", 2024)
    assert book.available is True
