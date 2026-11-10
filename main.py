from menu import show_menu
from db.books import BOOKS
from manage_books import display_books, search_book, add_book, borrow_book, get_available_books, return_book, get_books_by_author
from user_input import num_input, text_input

def main():
    while True:
        show_menu()
        menu_select = num_input("Choose an option between 1 - 8: ")
        if menu_select == 1:
            display_books(BOOKS)
        if menu_select == 2:
            search_input = text_input("please enter text to search a book")
            search_book_by_name = search_book(BOOKS, search_input)
            display_books([search_book_by_name])
        if menu_select == 3:
            book_name = text_input("to add new book please enter book name")
            book_author = text_input("please enter book author")
            book_year = text_input("please enter book year")
            add_book(BOOKS, book_name, book_author, book_year)
            display_books(BOOKS)
        if menu_select == 4:
            book_id = num_input("please enter book id: ")
            borrow_book(BOOKS, book_id)
        if menu_select == 5:
            book_id = num_input("please enter book id: ")
            return_book(BOOKS, book_id)
        if menu_select == 6:
            display_books(get_available_books(BOOKS))
        if menu_select == 7:
            book_author = text_input("please enter book author")
            display_books(get_books_by_author(BOOKS, book_author))
        if menu_select == 8:
            break
        else:
            print("please enter num between 1 - 8")

if __name__ == "__main__":
    main()