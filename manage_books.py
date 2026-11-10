def display_books(books):
    if books:
        for index in books:
            print(f"\n================================")
            for key, value in index.items():
                print(f"{key}: {value}")
            print(f"================================")

def search_book(books, name):
    for book in books:
        if name in book["name"]:
            return book

def add_book(books, name, author, year):
    new_book = {
        "id": get_next_book_id(books),
        "name": name,
        "author": author,
        "year": year,
        "available": True
        }
    for book in books:
        if book["name"] == name and book["author"] == author:
            print("the book is already in the library")
            return
    books.append(new_book)

def borrow_book(books, book_id):
    for index, book in enumerate(books):
        if book_id == book["id"]:
            if books[index]["available"]:
                books[index]["available"] = False
                display_books([book])
            else:
                print("the book is not available")
            return
        print("the book not found")

def return_book(books, book_id):
    for index, book in enumerate(books):
        if book_id == book["id"]:
            if not books[index]["available"]:
                books[index]["available"] = True
                display_books([book])
            else:
                print("the book is already return")
        return
    print("the book not found")
    

def get_available_books(books):
    return filter(lambda b: b["available"] == True, books)

def get_books_by_author(books, author):
    books_by_author = []
    for book in books:
        if book["author"] == author:
            books_by_author.append(book)
    return books_by_author

def get_next_book_id(books):
    return len(books) + 1