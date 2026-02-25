import tkinter as tk
from tkinter import ttk, messagebox
from databeas import add_book, get_all_books, search_book

# نافذة البرنامج
window = tk.Tk()
window.title("نظام إدارة المكتبة")
window.geometry("850x600")
window.configure(bg="#ECEFF1")

# -----------------------------
# تنسيق الستايل العصري
# -----------------------------
style = ttk.Style()
style.theme_use("clam")

# ألوان الجدول
style.configure("Treeview",
                background="#FFFFFF",
                foreground="#000000",
                rowheight=30,
                fieldbackground="#FFFFFF",
                bordercolor="#90A4AE",
                borderwidth=1)

style.map("Treeview",
          background=[("selected", "#80DEEA")])

# رأس الجدول
style.configure("Treeview.Heading",
                background="#5C6BC0",
                foreground="white",
                font=("Arial", 12, "bold"))

# -----------------------------
# عنوان رئيسي
# -----------------------------
title_label = tk.Label(window, text="نظام إدارة المكتبة",
                       font=("Arial", 22, "bold"),
                       bg="#ECEFF1", fg="#3949AB")
title_label.pack(pady=15)

# -----------------------------
# قسم إدخال البيانات
# -----------------------------
form_frame = tk.LabelFrame(window, text="إدخال بيانات الكتاب",
                           bg="#ECEFF1", padx=15, pady=15,
                           font=("Arial", 12, "bold"), fg="#3949AB")
form_frame.pack(fill="x", padx=20, pady=10)

labels = ["عنوان الكتاب", "اسم المؤلف", "سنة النشر", "ISBN"]
entries = {}

for label in labels:
    row = tk.Frame(form_frame, bg="#ECEFF1")
    row.pack(fill="x", pady=8)

    lbl = tk.Label(row, text=label, width=15, anchor="w",
                   bg="#ECEFF1", fg="#37474F", font=("Arial", 12))
    lbl.pack(side="left")

    ent = tk.Entry(row, width=50, font=("Arial", 12),
                   relief="solid", bd=1)
    ent.pack(side="left", padx=10)
    entries[label] = ent

# -----------------------------
# دوال الأزرار
# -----------------------------
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

def on_show_books():
    for row in table.get_children():
        table.delete(row)

    books = get_all_books()
    for book in books:
        table.insert("", "end", values=book)

def on_search_book():
    title = entries["عنوان الكتاب"].get()

    for row in table.get_children():
        table.delete(row)

    results = search_book(title)
    for book in results:
        table.insert("", "end", values=book)

# -----------------------------
# أزرار عصرية
# -----------------------------
btn_frame = tk.Frame(window, bg="#ECEFF1")
btn_frame.pack(pady=10)

def modern_button(text, color, command):
    return tk.Button(btn_frame, text=text, width=15, height=1,
                     command=command, bg=color, fg="white",
                     font=("Arial", 12, "bold"),
                     relief="flat", bd=0, highlightthickness=0)

add_btn = modern_button("إضافة كتاب", "#26A69A", on_add_book)
add_btn.grid(row=0, column=0, padx=10)

show_btn = modern_button("عرض الكتب", "#5C6BC0", on_show_books)
show_btn.grid(row=0, column=1, padx=10)

search_btn = modern_button("بحث عن كتاب", "#FF7043", on_search_book)
search_btn.grid(row=0, column=2, padx=10)

# -----------------------------
# جدول عرض الكتب
# -----------------------------
table_frame = tk.Frame(window)
table_frame.pack(fill="both", expand=True, padx=20, pady=10)

table = ttk.Treeview(table_frame,
                     columns=("id", "title", "author", "year", "isbn"),
                     show="headings")
table.pack(fill="both", expand=True)

table.heading("id", text="ID")
table.heading("title", text="العنوان")
table.heading("author", text="المؤلف")
table.heading("year", text="السنة")
table.heading("isbn", text="ISBN")

table.column("id", width=50, anchor="center")
table.column("title", width=250)
table.column("author", width=150)
table.column("year", width=80, anchor="center")
table.column("isbn", width=150)

# -----------------------------
# تشغيل الواجهة
# -----------------------------
window.mainloop()