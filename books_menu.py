from book import Book


class Books_Menu:

    prompt_dict = {
        "1": "Enter a book name you want to store copy of: ",
        "2": "Enter a book name you want to borrow: ",
        "3": "Enter a book name you want to return: ",
        "4": "Enter a book name or author name you want to find: ",
        "0a": "Book name: ",
        "0b": "Book author: ",
        "0c": "Book release year: "
    }

    def menu():
        print("""\n0. Create a book
1. Put a copy of an existing book in the library
2. Borrow a book
3. Return a book
4. Search for a book
5. List of available books
6. List of taken books
\n""")

    def option_menu(option):
        if option == '0':
            book_name = str(input(Books_Menu.prompt_dict[option + 'a']))
            book_author = str(input(Books_Menu.prompt_dict[option + 'b']))
            book_release_year = int(input(Books_Menu.prompt_dict[option + 'c']))
            print(Book.create_a_book(book_name, book_author, book_release_year))

        elif option == '1':
            book_name = str(input(Books_Menu.prompt_dict[option]))
            book_author = str(input(Books_Menu.prompt_dict["0b"]))
            print(Book.create_a_copy(book_name, book_author))

        elif option == '2':
            book_name = str(input(Books_Menu.prompt_dict[option]))
            book_author = str(input(Books_Menu.prompt_dict["0b"]))
            print(Book.borrow_a_book(book_name, book_author))

        elif option == '3':
            book_name = str(input(Books_Menu.prompt_dict[option]))
            book_author = str(input(Books_Menu.prompt_dict["0b"]))
            print(Book.return_a_book(book_name, book_author))

        elif option == '4':
            book_name_or_author = str(input(Books_Menu.prompt_dict[option]))
            Book.find_a_book(book_name_or_author)

        elif option == '5':
            Book.list_of_books(False)

        elif option == '6':
            Book.list_of_books(True)

        else:
            print("Quiting program")
            quit()