# src/database.py
import mysql.connector
from book import Book
from user import User
from transaction import Transaction

class Database:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host='localhost',
            user='yourusername',
            password='yourpassword',
            database='library'
        )
        self.cursor = self.connection.cursor()

    def setup(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS books (title VARCHAR(255), author VARCHAR(255), year INT)")
        self.cursor.execute("CREATE TABLE IF NOT EXISTS users (name VARCHAR(255), email VARCHAR(255))")
        self.cursor.execute("CREATE TABLE IF NOT EXISTS transactions (user_name VARCHAR(255), book_title VARCHAR(255), borrow_date DATETIME, return_date DATETIME)")

    def add_book(self, book):
        sql = "INSERT INTO books (title, author, year) VALUES (%s, %s, %s)"
        val = (book.title, book.author, book.year)
        self.cursor.execute(sql, val)
        self.connection.commit()

    def add_user(self, user):
        sql = "INSERT INTO users (name, email) VALUES (%s, %s)"
        val = (user.name, user.email)
        self.cursor.execute(sql, val)
        self.connection.commit()

    def borrow_book(self, transaction):
        sql = "INSERT INTO transactions (user_name, book_title, borrow_date) VALUES (%s, %s, %s)"
        val = (transaction.user.name, transaction.book.title, transaction.borrow_date)
        self.cursor.execute(sql, val)
        self.connection.commit()

    def close(self):
        self.connection.close()
