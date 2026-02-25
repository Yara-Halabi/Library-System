from services import list_books, add_book

def show_books():
    books = list_books()
    print("Library Books:")
    for book in books:
        print(f"{book[0]} - {book[1]} by {book[2]}")

def demo():
    add_book("1984", "George Orwell")
    add_book("The Little Prince", "Antoine de Saint-Exupéry")
    show_books()

if __name__ == "__main__":
    demo()