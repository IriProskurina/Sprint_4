import pytest
from books_collector import BooksCollector


class TestBooksCollector:


    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert collector.get_books_genre() == {'Гордость и предубеждение и зомби': '', 'Что делать, если ваш кот хочет вас убить': ''}



    def test_add_new_book_already_added_book(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение')
        collector.add_new_book('Гордость и предубеждение')
        assert collector.get_books_genre() == {'Гордость и предубеждение': ''}


    @pytest.mark.parametrize('name', ['',
                                      'Удивительное путешествие Нильса Хольгерсс',
                                      'Удивительное путишествие Нильса Хольгерссона с дикими гусями по Швеции'])
    def test_add_new_book_name_out_of_range(self, name, books_collection):
        books_collection.add_new_book(name)
        assert len(books_collection.get_books_genre()) == 0

