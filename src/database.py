import sqlite3

DB_NAME = "library.db"

def create_connection():
    conn = sqlite3.connect(DB_NAME)
    return conn

def create_table():
    conn = create_connection()
    cursor = conn.cursor()
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT NOT NULL
        )
    """)
    
    conn.commit()
    conn.close()

def add_book(title, author):
    conn = create_connection()
    cursor = conn.cursor()
    
    cursor.execute("INSERT INTO books (title, author) VALUES (?, ?)", (title, author))
    
    conn.commit()
    conn.close()

def get_books():
    conn = create_connection()
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()
    
    conn.close()
    return books