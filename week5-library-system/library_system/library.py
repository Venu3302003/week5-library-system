import json
import os
from library_system.book import Book
from library_system.member import Member

BOOK_FILE = "data/books.json"
MEMBER_FILE = "data/members.json"

class Library:
    def __init__(self):
        self.books = {}
        self.members = {}
        self.load_data()

    def load_data(self):
        if os.path.exists(BOOK_FILE):
            with open(BOOK_FILE, "r") as f:
                data = json.load(f)
                for isbn, book in data.items():
                    self.books[isbn] = Book.from_dict(book)

        if os.path.exists(MEMBER_FILE):
            with open(MEMBER_FILE, "r") as f:
                data = json.load(f)
                for mid, member in data.items():
                    self.members[mid] = Member.from_dict(member)

    def save_data(self):
        with open(BOOK_FILE, "w") as f:
            json.dump({k: v.to_dict() for k, v in self.books.items()}, f, indent=4)

        with open(MEMBER_FILE, "w") as f:
            json.dump({k: v.to_dict() for k, v in self.members.items()}, f, indent=4)

    def add_book(self, title, author, isbn, year):
        self.books[isbn] = Book(title, author, isbn, year)

    def register_member(self, name, member_id):
        self.members[member_id] = Member(name, member_id)

    def borrow_book(self, isbn, member_id):
        if isbn not in self.books or member_id not in self.members:
            return "Invalid book or member"

        book = self.books[isbn]
        member = self.members[member_id]

        success, msg = book.borrow(member_id)
        if success:
            member.borrow_book(isbn)
        return msg

    def return_book(self, isbn, member_id):
        book = self.books[isbn]
        member = self.members[member_id]

        book.return_book()
        member.return_book(isbn)
        return "Book returned"
