from book import Book


class Starter_Books:
    def fill_book_list():
        Book.book_list.append(Book("LOTR - The Fellowship of the Ring ", "J.R.R Tolkien", 2010, False))
        Book.book_list.append(Book("Encyclopaedia Britannica", "Many", 2006, False))
        Book.book_list.append(Book("Harry Potter and the goblet of fire", "J.K. Rowling", 2000, False))
        Book.book_list.append(Book("Five", "Smith", 2000, False))