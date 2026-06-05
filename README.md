# Library Management System

A simple, console-based Library Management System implemented in Python. This project demonstrates core Object-Oriented Programming (OOP) principles, including inheritance, abstraction, interfaces, encapsulation, and polymorphism.

---

## Features

- **Book Inventory Management**: Add, remove, and list various types of books.
- **Book Types**:
  - **Physical Books** (with shelf location attributes)
  - **E-Books** (with file size attributes)
  - **Audio Books** (with duration attributes)
- **Membership Hierarchy**: Support for different member types (e.g., standard `Member`, `Faculty` members).
- **Search Capabilities**: Search books by title (substring search) or author (exact match).
- **Borrowing System**: Tracks book borrowing status (`AVAILABLE` vs. `BORROWED`) and associates borrowed books with specific members.
- **Interactive CLI**: Menu-driven interface for easy operation.

---

## Project Structure

```text
Library-Management/
├── src/
│   ├── books/              # Book models (Base Book, Ebook, AudioBook, PhysicalBook)
│   ├── enums/              # Project-wide enums (BookStatus)
│   ├── interfaces/         # OOP Interfaces (Borrowable, Searchable)
│   ├── members/            # Member models (Member, Faculty)
│   ├── services/           # Business logic services (Library)
│   └── main.py             # CLI Entry Point
└── README.md               # Project documentation
```

---

## How to Run

1. Make sure you have **Python 3.x** installed.
2. Navigate to the root directory of the project:
   ```bash
   cd Library-Management
   ```
3. Run the application:
   ```bash
   python src/main.py
   ```

---

## Example Usage

Once launched, you will see an interactive menu:

```text
========= LIBRARY MENU =========
1. View All Books
2. Borrow Book
3. Return Book
4. Search Book By Title
5. Search Book By Author
6. View Borrowed Books
7. Exit
Enter choice:
```
