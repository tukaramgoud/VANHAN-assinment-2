from datetime import datetime, timedelta

class Book:
    def __init__(self, title, author, isbn, genre, quantity):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.genre = genre
        self.quantity = quantity
        self.available_copies = quantity
    
    
    def is_available(self):
        return self.available_copies > 0
    
    def borrow_book(self):
        if self.available_copies > 0:
            self.available_copies -= 1
            print("{} book borrowed".format(self.title))
            return True
        else:
            print("{} book is not in the library".format(self.title))
            return False
    
    def return_book(self):
        if self.available_copies < self.quantity:
            self.available_copies += 1
            print("{} Book is returned".format(self.title))
            return True
        else:
            print("{} is Not the book You've taken".format(self.title))
            return False

class Borrower:
    def __init__(self, name, contact_details, membership_id):
        self.name = name
        self.contact_details = contact_details
        self.membership_id = membership_id
        self.borrowed_books = {}
 
    
    def borrow_book(self, book, due_date):
        if book.borrow_book():
            self.borrowed_books[book.isbn] = due_date
            print( "Book due date is {}".format(due_date))
            return True
        else:
            print( "Book not in the library")
            return False
    
    def return_book(self, book):
        if book.isbn in self.borrowed_books:
            del self.borrowed_books[book.isbn]
            book.return_book()
            print("{} Book deleted from borrowed list successfully".format(book.title))
            return True
        else:
            print("This is not the book you've taken")
            return False

class Library:
    def __init__(self):
        self.books = {}
        self.borrowers = {}
    
    def add_book(self, title, author, isbn, genre, quantity):
        if isbn in self.books:
            print("{} - Book Already exists".format(title))
            return False  # Book already exists
        else:
            new_book = Book(title, author, isbn, genre, quantity)
            self.books[isbn] = new_book
            print("{} - Book Added successfully".format(new_book.title))
            return True
    
    def update_book(self, isbn, title=None, author=None, quantity=None):
        if isbn in self.books:
            book = self.books[isbn]
            if title:
                book.title = title
            if author:
                book.author = author
            if quantity is not None:
                book.quantity = quantity
                book.available_copies = quantity
            print("{} Book Updated successfully".format(book.title))
            return True
        else:
            print("There is NO book in the library")
            return False
    
    def remove_book(self, isbn):
        if isbn in self.books:
            del self.books[isbn]
            print("{} Book removed from library".format(book.title))
            return True
        else:
            print("Enter correct book details")
            return False
    
    def add_borrower(self, name, contact_details, membership_id):
        if membership_id in self.borrowers:
            print('"{} Borrower is already exists"'.format(self.membership_id))
            return False  # Borrower already exists
        else:
            new_borrower = Borrower(name, contact_details, membership_id)
            self.borrowers[membership_id] = new_borrower
            print("A new borrower added to list")
            return  True
    
    def update_borrower(self, membership_id, name=None, contact_details=None):
        if membership_id in self.borrowers:
            borrower = self.borrowers[membership_id]
            if name:
                borrower.name = name
            if contact_details:
                borrower.contact_details = contact_details
            print("{} Borrower details are updated succesfully".format(self.membership_id))
            return True
        else:
            print("Borrower is not in the list")
            return False
    
    def remove_borrower(self, membership_id):
        if membership_id in self.borrowers:
            del self.borrowers[membership_id]
            print(" {} Borrower removed from the list".format(self.membership_id))
            return True
        else:
            print("Enter the correct borrower details")
            return False
    
    def borrow_book(self, membership_id, isbn, due_date):
        if isbn in self.books and membership_id in self.borrowers:
            borrower = self.borrowers[membership_id]
            book = self.books[isbn]
            return borrower.borrow_book(book, due_date)
        else:
            return False
    
    def return_book(self, membership_id, isbn):
        if isbn in self.books and membership_id in self.borrowers:
            borrower = self.borrowers[membership_id]
            book = self.books[isbn]
            return borrower.return_book(book)
        else:
            return False
    
    def search_books(self, keyword):
        results = []
        for isbn, book in self.books.items():
            if keyword.lower() in book.title.lower() or keyword.lower() in book.author.lower() or keyword.lower() in book.genre.lower():
                results.append((book, book.available_copies))
        return results

# Example usage:

# Create a library instance
library = Library()

# Add books to the library

library.add_book("The Secret", "Rhonda Byrne", "9780743273565", "Self-help book", 3)
library.add_book("Rich Dad Poor Dad", "Robert T. Kiyosaki Robert", "9780061120084", "Personal Finance", 5)
library.add_book("The Alchemist", "Paulo Coelho", "9780316769488", "Contemporary Fiction", 2)
library.add_book("The Secret", "Rhonda Byrne", "9780743273565", "Self-help book", 3)

# Add borrowers to the library
library.add_borrower("TukaramGoud", "tukaramgoud2804@gmail.com", "MID123")
library.add_borrower("GnaneshwarGoud", "gnany2001@gmail.com", "MID456")

# Borrow books
library.borrow_book("MID123", "9780743273565", datetime.now() + timedelta(days=14))
library.borrow_book("MID123", "9780061120084", datetime.now() + timedelta(days=21))
library.borrow_book("MID456", "9780743273565", datetime.now() + timedelta(days=14))

# Return books
library.return_book("MID123", "9780743273565")


# Search for books
search_results = library.search_books("the")
for result in search_results:
    book, available_copies = result
    print(f"{book.title} by {book.author} and belongs to genre of {book.genre} - Available Copies: {available_copies}")
