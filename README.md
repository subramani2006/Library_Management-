# Library Management System

A simple **DBMS mini project** built using **Python and MySQL**.  
It allows a small library to manage books, students, and book issue/return transactions.

## Features

- Add new books
- View all books
- Search books
- Add students
- View all students
- Issue a book
- Return a book
- View active issued books
- MySQL database with relational tables
- Basic input validation
- Simple command-line interface

## Technologies Used

- Python 3
- MySQL 8
- mysql-connector-python
- SQL

## Project Structure

```text
Library-Management-System/
│
├── README.md
├── requirements.txt
├── .gitignore
│
├── database/
│   └── schema.sql
│
├── config/
│   └── db_config.py
│
├── src/
│   ├── main.py
│   ├── book.py
│   ├── student.py
│   └── transaction.py
│
└── screenshots/
    └── .gitkeep
```

## Database Design

The project uses three main tables:

### books
Stores book information.

- book_id
- title
- author
- category
- quantity

### students
Stores student information.

- student_id
- name
- email
- phone

### transactions
Stores book issue and return information.

- transaction_id
- book_id
- student_id
- issue_date
- return_date
- status

Relationship:

```text
Books 1 -------- N Transactions N -------- 1 Students
```

## Requirements

Install:

- Python 3.9+
- MySQL Server 8.0+

Install the Python dependency:

```bash
pip install -r requirements.txt
```

## MySQL Setup

1. Open MySQL.
2. Run the SQL file:

```sql
SOURCE database/schema.sql;
```

Or copy and execute the contents of `database/schema.sql` in MySQL Workbench.

3. Open:

```text
config/db_config.py
```

4. Change the MySQL username and password:

```python
DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "YOUR_MYSQL_PASSWORD",
    "database": "library_management"
}
```

## Run the Project

From the project folder:

```bash
python src/main.py
```

## Main Menu

```text
===== LIBRARY MANAGEMENT SYSTEM =====
1. Add Book
2. View Books
3. Search Book
4. Add Student
5. View Students
6. Issue Book
7. Return Book
8. View Issued Books
9. Exit
```

## Sample Workflow

```text
1. Add a book
2. Add a student
3. Issue the book to the student
4. View issued books
5. Return the book
```

## Learning Outcomes

This project demonstrates:

- Database creation
- Tables and relationships
- Primary keys
- Foreign keys
- CRUD operations
- SQL JOIN
- Transactions
- Python-MySQL connectivity
- Modular Python programming

## Future Improvements

- Login system
- GUI using Tkinter
- Fine calculation
- Admin dashboard
- Due-date notifications
- Web version using Flask
- Export reports to CSV/PDF

## Author

**Subramani U**  
B.Tech Artificial Intelligence & Data Science

This project was created as a beginner-friendly DBMS mini project for learning and portfolio development.
