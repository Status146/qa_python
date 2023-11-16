import pytest


class TestBooksCollector:

    def test_add_new_book_add_two_books(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_genre()) == 2

    def test_add_new_book_add_two_equal_books(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Гордость и предубеждение и зомби')
        assert len(collector.get_books_genre()) == 1

    @pytest.mark.parametrize('name', ['', 'This book is not valid they have 41 sumb.'])
    def test_add_new_book_name_not_valid(self, name, collector):
        collector.add_new_book(name)
        assert len(collector.get_books_genre()) == 0

    def test_add_book_in_favorites(self, collector):
        book = 'book_1'
        collector.add_new_book(book)
        collector.add_book_in_favorites(book)
        assert len(collector.get_list_of_favorites_books()) == 1
        assert book in collector.get_list_of_favorites_books()

    def test_add_book_in_favorites_book_already_in_favorites(self, collector):
        book = 'book_1'
        collector.add_new_book(book)
        collector.add_book_in_favorites(book)
        collector.add_book_in_favorites(book)
        assert len(collector.get_list_of_favorites_books()) == 1
        assert book in collector.get_list_of_favorites_books()

    def test_add_book_in_favorites_book_not_exist(self, collector):
        book = 'book_1'
        collector.add_book_in_favorites(book)
        assert len(collector.get_list_of_favorites_books()) == 0
        assert book not in collector.get_list_of_favorites_books()

    def test_delete_book_from_favorite(self, collector):
        book = 'book_1'
        collector.add_new_book(book)
        collector.add_book_in_favorites(book)
        collector.delete_book_from_favorites(book)
        assert len(collector.get_list_of_favorites_books()) == 0
        assert book not in collector.get_list_of_favorites_books()

    def test_delete_book_from_favorite_book_not_exist(self, collector):
        book = 'book_1'
        collector.delete_book_from_favorites(book)
        assert len(collector.get_list_of_favorites_books()) == 0
        assert book not in collector.get_list_of_favorites_books()

    @pytest.mark.parametrize('name, genre', [['scared_book', 'Ужасы'], ['fantastic_book', 'Фантастика']])
    def test_get_book_genre(self, name, genre, collector):
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.get_book_genre(name) == genre

    def test_get_book_genre_no_book_genre(self, collector):
        collector.add_new_book('Zorro')
        assert collector.get_book_genre('Zorro') == ''

    def test_get_book_genre_book_not_exist(self, collector):
        assert collector.get_book_genre('Zorro') is None

    def test_set_book_genre(self, collector):
        collector.add_new_book('Zorro')
        collector.set_book_genre('Zorro', 'Фантастика')
        assert collector.get_book_genre('Zorro') == 'Фантастика'

    def test_set_book_genre_book_not_exist(self, collector):
        collector.set_book_genre('book_1', 'Детективы')
        assert collector.get_book_genre('book_1') is None

    def test_set_book_genre_genre_not_exist(self, collector):
        collector.add_new_book('Lion King')
        collector.set_book_genre('Lion King', 'Сказки')
        assert collector.get_book_genre('Lion King') == ''

    def test_get_books_genre(self, collector):
        collector.add_new_book('book_1')
        collector.add_new_book('book_2')
        collector.add_new_book('book_3')
        assert len(collector.get_books_genre()) == 3

    def test_get_books_genre_books_genre_empty(self, collector):
        assert len(collector.get_books_genre()) == 0

    def test_get_books_for_children(self, collector):
        collector.add_new_book('The Rolling Roll')
        collector.set_book_genre('The Rolling Roll', 'Мультфильмы')
        assert len(collector.get_books_for_children()) == 1
        assert 'The Rolling Roll' in collector.get_books_for_children()

    def test_get_books_for_children_book_not_in_age_rating(self, collector):
        collector.add_new_book('Murder, She Wrote')
        collector.set_book_genre('Murder, She Wrote', 'Детективы')
        assert 'Murder, She Wrote' not in collector.get_books_for_children()

    def test_get_books_for_children_genre_not_exist(self, collector):
        collector.add_new_book('Neznaika')
        collector.set_book_genre('Neznaika', 'Russian Fairy Tales')
        assert len(collector.get_books_for_children()) == 0

    def test_get_books_with_specific_genre(self, collector):
        collector.add_new_book('Murder, She Wrote')
        collector.add_new_book('Sherlock')
        collector.add_new_book('Friends')
        collector.set_book_genre('Sherlock', 'Детективы')
        collector.set_book_genre('Murder, She Wrote', 'Детективы')
        collector.set_book_genre('Friends', 'Комедии')
        assert all(i in collector.get_books_with_specific_genre('Детективы') for i in ['Sherlock', 'Murder, She Wrote'])

    def test_get_list_of_favorites_books(self, collector):
        collector.add_new_book('book_1')
        collector.add_new_book('book_2')
        collector.add_new_book('book_3')
        collector.add_book_in_favorites('book_1')
        collector.add_book_in_favorites('book_2')
        assert all(i in collector.get_list_of_favorites_books() for i in ['book_1', 'book_2'])
