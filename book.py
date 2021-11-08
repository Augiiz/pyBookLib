class Book:
    book_list = []
    specific_book_by_year_list = []

    def __init__(self, book_name, book_author, release_date, taken):
        self.book_name = book_name
        self.book_author = book_author
        self.release_date = release_date
        self.taken = taken

    def list_of_books(taken):
        print("Book name | Author | Release Date")
        found_books = False
        for book in Book.book_list:
            if book.taken is taken:
                found_books = True
                print(book.book_name, " | ", book.book_author, " | ", book.release_date)

        if not found_books:
            print("No books has been found")
        print("\n")

    def create_a_book(book_name, book_author, release_date):
        Book.book_list.append(Book(book_name, book_author, release_date, False))
        print("The book has been succesfully placed in the library: ", end=" ")
        return book_name

    def create_a_copy(book_name, book_author):
        for book in Book.book_list:
            if book_name == book.book_name and book_author == book.book_author:
                Book.create_a_book(book.book_name, book.book_author, book.release_date)
                return book_name
        return "Such book was not found"

    def borrow_a_book(book_name, book_author):
        for book in Book.book_list:
            if book_name == book.book_name and book_author == book.book_author and book.taken is False:
                book.taken = True
                print("Book succesfully borrowed: ", end=" ")
                return book_name
        return "Failed to borrow a book, did you misstype the book name?\n"

    def return_a_book(book_name, book_author):
        for book in Book.book_list:
            if book_name == book.book_name and book_author == book.book_author and book.taken is True:
                book.taken = False
                print("Book succesfully returned: ", end=" ")
                return book_name
        return "Failed to return a book, did you misstype the book name?\n"

    def find_a_book(book_name_or_author):
        Book.clear_year_list()
        print("Book name | Author | Release Date")
        for book in Book.book_list:
            if book_name_or_author == book.book_name or book_name_or_author == book.book_author:
                Book.specific_book_by_year_list.append(Book(book.book_name, book.book_author, book.release_date, False))

        Book.sort_books_by_date()

        for book in Book.specific_book_by_year_list:
            print(book.book_name, " | ", book.book_author, " | ", book.release_date)
        if not Book.specific_book_by_year_list:
            print("No books has been found")

    def clear_year_list():
        Book.specific_book_by_year_list.clear()

    def sort_books_by_date():
        Book.specific_book_by_year_list.sort(key=lambda book: book.release_date, reverse=True)