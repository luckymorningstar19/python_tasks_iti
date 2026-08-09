import csv
import os
from abc import ABC, abstractmethod

class LibraryError(Exception):
    """Base class for all library-related exceptions."""


class BookNotFoundError(LibraryError):
    """Raised when a referenced Book ID does not exist in the catalog."""


class BookNotAvailableError(LibraryError):
    """Raised when trying to borrow a book with zero available copies."""


class BookNotBorrowedError(LibraryError):
    """Raised when trying to return a book the user never borrowed."""


class BorrowLimitExceededError(LibraryError):
    """Raised when a user tries to borrow more books than their role allows."""


class InvalidChoiceError(LibraryError):
    """Raised when a menu choice is out of the valid range."""


# Book
class Book:
    """Represents a single title in the library catalog (Encapsulation)."""

    def __init__(self, book_id, title, author, category, available_copies):
        self._book_id = book_id
        self._title = title
        self._author = author
        self._category = category
        self._available_copies = int(available_copies)
        self._total_copies = int(available_copies)

    @property
    def book_id(self):
        return self._book_id

    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    @property
    def category(self):
        return self._category

    @property
    def available_copies(self):
        return self._available_copies

    @property
    def total_copies(self):
        return self._total_copies

    def display_info(self):
        status = "Available" if self._available_copies > 0 else "Not Available"
        print(f"[{self._book_id}] {self._title} by {self._author} "
              f"| Category: {self._category} "
              f"| Copies: {self._available_copies}/{self._total_copies} | {status}")

    def borrow_book(self):
        """Decrease the available copy count. Raises if none are left."""
        if self._available_copies <= 0:
            raise BookNotAvailableError(f"'{self._title}' has no available copies right now.")
        self._available_copies -= 1

    def return_book(self):
        """Increase the available copy count (never above total_copies)."""
        if self._available_copies >= self._total_copies:
            raise LibraryError(f"'{self._title}' is already fully returned.")
        self._available_copies += 1

# User (Abstract Parent Class)
class User(ABC):
    """Abstract base class for every person who uses the system (Abstraction)."""

    def __init__(self, user_id, name):
        self._user_id = user_id
        self._name = name

    @property
    def user_id(self):
        return self._user_id

    @property
    def name(self):
        return self._name

    @abstractmethod
    def borrow(self, library, book_id):
        """Attempt to borrow a book. Behavior differs per role."""
        raise NotImplementedError

    @abstractmethod
    def return_book(self, library, book_id):
        """Attempt to return a book. Behavior differs per role."""
        raise NotImplementedError

    @abstractmethod
    def show_menu(self, library):
        """Display the role-specific menu loop."""
        raise NotImplementedError

def _borrow_book(user, library, book_id, max_books, role_label):
    borrowed = library.get_borrowed_list(user.user_id)
    if len(borrowed) >= max_books:
        raise BorrowLimitExceededError(
            f"{role_label}s can borrow at most {max_books} books at a time.")
    book = library.find_book(book_id)
    book.borrow_book()
    borrowed.append(book_id)
    print(f"'{book.title}' borrowed successfully.")


def _return_book(user, library, book_id):
    borrowed = library.get_borrowed_list(user.user_id)
    if book_id not in borrowed:
        raise BookNotBorrowedError("You did not borrow this book, so it cannot be returned.")
    book = library.find_book(book_id)
    book.return_book()
    borrowed.remove(book_id)
    print(f"'{book.title}' returned successfully.")


# Student (Child Class)
class Student(User):
    """A Student may borrow a maximum of 3 books at a time."""

    MAX_BOOKS = 3

    def borrow(self, library, book_id):
        _borrow_book(self, library, book_id, self.MAX_BOOKS, "Student")

    def return_book(self, library, book_id):
        _return_book(self, library, book_id)

    def show_menu(self, library):
        while True:
            print(f"\n--- Student Menu ({self.name}) ---")
            print("1. Borrow a book")
            print("2. Return a book")
            print("3. Display all books")
            print("4. Display available books")
            print("5. Display my borrowed books")
            print("6. Logout")
            choice = get_int_input("Choose an option: ")
            try:
                if choice == 1:
                    self.borrow(library, get_str_input("Enter Book ID to borrow: "))
                elif choice == 2:
                    self.return_book(library, get_str_input("Enter Book ID to return: "))
                elif choice == 3:
                    library.display_all_books()
                elif choice == 4:
                    library.display_available_books()
                elif choice == 5:
                    library.display_borrowed_books(self.user_id)
                elif choice == 6:
                    print("Logging out...")
                    break
                else:
                    raise InvalidChoiceError("Please choose a valid option (1-6).")
            except LibraryError as e:
                print(f"Error: {e}")


