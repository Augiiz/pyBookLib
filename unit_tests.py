import unittest
from book import Book


class Test_book_methods(unittest.TestCase):

    def test_create_a_book(self):
        self.assertEqual(Book.create_a_book('Knyga', 'Autorius', 2005), 'Knyga')

    def test_borrow_a_book(self):
        Book.create_a_book('Knyga', 'Autorius', 2005)
        self.assertEqual(Book.borrow_a_book('Knyga', 'Autorius'), 'Knyga')

    def test_create_a_copy(self):
        self.assertEqual(Book.create_a_copy('Knyga', 'Autorius'), 'Knyga')

    def test_return_a_book(self):
        self.assertEqual(Book.return_a_book('Five', 'Smith'), 'Failed to return a book, did you misstype the book name?\n')

    def test_return_a_book_2(self):
        self.assertEqual(Book.return_a_book('Five', 'Smith'), 'Five')


if __name__ == '__main__':
    unittest.main(verbosity=2, exit=False)
