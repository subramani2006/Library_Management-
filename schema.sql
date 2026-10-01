-- Library Management System
-- Database schema and sample data

CREATE DATABASE IF NOT EXISTS library_management;
USE library_management;

DROP TABLE IF EXISTS transactions;
DROP TABLE IF EXISTS students;
DROP TABLE IF EXISTS books;

CREATE TABLE books (
    book_id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(150) NOT NULL,
    author VARCHAR(100) NOT NULL,
    category VARCHAR(80),
    quantity INT NOT NULL DEFAULT 1,
    CHECK (quantity >= 0)
);

CREATE TABLE students (
    student_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(150) UNIQUE NOT NULL,
    phone VARCHAR(15)
);

CREATE TABLE transactions (
    transaction_id INT AUTO_INCREMENT PRIMARY KEY,
    book_id INT NOT NULL,
    student_id INT NOT NULL,
    issue_date DATE NOT NULL,
    return_date DATE NULL,
    status ENUM('Issued', 'Returned') NOT NULL DEFAULT 'Issued',

    CONSTRAINT fk_transaction_book
        FOREIGN KEY (book_id) REFERENCES books(book_id),

    CONSTRAINT fk_transaction_student
        FOREIGN KEY (student_id) REFERENCES students(student_id)
);

-- Sample books
INSERT INTO books (title, author, category, quantity) VALUES
('Python Programming', 'John Smith', 'Programming', 3),
('Database System Concepts', 'Abraham Silberschatz', 'DBMS', 2),
('Data Structures and Algorithms', 'Thomas Cormen', 'Algorithms', 2);

-- Sample students
INSERT INTO students (name, email, phone) VALUES
('Arun Kumar', 'arun@example.com', '9876543210'),
('Priya S', 'priya@example.com', '9876501234');

-- Sample transaction
INSERT INTO transactions
(book_id, student_id, issue_date, return_date, status)
VALUES
(1, 1, CURDATE(), NULL, 'Issued');
