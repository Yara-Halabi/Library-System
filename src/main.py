import sqlite3

# إنشاء قاعدة بيانات إذا لم تكن موجودة
conn = sqlite3.connect("library.db")
cursor = conn.cursor()

# إنشاء جدول الكتب
cursor.execute("""
CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    author TEXT NOT NULL
)
""")

conn.commit()
conn.close()

print("Database and table created successfully!")
