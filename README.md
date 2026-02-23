# 📚 Library Management System (Python + MySQL)

A simple console-based Library Management System built using **Python** and **MySQL**.
This project demonstrates database connectivity, CRUD operations, and book issue/return workflow without any GUI or frontend.

---

## 🚀 Features

* 🔐 Simple login authentication
* ➕ Add new books to database
* 📖 View all available books
* 📤 Issue book to student (reduces quantity automatically)
* 📥 Return book (restores quantity)
* 📋 View all issued books
* 🗂️ MySQL relational database with foreign key support
* 🖥️ Menu-driven console interface

---

## 🛠️ Tech Stack

* **Python 3**
* **MySQL**
* **mysql-connector-python**
* **Datetime module**

---

## 🗄️ Database Structure

### **Database:** `library_db`

### **Table: books**

| Column   | Type                              |
| -------- | --------------------------------- |
| id       | INT (Primary Key, Auto Increment) |
| title    | VARCHAR                           |
| author   | VARCHAR                           |
| price    | INT                               |
| quantity | INT                               |

### **Table: issued_books**

| Column       | Type                              |
| ------------ | --------------------------------- |
| issue_id     | INT (Primary Key, Auto Increment) |
| book_id      | INT (Foreign Key → books.id)      |
| student_name | VARCHAR                           |
| issue_date   | DATE                              |

---

## ⚙️ Setup Instructions

### 1️⃣ Install dependencies

```
pip install mysql-connector-python
```

### 2️⃣ Create MySQL database

Run in MySQL:

```sql
CREATE DATABASE library_db;
USE library_db;

CREATE TABLE books(
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(100),
    author VARCHAR(100),
    price INT,
    quantity INT
);

CREATE TABLE issued_books(
    issue_id INT AUTO_INCREMENT PRIMARY KEY,
    book_id INT,
    student_name VARCHAR(100),
    issue_date DATE,
    FOREIGN KEY(book_id) REFERENCES books(id)
);
```

### 3️⃣ Update database credentials

Open `library_app.py` and change:

```
password="YOUR_PASSWORD"
```

to your MySQL password.

---

### 4️⃣ Run the project

```
python library_app.py
```

Login credentials:

```
username: admin
password: 1234
```

---

## 📸 Example Menu

```
1. Add Book
2. View Books
3. Issue Book
4. Return Book
5. View Issued Books
6. Exit
```

---

## 🎯 Learning Outcomes

* Connecting Python to MySQL database
* Executing SQL queries from Python
* Handling transactions with commit()
* Using foreign keys in relational tables
* Building a structured console application

---

## 👩‍💻 Author

**Nirmala jyothi Gadela**
Aspiring Data Analyst / Python Developer

---

⭐ If you like this project, feel free to star the repository!
