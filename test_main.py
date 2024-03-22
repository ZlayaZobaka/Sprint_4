import pytest

from main import BooksCollector


class TestBooksCollector:

    @pytest.fixture(scope='function', autouse=True)
    def collector(self):
        self.collector = BooksCollector()

    def test_add_new_book_add_two_books_books_added(self):
        #Добавляем две книги. Проверяем, что они добавились

        self.collector.add_new_book('Гордость и предубеждение и зомби')
        self.collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        assert len(self.collector.get_books_genre()) == 2

    @pytest.mark.parametrize(
        'book_name',
        [
            '',
            'Удивительное путешествие Нильса Хольгерссона с дикими гусями по Швеции'
        ]
    )
    def test_add_new_book_add_wrong_name_book_books_skipped(self, book_name):
        # Добавляем книгу с некоректным названием. Проверяем, что ничего не добавилось

        self.collector.add_new_book(book_name)

        assert len(self.collector.get_books_genre()) == 0

    @pytest.mark.parametrize(
        'book_name, book_genre',
        [
            ['Квантовая механика', 'Ужасы'],
            ['Преступление и наказание', 'Фантастика']
        ]
    )
    def test_set_book_genre_set_genre_genre_setted(self, book_name, book_genre):
        # Добавляем книгу, устанавливаем жанр. Проверяем, что жанр применился

        self.collector.add_new_book(book_name)
        self.collector.set_book_genre(book_name, book_genre)

        assert (len(self.collector.get_books_genre()) == 1
                and
                self.collector.get_book_genre(book_name) == book_genre)

    def test_set_book_genre_change_genre_genre_changed(self):
        # Добавляем книгу, устанавливаем и меняем жанр. Проверяем, что новый жанр применился

        book_name = 'Винни-Пух и все-все-все.'
        self.collector.add_new_book(book_name)

        self.collector.set_book_genre(book_name, 'Детективы')
        self.collector.set_book_genre(book_name, 'Мультфильмы')

        assert self.collector.get_book_genre(book_name) == 'Мультфильмы'

    def test_set_book_genre_set_wrong_genre_genre_skipped(self):
        # Добавляем книгу, устанавливаем неизвестный жанр. Проверяем, что жанр не применился

        book_name = 'Каштанка'
        self.collector.add_new_book(book_name)
        self.collector.set_book_genre(book_name, 'Нуар')

        assert self.collector.get_book_genre(book_name) == ''

    @pytest.mark.parametrize(
        'books, genre, quantity',
        [
            [
                {
                    'Приключения Незнайки': 'Мультфильмы',
                    'Маша и Медведь': 'Мультфильмы'
                },
                'Мультфильмы',
                2
            ],
            [
                {
                    'Следствие ведут колобки': 'Детективы',
                    'Фиксики': 'Мультфильмы'
                },
                'Детективы',
                1
            ]
        ]
    )
    def test_get_books_with_specific_genre_get_books_with_genre_books_returned(self, books, genre, quantity):
        # Добавляем книги, устанавливаем их жанры. Выводим книги определённого жанра
        # Проверяем, что их количество совпадает с ожидаемым

        for book_name in books:
            self.collector.add_new_book(book_name)
            self.collector.set_book_genre(book_name, books[book_name])

        assert len(self.collector.get_books_with_specific_genre(genre)) == quantity

    def test_get_books_for_children_only_allowed_books_returned(self):
        # Добавляем книги, устанавливаем их жанры. Выводим книги, подходящие детям
        # Проверяем, что выводятся только книги, подходящие детям

        books = {
            'Тайна третьей планеты': 'Фантастика',
            'Шрек': 'Мультфильмы',
            'Кто подставил кролика Роджера': 'Детективы'
        }

        for book_name in books:
            self.collector.add_new_book(book_name)
            self.collector.set_book_genre(book_name, books[book_name])

        assert (len(self.collector.get_books_for_children()) == 2
                and
                'Кто подставил кролика Роджера' not in self.collector.get_books_for_children())

    def test_add_book_in_favorites_add_two_books_books_added(self):
        # Добавляем книги в Избранное. Выводим список избранных книг
        # Проверяем, что он совпадает с ожидаемым

        books = {
            'Автостопом по Галактике': 'Комедии',
            'Собака Баскервилей': 'Детективы'
        }

        for book_name in books:
            self.collector.add_new_book(book_name)
            self.collector.set_book_genre(book_name, books[book_name])
            self.collector.add_book_in_favorites(book_name)

        assert self.collector.get_list_of_favorites_books() == [name for name in books]

    def test_delete_book_from_favorites_delete_last_book_favorites_empty(self):
        # Удаляем книгу из Избранного. Выводим список избранных книг
        # Проверяем, что она пропала из списка Избранное

        book_name = 'Поваренная книга анархиста'
        self.collector.add_new_book(book_name)
        self.collector.add_book_in_favorites(book_name)
        self.collector.delete_book_from_favorites(book_name)

        assert len(self.collector.get_list_of_favorites_books()) == 0
