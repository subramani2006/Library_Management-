from config.db_config import DB_CONFIG
import mysql.connector
from datetime import date


def get_connection():
    return mysql.connector.connect(**DB_CONFIG)


def issue_book():
    try:
        book_id = int(input("Enter book ID: "))
        student_id = int(input("Enter student ID: "))
    except ValueError:
        print("IDs must be numbers.")
        return

    conn = get_connection()
    cursor = conn.cursor()

    try:
        # Check whether the book exists and has copies available.
        cursor.execute(
            "SELECT quantity FROM books WHERE book_id = %s FOR UPDATE",
            (book_id,)
        )
        book = cursor.fetchone()

        if book is None:
            print("Book not found.")
            conn.rollback()
            return

        if book[0] <= 0:
            print("Book is currently unavailable.")
            conn.rollback()
            return

        # Check whether the student exists.
        cursor.execute(
            "SELECT student_id FROM students WHERE student_id = %s",
            (student_id,)
        )

        if cursor.fetchone() is None:
            print("Student not found.")
            conn.rollback()
            return

        # Prevent the same student from issuing the same book twice.
        cursor.execute("""
            SELECT transaction_id
            FROM transactions
            WHERE book_id = %s
              AND student_id = %s
              AND status = 'Issued'
        """, (book_id, student_id))

        if cursor.fetchone():
            print("This student already has this book.")
            conn.rollback()
            return

        cursor.execute("""
            INSERT INTO transactions
            (book_id, student_id, issue_date, status)
            VALUES (%s, %s, %s, 'Issued')
        """, (book_id, student_id, date.today()))

        cursor.execute("""
            UPDATE books
            SET quantity = quantity - 1
            WHERE book_id = %s
        """, (book_id,))

        conn.commit()
        print("Book issued successfully.")

    except mysql.connector.Error as error:
        conn.rollback()
        print(f"Transaction failed: {error}")

    finally:
        cursor.close()
        conn.close()


def return_book():
    try:
        transaction_id = int(input("Enter transaction ID: "))
    except ValueError:
        print("Transaction ID must be a number.")
        return

    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("""
            SELECT book_id, status
            FROM transactions
            WHERE transaction_id = %s
            FOR UPDATE
        """, (transaction_id,))

        transaction = cursor.fetchone()

        if transaction is None:
            print("Transaction not found.")
            conn.rollback()
            return

        book_id, status = transaction

        if status == "Returned":
            print("This book has already been returned.")
            conn.rollback()
            return

        cursor.execute("""
            UPDATE transactions
            SET return_date = %s, status = 'Returned'
            WHERE transaction_id = %s
        """, (date.today(), transaction_id))

        cursor.execute("""
            UPDATE books
            SET quantity = quantity + 1
            WHERE book_id = %s
        """, (book_id,))

        conn.commit()
        print("Book returned successfully.")

    except mysql.connector.Error as error:
        conn.rollback()
        print(f"Transaction failed: {error}")

    finally:
        cursor.close()
        conn.close()


def view_issued_books():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            t.transaction_id,
            b.title,
            s.name,
            t.issue_date,
            t.status
        FROM transactions t
        JOIN books b ON t.book_id = b.book_id
        JOIN students s ON t.student_id = s.student_id
        WHERE t.status = 'Issued'
        ORDER BY t.transaction_id
    """)

    records = cursor.fetchall()

    print("\n----- ISSUED BOOKS -----")

    if not records:
        print("No books are currently issued.")
    else:
        for record in records:
            print(
                f"Transaction ID: {record[0]} | "
                f"Book: {record[1]} | "
                f"Student: {record[2]} | "
                f"Issue Date: {record[3]} | "
                f"Status: {record[4]}"
            )

    cursor.close()
    conn.close()
