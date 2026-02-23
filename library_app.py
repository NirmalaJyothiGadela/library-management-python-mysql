import mysql.connector
from datetime import datetime

# -------- LOGIN SYSTEM --------
USERNAME = "admin"
PASSWORD = "1234"

print("---- LIBRARY LOGIN ----")
u = input("Username: ")
p = input("Password: ")

if u != USERNAME or p != PASSWORD:
    print("Invalid login. Exiting...")
    exit()

print("\nLogin successful!\n")

# -------- DB CONNECTION --------
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Mysql@8778",
    database="library_db"
)
cursor = conn.cursor()


# -------- HELPER FUNCTION --------
def show_books():
    cursor.execute("SELECT * FROM books")
    rows = cursor.fetchall()

    print("\nID | Title | Author | Price | Qty")
    print("-"*40)
    for r in rows:
        print(f"{r[0]} | {r[1]} | {r[2]} | {r[3]} | {r[4]}")
    print()


# -------- MAIN LOOP --------
while True:

    print("\n--- LIBRARY MENU ---")
    print("1. Add Book")
    print("2. View Books")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. View Issued Books")
    print("6. Exit")

    choice = input("Enter choice: ")

    # -------- ADD BOOK --------
    if choice == "1":
        title = input("Enter title: ").strip()
        author = input("Enter author: ").strip()

        if not title or not author:
            print("Title/Author cannot be empty")
            continue

        price = int(input("Enter price: "))
        quantity = int(input("Enter quantity: "))

        if price < 0 or quantity < 0:
            print("Invalid price/quantity")
            continue

        cursor.execute(
            "INSERT INTO books(title,author,price,quantity) VALUES(%s,%s,%s,%s)",
            (title, author, price, quantity)
        )
        conn.commit()

        print("Book added successfully!")

    # -------- VIEW BOOKS --------
    elif choice == "2":
        show_books()

    # -------- ISSUE BOOK --------
    elif choice == "3":
        show_books()
        book_id = int(input("Enter Book ID: "))
        student = input("Enter student name: ").strip()

        date_input = input("Enter issue date (DD-MM-YYYY): ")
        date = datetime.strptime(date_input, "%d-%m-%Y").strftime("%Y-%m-%d")

        cursor.execute("SELECT quantity FROM books WHERE id=%s", (book_id,))
        result = cursor.fetchone()

        if result and result[0] > 0:

            cursor.execute(
                "INSERT INTO issued_books(book_id,student_name,issue_date) VALUES(%s,%s,%s)",
                (book_id, student, date)
            )

            cursor.execute(
                "UPDATE books SET quantity=quantity-1 WHERE id=%s",
                (book_id,)
            )

            conn.commit()
            print("Book issued!")

        else:
            print("Book not available.")

    # -------- RETURN BOOK --------
    elif choice == "4":

        cursor.execute("SELECT * FROM issued_books")
        rows = cursor.fetchall()

        print("\nIssueID | BookID | Student | Date")
        print("-"*40)
        for r in rows:
            print(f"{r[0]} | {r[1]} | {r[2]} | {r[3]}")

        issue_id = int(input("\nEnter Issue ID to return: "))

        cursor.execute(
            "SELECT book_id FROM issued_books WHERE issue_id=%s",
            (issue_id,)
        )
        result = cursor.fetchone()

        if result:
            book_id = result[0]

            cursor.execute(
                "DELETE FROM issued_books WHERE issue_id=%s",
                (issue_id,)
            )

            cursor.execute(
                "UPDATE books SET quantity=quantity+1 WHERE id=%s",
                (book_id,)
            )

            conn.commit()
            print("Book returned!")

        else:
            print("Invalid Issue ID")

    # -------- VIEW ISSUED BOOKS --------
    elif choice == "5":

        cursor.execute("SELECT * FROM issued_books")
        rows = cursor.fetchall()

        print("\nIssueID | BookID | Student | Date")
        print("-"*40)

        for r in rows:
            print(f"{r[0]} | {r[1]} | {r[2]} | {r[3]}")

        print()

    # -------- EXIT --------
    elif choice == "6":
        print("Goodbye!")
        break

    else:
        print("Invalid choice")