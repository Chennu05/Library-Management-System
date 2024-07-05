# src/transaction.py
from datetime import datetime

class Transaction:
    def __init__(self, user, book):
        self.user = user
        self.book = book
        self.borrow_date = datetime.now()
        self.return_date = None

    def return_book(self):
        self.return_date = datetime.now()

    def __str__(self):
        return f"{self.user.name} borrowed {self.book.title} on {self.borrow_date}"
