from book import add_book, view_books, search_book
from student import add_student, view_students
from transaction import issue_book, return_book, view_issued_books


def show_menu():
    print("\n" + "=" * 42)
    print("       LIBRARY MANAGEMENT SYSTEM")
    print("=" * 42)
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Add Student")
    print("5. View Students")
    print("6. Issue Book")
    print("7. Return Book")
    print("8. View Issued Books")
    print("9. Exit")
    print("=" * 42)


def main():
    while True:
        show_menu()
        choice = input("Enter your choice: ").strip()

        try:
            if choice == "1":
                add_book()
            elif choice == "2":
                view_books()
            elif choice == "3":
                search_book()
            elif choice == "4":
                add_student()
            elif choice == "5":
                view_students()
            elif choice == "6":
                issue_book()
            elif choice == "7":
                return_book()
            elif choice == "8":
                view_issued_books()
            elif choice == "9":
                print("Thank you for using the Library Management System.")
                break
            else:
                print("Invalid choice. Please select 1-9.")

        except Exception as error:
            print(f"Unexpected error: {error}")


if __name__ == "__main__":
    main()
