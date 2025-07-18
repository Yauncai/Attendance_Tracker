import sqlite3
import os

DB_FILE = 'yaf_attendance.db'

def yaf_database():
    # Check if DB file exists
    db_exists = os.path.isfile(DB_FILE)

    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()

    # Create table only if it doesn't exist (safe to run multiple times)
    c.execute('''
        CREATE TABLE IF NOT EXISTS attendance (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            surname TEXT NOT NULL,
            phone TEXT NOT NULL,
            status TEXT NOT NULL,
            timestamp TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

    if not db_exists:
        print("Database created and initialized.")
    else:
        print("Database already exists. No changes made.")

if __name__ == '__main__':
    yaf_database()
