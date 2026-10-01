from config.db_config import DB_CONFIG
import mysql.connector


def get_connection():
    return mysql.connector.connect(**DB_CONFIG)


def add_book():
    title = input("Enter book title: ").strip()
    author = input("Enter author: ").strip()
    category = input("Enter category: ").strip()

    try:
        quantity = int(input("Enter quantity: "))
        if quantity < 1:
            print("Quantity must be at least 1.")
            return
    except ValueError:
        print("Please enter a valid quantity.")
        return

    conn = get_connection()
    cursor = conn.cursor()

    query = """
        INSERT INTO books (title, author, category, quantity)
        VALUES (%s, %s, %s, %s)
    """

    cursor.execute(query, (title, author, category, quantity))
    conn.commit()

    print("Book added successfully.")

    cursor.close()
    conn.close()


def view_books():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT book_id, title, author, category, quantity
        FROM books
        ORDER BY book_id
    """)

    books = cursor.fetchall()

    print("\n----- BOOKS -----")
    if not books:
        print("No books found.")
    else:
        for book in books:
            print(
                f"ID: {book[0]} | Title: {book[1]} | "
                f"Author: {book[2]} | Category: {book[3]} | "
                f"Available: {book[4]}"
            )

    cursor.close()
    conn.close()


def search_book():
    keyword = input("Enter title or author to search: ").strip()

    conn = get_connection()
    cursor = conn.cursor()

    query = """
        SELECT book_id, title, author, category, quantity
        FROM books
        WHERE title LIKE %s OR author LIKE %s
    """

    value = f"%{keyword}%"
    cursor.execute(query, (value, value))

    books = cursor.fetchall()

    print("\n----- SEARCH RESULTS -----")
    if not books:
        print("No matching books found.")
    else:
        for book in books:
            print(
                f"ID: {book[0]} | {book[1]} | "
                f"{book[2]} | {book[3]} | Available: {book[4]}"
            )

    cursor.close()
    conn.close()
