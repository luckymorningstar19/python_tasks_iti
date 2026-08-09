# Smart Library Management System

A console-based Python application for managing a public library's book
catalog, built for the Python Final Project.

## Requirements

- Python 3.8 or later
- No external libraries needed (uses only the standard library: `csv`, `os`, `abc`)

## How to Run

1. Download/clone this repository.
2. Open a terminal in the project folder.
3. Run:

   ```bash
   python library_system.py
   ```

   (On some systems you may need `python3` instead of `python`.)

4. You'll see a login menu. Choose a role — **Librarian**, **Student**, or
   **Teacher** — enter a User ID and name, and you'll be taken to a menu
   specific to that role.

## Roles & What They Can Do

| Role | Menu options |
|---|---|
| **Librarian** | Add a book, remove a book, search books, view all books, view available books, view all borrowed books, save catalog to `books.csv` |
| **Student** | Borrow a book (max **3** at a time), return a book, view all books, view available books, view my borrowed books |
| **Teacher** | Borrow a book (max **5** at a time), return a book, view all books, view available books, view my borrowed books |

Type `4` (or `6`/`8` inside a role menu) to log out or exit at any point.

## Data

The program starts with 5 sample books. If a `books.csv` file is saved by a
librarian (menu option "Save catalog to file"), it will be automatically
loaded the next time the program starts, so your catalog persists between
runs.

## Error Handling

The program will never crash on bad input. It gracefully handles:

- Invalid/out-of-range menu choices
- Non-numeric input where a number is expected
- Borrowing a book that has no copies available
- Borrowing a book ID that doesn't exist
- Returning a book you never borrowed
- A student/teacher trying to exceed their borrowing limit

## OOP Design

- **Abstraction** — `User` is an abstract base class (`abc.ABC`) with
  abstract methods `borrow()`, `return_book()`, and `show_menu()`.
- **Inheritance** — `Student`, `Teacher`, and `Librarian` all inherit from `User`.
- **Polymorphism** — `main()` calls `user.show_menu(library)` on any `User`
  object; the actual behavior depends on the real (runtime) subclass.
- **Encapsulation** — `Book` and `Library` keep their internal data
  (copy counts, catalog dictionary, borrow records) in private attributes,
  only accessible through methods/properties.

## Screenshots

*(Add screenshots of the program running here before submitting.)*

## Repository Link

*(Add your GitHub repository link here before submitting.)*
