"""
Assignment 4: Relational SQLite User Management System
Scenario
An internal employee directory stores user contact details in a SQLite database. The application must search for users, display existing details, or register new users.

Problem Description
Create a class UserDatabaseManager that connects to a SQLite database file:

__init__(self, db_path): Connects to the database and creates a table users if it doesn't already exist:
Columns: id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT UNIQUE NOT NULL, address TEXT, mobile TEXT, email TEXT.
find_user(self, username):
Queries the database for the given username using a parameterized SQL query.
If found, returns a dictionary: {"id": row[0], "username": row[1], "address": row[2], "mobile": row[3], "email": row[4]}.
If not found, returns None.
add_or_update_user(self, username, address, mobile, email):
Checks if username exists.
If user exists, updates their address, mobile, and email values and returns "UPDATED".
If user does not exist, inserts a new record and returns "INSERTED".
list_all_users(self): Returns a list of dictionaries for all registered users ordered alphabetically by username.
Example Walkthrough
db = UserDatabaseManager("company.db")

# Insert new user
status1 = db.add_or_update_user("arham_k", "Pune, MH", "9876543210", "arham@cdac.in")
print(status1)  # Output: INSERTED

# Search user
user_info = db.find_user("arham_k")
print(user_info["email"])  # Output: arham@cdac.in

# Update existing user
status2 = db.add_or_update_user("arham_k", "Bengaluru, KA", "9876543210", "arham@cdac.in")
print(status2)  # Output: UPDATED
"""
import sqlite3
class UserDatabaseManager:
    def __init__(self, db_path):
        self.db_path=db_path

        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS users(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                address TEXT,
                mobile TEXT,
                email TEXT)
            """)
            conn.commit()

    def find_user(self, username):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, username, address, mobile, email FROM users WHERE username = ?", (username,))
            row = cursor.fetchone()

            if row:
                return {
                    "id": row[0],
                    "username": row[1],
                    "address": row[2],
                    "mobile": row[3],
                    "email": row[4]
                }
            return None

    def add_or_update_user(self, username, address, mobile, email):
        existing_user = self.find_user(username)
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            if existing_user:
                    cursor.execute("""
                        UPDATE users 
                        SET address = ?, mobile = ?, email = ? 
                        WHERE username = ?
                    """, (address, mobile, email, username))
                    conn.commit()
                    return "UPDATED"
            else:
                cursor.execute("""
                    INSERT INTO users (username, address, mobile, email) 
                    VALUES (?, ?, ?, ?)
                    """, (username, address, mobile, email))
                conn.commit()
                return "INSERTED"

    def list_all_users(self):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, username, address, mobile, email FROM users ORDER BY username ASC")
            rows = cursor.fetchall()
            
            user_list = []
            for row in rows:
                user_list.append({
                    "id": row[0],
                    "username": row[1],
                    "address": row[2],
                    "mobile": row[3],
                    "email": row[4]
                })
            return user_list

db = UserDatabaseManager("company.db")

status1 = db.add_or_update_user("arham_k", "Pune, MH", "9876543210", "arham@cdac.in")
print(status1)  

user_info = db.find_user("arham_k")
print(user_info["email"]) 

status2 = db.add_or_update_user("arham_k", "Bengaluru, KA", "9876543210", "arham@cdac.in")
print(status2)  