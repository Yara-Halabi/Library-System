import sqlite3

# إنشاء قاعدة البيانات والجدول
def create_database():
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            year INTEGER,
            isbn TEXT
        )
    """)

    conn.commit()
    conn.close()


# إضافة كتاب
def add_book(title, author, year, isbn):
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()

    cursor.execute("INSERT INTO books (title, author, year, isbn) VALUES (?, ?, ?, ?)",
                   (title, author, year, isbn))

    conn.commit()
    conn.close()


# عرض جميع الكتب
def get_all_books():
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()

    conn.close()
    return books


# البحث عن كتاب بالعنوان
def search_book(title):
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM books WHERE title LIKE ?", ('%' + title + '%',))
    results = cursor.fetchall()

    conn.close()
    return results


# تشغيل إنشاء قاعدة البيانات أول مرة
create_database()