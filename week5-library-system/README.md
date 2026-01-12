# 📚 Week 5 – Library Management System (Python OOP)

A command-line based **Library Management System** built using **Python Object-Oriented Programming (OOP)** concepts.  
This project demonstrates how to design a real-world system using classes, objects, and file handling.

---

## 📌 Project Overview

The Library Management System allows librarians to manage books and members efficiently.  
Users can add books, register members, borrow and return books, search records, and store data persistently using JSON files.

This project focuses on applying **OOP fundamentals** in a practical way.

---

## 🎯 Objectives

- Understand Object-Oriented Programming concepts
- Design classes and objects for real-world problems
- Practice constructors, methods, and object interaction
- Implement file handling for data persistence
- Build a structured, menu-driven Python application

---

## 🛠 Technologies Used

- Python 3
- Object-Oriented Programming (OOP)
- JSON for data storage
- Command Line Interface (CLI)

---

## 📂 Project Structure
week5-library-system/
│── library_system/
│ ├── init.py
│ ├── book.py
│ ├── member.py
│ ├── library.py
│ └── main.py
│
│── data/
│ ├── books.json
│ ├── members.json
│ └── backup/
│
│── tests/
│ ├── test_book.py
│ ├── test_member.py
│ └── test_library.py
│
│── README.md
│── requirements.txt
│── .gitignore

---

## 🧩 Class Description

### 📘 Book Class
- Attributes: title, author, ISBN, year, availability
- Methods: borrow book, return book, convert to/from dictionary

### 👤 Member Class
- Attributes: name, member ID, borrowed books
- Methods: borrow book, return book

### 🏛 Library Class
- Manages all books and members
- Handles borrowing, returning, searching, saving, and loading data

---

## ⚙️ How to Run the Project

1. Open terminal in the project root folder:
2. Run the application:
```bash
python -m library_system.main

📋 Application Menu
1. Add New Book
2. Register Member
3. Borrow Book
4. Return Book
5. View All Books
6. Save & Exit

✨ Features Implemented

1. Add new books to the library
2. Register library members
3. Borrow and return books
4. Search books by title, author, or ISBN
5. Store data using JSON files
6. Menu-driven user interface
7. Modular and reusable OOP design

🧪 Testing

. Basic unit tests are included in the tests/ folder to validate:
. Book creation
. Member creation
. Library initialization
🧠 Learning Outcomes

Clear understanding of OOP fundamentals

Hands-on experience with classes and objects

Designing a real-world system using Python

Improved code organization and readability

Practical use of file handling

🚀 Conclusion

This project strengthened my understanding of Object-Oriented Programming in Python and helped me move from simple scripts to building structured, real-world applications.
👨‍💻 Author

Developed as part of Week 5 – Python OOP Learning Program
Guided by Developers Arena
