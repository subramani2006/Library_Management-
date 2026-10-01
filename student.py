from config.db_config import DB_CONFIG
import mysql.connector


def get_connection():
    return mysql.connector.connect(**DB_CONFIG)


def add_student():
    name = input("Enter student name: ").strip()
    email = input("Enter email: ").strip()
    phone = input("Enter phone number: ").strip()

    if not name or not email:
        print("Name and email are required.")
        return

    conn = get_connection()
    cursor = conn.cursor()

    try:
        query = """
            INSERT INTO students (name, email, phone)
            VALUES (%s, %s, %s)
        """
        cursor.execute(query, (name, email, phone))
        conn.commit()
        print("Student added successfully.")

    except mysql.connector.Error as error:
        conn.rollback()
        print(f"Could not add student: {error}")

    finally:
        cursor.close()
        conn.close()


def view_students():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT student_id, name, email, phone
        FROM students
        ORDER BY student_id
    """)

    students = cursor.fetchall()

    print("\n----- STUDENTS -----")
    if not students:
        print("No students found.")
    else:
        for student in students:
            print(
                f"ID: {student[0]} | Name: {student[1]} | "
                f"Email: {student[2]} | Phone: {student[3]}"
            )

    cursor.close()
    conn.close()
