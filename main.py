from books_menu import Books_Menu
from starter_books import Starter_Books


def main():
    Books_Menu.menu()
    option = str(input())
    Books_Menu.option_menu(option)


if __name__ == "__main__":
    Starter_Books.fill_book_list()
    while True:
        main()