# Teacher (Child Class)
class Teacher(User):
    """A Teacher may borrow a maximum of 5 books at a time."""

    MAX_BOOKS = 5

    def borrow(self, library, book_id):
        _borrow_book(self, library, book_id, self.MAX_BOOKS, "Teacher")

    def return_book(self, library, book_id):
        _return_book(self, library, book_id)

    def show_menu(self, library):
        while True:
            print(f"\n--- Teacher Menu ({self.name}) ---")
            print("1. Borrow a book")
            print("2. Return a book")
            print("3. Display all books")
            print("4. Display available books")
            print("5. Display my borrowed books")
            print("6. Logout")
            choice = get_int_input("Choose an option: ")
            try:
                if choice == 1:
                    self.borrow(library, get_str_input("Enter Book ID to borrow: "))
                elif choice == 2:
                    self.return_book(library, get_str_input("Enter Book ID to return: "))
                elif choice == 3:
                    library.display_all_books()
                elif choice == 4:
                    library.display_available_books()
                elif choice == 5:
                    library.display_borrowed_books(self.user_id)
                elif choice == 6:
                    print("Logging out...")
                    break
                else:
                    raise InvalidChoiceError("Please choose a valid option (1-6).")
            except LibraryError as e:
                print(f"Error: {e}")


# Librarian (Child Class)
class Librarian(User):
    """A Librarian manages the catalog: add, remove, search, view books."""

    def borrow(self, library, book_id):
        print("Librarians manage the catalog and do not borrow books.")

    def return_book(self, library, book_id):
        print("Librarians manage the catalog and do not return books.")

    def add_book(self, library):
        book_id = get_str_input("Enter new Book ID: ")
        title = get_str_input("Enter Title: ")
        author = get_str_input("Enter Author: ")
        category = get_str_input("Enter Category: ")
        copies = get_int_input("Enter number of copies: ")
        library.add_book(Book(book_id, title, author, category, copies))

    def remove_book(self, library):
        book_id = get_str_input("Enter Book ID to remove: ")
        library.remove_book(book_id)

    def search_books(self, library):
        keyword = get_str_input("Enter a title/author/category keyword: ")
        library.search_books(keyword)

    def show_menu(self, library):
        while True:
            print(f"\n--- Librarian Menu ({self.name}) ---")
            print("1. Add a new book")
            print("2. Remove a book")
            print("3. Search books")
            print("4. View all books")
            print("5. Display available books")
            print("6. Display all borrowed books")
            print("7. Save catalog to file (books.csv)")
            print("8. Logout")
            choice = get_int_input("Choose an option: ")
            try:
                if choice == 1:
                    self.add_book(library)
                elif choice == 2:
                    self.remove_book(library)
                elif choice == 3:
                    self.search_books(library)
                elif choice == 4:
                    library.display_all_books()
                elif choice == 5:
                    library.display_available_books()
                elif choice == 6:
                    library.display_borrowed_books()
                elif choice == 7:
                    library.save_to_csv()
                elif choice == 8:
                    print("Logging out...")
                    break
                else:
                    raise InvalidChoiceError("Please choose a valid option (1-8).")
            except LibraryError as e:
                print(f"Error: {e}")


