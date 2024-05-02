import pytest
from main import BooksCollector


class TestBooksCollector:

    def test_add_new_book_add_one_book(self):
        collector = BooksCollector()
        collector.add_new_book('Праздник непослушания')
        assert len(collector.get_books_genre()) == 1

    @pytest.mark.parametrize('genre', ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии'])
    def test_set_book_genre_set_genre_one_book(self, genre):
        collector = BooksCollector()
        collector.add_new_book('Трое из Простоквашино')
        collector.set_book_genre('Трое из Простоквашино', genre)
        assert collector.get_book_genre('Трое из Простоквашино') == genre

    

    @pytest.mark.parametrize('genre', ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии'])
    def test_get_books_with_specific_genre_get_books_selected_genre(self, genre):
        collector = BooksCollector()
        collector.add_new_book('Праздник непослушания')
        collector.set_book_genre('Праздник непослушания', genre)
        collector.add_new_book('Маленький принц')
        collector.set_book_genre('Маленький принц', genre)
        assert collector.get_books_with_specific_genre(genre) == ['Праздник непослушания', 'Маленький принц']

    def test_get_books_genre_get_dictionary_wih_one_book(self):
        collector = BooksCollector()
        collector.add_new_book('Праздник непослушания')
        collector.set_book_genre('Праздник непослушания', 'Комедии')
        assert collector.get_books_genre() == {'Праздник непослушания': 'Комедии'}

    def test_get_books_for_children_get_one_book_for_children(self):
        collector = BooksCollector()
        collector.add_new_book('Вий')
        collector.set_book_genre('Вий', 'Ужасы')
        collector.add_new_book('Незнайка на луне')
        collector.set_book_genre('Незнайка на луне', 'Мультфильмы')
        assert collector.get_books_for_children() == ['Незнайка на луне']

    def test_add_book_in_favorites_add__one_book(self):
        collector = BooksCollector()
        collector.add_new_book('Маленький принц')
        collector.add_book_in_favorites('Маленький принц')
        assert 'Маленький принц' in collector.get_list_of_favorites_books()

    def test_delete_book_from_favorites_delete_one_book(self):
        collector = BooksCollector()
        collector.add_new_book('Праздник непослушания')
        collector.add_book_in_favorites('Праздник непослушания')
        collector.delete_book_from_favorites('Праздник непослушания')
        assert 'Праздник непослушания' not in collector.get_list_of_favorites_books()

    def test_get_list_of_favorites_books_get_list_with_one_book(self):
        collector = BooksCollector()
        collector.add_new_book('Маленький принц')
        collector.add_book_in_favorites('Маленький принц')
        assert collector.get_list_of_favorites_books() == ['Маленький принц']


