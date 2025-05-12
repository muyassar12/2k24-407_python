import sqlite3
def get_connection():
    return sqlite3.connect("certifications.db")  # Fayl nomi .db
def create_certification_table():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS certifications (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            header TEXT NOT NULL,
            date TEXT,
            image TEXT,
            description TEXT
        )
    """)
    conn.commit()
    cur.close()
    conn.close()
from db import get_connection
def save_certification_to_db(data):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO certifications (header, date, image, description)
        VALUES (?, ?, ?, ?)
    """, (data["header"], data["date"], data["image"], data["description"]))
    conn.commit()
    cur.close()
    conn.close()
    print("Ma'lumotlar SQLite bazaga saqlandi.")