# Library
class Library:
    """Owns the book catalog and borrow records. All access goes through methods."""

    def __init__(self):
        self._books = {}           
        self._borrowed_records = {} 

    def add_book(self, book):
        if book.book_id in self._books:
            raise LibraryError(f"Book ID '{book.book_id}' already exists in the catalog.")
        self._books[book.book_id] = book
        print(f"Book '{book.title}' added to the catalog.")

    def remove_book(self, book_id):
        if book_id not in self._books:
            raise BookNotFoundError(f"No book found with ID '{book_id}'.")
        removed = self._books.pop(book_id)
        print(f"Book '{removed.title}' removed from the catalog.")

    def find_book(self, book_id):
        book = self._books.get(book_id)
        if book is None:
            raise BookNotFoundError(f"No book found with ID '{book_id}'.")
        return book

    def search_books(self, keyword):
        keyword = keyword.lower()
        results = [b for b in self._books.values()
                   if keyword in b.title.lower()
                   or keyword in b.author.lower()
                   or keyword in b.category.lower()]
        if not results:
            print("No books matched your search.")
        else:
            print(f"\nFound {len(results)} matching book(s):")
            for b in results:
                b.display_info()

    def display_all_books(self):
        if not self._books:
            print("The catalog is empty.")
            return
        print("\n--- All Books ---")
        for b in self._books.values():
            b.display_info()

    def display_available_books(self):
        available = [b for b in self._books.values() if b.available_copies > 0]
        if not available:
            print("No books are currently available.")
            return
        print("\n--- Available Books ---")
        for b in available:
            b.display_info()

    def display_borrowed_books(self, user_id=None):
        if user_id is not None:
            ids = self._borrowed_records.get(user_id, [])
            if not ids:
                print("You have not borrowed any books.")
                return
            print("\n--- Your Borrowed Books ---")
            for bid in ids:
                self._books[bid].display_info()
        else:
            print("\n--- All Borrowed Books (every user) ---")
            any_borrowed = False
            for uid, ids in self._borrowed_records.items():
                for bid in ids:
                    book = self._books.get(bid)
                    if book:
                        any_borrowed = True
                        print(f"User {uid} has borrowed: {book.title} ({book.book_id})")
            if not any_borrowed:
                print("No books are currently borrowed.")

    def get_borrowed_list(self, user_id):
        return self._borrowed_records.setdefault(user_id, [])

    # --- Bonus: persistence to CSV ---
    def save_to_csv(self, filename="books.csv"):
        try:
            with open(filename, "w", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow(["book_id", "title", "author", "category",
                                  "available_copies", "total_copies"])
                for b in self._books.values():
                    writer.writerow([b.book_id, b.title, b.author, b.category,
                                      b.available_copies, b.total_copies])
            print(f"Catalog saved to '{filename}'.")
        except OSError as e:
            print(f"Could not save catalog: {e}")

    def load_from_csv(self, filename="books.csv"):
        if not os.path.exists(filename):
            return False
        try:
            with open(filename, newline="", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    book = Book(row["book_id"], row["title"], row["author"],
                                row["category"], int(row["available_copies"]))
                    book._total_copies = int(row["total_copies"])
                    self._books[book.book_id] = book
            return True
        except (OSError, KeyError, ValueError):
            return False

# Safe input helpers (prevent crashes on bad input)
def get_int_input(prompt):
    while True:
        raw = input(prompt).strip()
        try:
            return int(raw)
        except ValueError:
            print("Invalid input. Please enter a whole number.")


def get_str_input(prompt):
    while True:
        raw = input(prompt).strip()
        if raw:
            return raw
        print("Input cannot be empty. Please try again.")


# Sample data + main program loop
def load_sample_books(library):
    samples = [
        ("B001", "The Hobbit", "J.R.R. Tolkien", "Fantasy", 3),
        ("B002", "Clean Code", "Robert C. Martin", "Programming", 2),
        ("B003", "1984", "George Orwell", "Dystopian", 4),
        ("B004", "A Brief History of Time", "Stephen Hawking", "Science", 1),
        ("B005", "Introduction to Algorithms", "T. Cormen et al.", "Programming", 2),
    ]
    for book_id, title, author, category, copies in samples:
        library.add_book(Book(book_id, title, author, category, copies))


def main():
    library = Library()
    if not library.load_from_csv():
        load_sample_books(library)

    print("=" * 55)
    print("   Welcome to the Smart Library Management System")
    print("=" * 55)

    while True:
        print("\n--- Login ---")
        print("1. Librarian")
        print("2. Student")
        print("3. Teacher")
        print("4. Exit Program")
        choice = get_int_input("Select your role: ")

        if choice == 4:
            print("Thank you for using the Smart Library Management System. Goodbye!")
            break
        elif choice in (1, 2, 3):
            user_id = get_str_input("Enter your User ID: ")
            name = get_str_input("Enter your Name: ")
            if choice == 1:
                user = Librarian(user_id, name)
            elif choice == 2:
                user = Student(user_id, name)
            else:
                user = Teacher(user_id, name)
            user.show_menu(library)
        else:
            print("Invalid choice. Please select an option between 1 and 4.")


if __name__ == "__main__":
    main()
