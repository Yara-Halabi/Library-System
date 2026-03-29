from database import add_book, get_books

def add_new_book(title, author):
    add_book(title, author)

def list_books():
    books = get_books()
    return books

def search_book_by_title(search_title):
    books = get_books()
    result = []

    for book in books:
        if search_title.lower() in book[1].lower():
            result.append(book)

    return result
def test_service():
    print("Service functions are working")
    