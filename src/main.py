
# src/main.py
from book import Book
from user import User
from transaction import Transaction
from database import Database

def main():
    db = Database()
    db.setup()

    # Example interaction
    book1 = Book("Python Programming", "Guido van Rossum", 2023)
    db.add_book(book1)

    user1 = User("John Doe", "john@example.com")
    db.add_user(user1)

    transaction = Transaction(user1, book1)
    db.borrow_book(transaction)

    print("Library Management System")

if __name__ == "__main__":
    main()
