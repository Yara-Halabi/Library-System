import tkinter as tk
from tkinter import ttk, messagebox
from databeas import add_book, get_all_books, search_book

# نافذة البرنامج
window = tk.Tk()
window.title("نظام إدارة المكتبة")
window.geometry("750x550")
window.configure(bg="#f5f5f5")


# قسم إدخال البيانات (Form)

form_frame = tk.LabelFrame(window, text="إدخال بيانات الكتاب", bg="#f5f5f5", padx=10, pady=10)
form_frame.pack(fill="x", padx=20, pady=10)

labels = ["عنوان الكتاب", "اسم المؤلف", "سنة النشر", "ISBN"]
entries = {}

for label in labels:
    row = tk.Frame(form_frame, bg="#f5f5f5")
    row.pack(fill="x", pady=5)

    lbl = tk.Label(row, text=label, width=15, anchor="w", bg="#f5f5f5", font=("Arial", 12))
    lbl.pack(side="left")

    ent = tk.Entry(row, width=50)
    ent.pack(side="left", padx=10)
    entries[label] = ent

# -----------------------------
# قسم الأزرار
# -----------------------------
btn_frame = tk.Frame(window, bg="#f5f5f5")
btn_frame.pack(pady=10)

# دالة إضافة كتاب
def on_add_book():
    title = entries["عنوان الكتاب"].get()
    author = entries["اسم المؤلف"].get()
    year = entries["سنة النشر"].get()
    isbn = entries["ISBN"].get()

    if not title or not author:
        messagebox.showerror("خطأ", "العنوان والمؤلف مطلوبان")
        return

    add_book(title, author, year, isbn)
    messagebox.showinfo("تم", "تمت إضافة الكتاب بنجاح")

# دالة عرض الكتب
def on_show_books():
    for row in table.get_children():
        table.delete(row)

    books = get_all_books()
    for book in books:
        table.insert("", "end", values=book)

# دالة البحث عن كتاب
def on_search_book():
    title = entries["عنوان الكتاب"].get()

    for row in table.get_children():
        table.delete(row)

    results = search_book(title)
    for book in results:
        table.insert("", "end", values=book)

# الأزرار
add_btn = tk.Button(btn_frame, text="إضافة كتاب", width=15, command=on_add_book, bg="#4CAF50", fg="white")
add_btn.grid(row=0, column=0, padx=10)

show_btn = tk.Button(btn_frame, text="عرض الكتب", width=15, command=on_show_books, bg="#2196F3", fg="white")
show_btn.grid(row=0, column=1, padx=10)

search_btn = tk.Button(btn_frame, text="بحث عن كتاب", width=15, command=on_search_book, bg="#FF9800", fg="white")
search_btn.grid(row=0, column=2, padx=10)


table_frame = tk.Frame(window)
table_frame.pack(fill="both", expand=True, padx=20, pady=10)

table = ttk.Treeview(table_frame, columns=("id", "title", "author", "year", "isbn"), show="headings")
table.pack(fill="both", expand=True)

table.heading("id", text="ID")
table.heading("title", text="العنوان")
table.heading("author", text="المؤلف")
table.heading("year", text="السنة")
table.heading("isbn", text="ISBN")

table.column("id", width=50)
table.column("title", width=200)
table.column("author", width=150)
table.column("year", width=80)
table.column("isbn", width=120)

# تشغيل الواجهة
window.mainloop()