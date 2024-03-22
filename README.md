# Финальный проект 4 спринта

## Список тестов: 

### test_add_new_book_add_two_books_books_added()
Добавляем две книги. Проверяем, что они добавились

### test_add_new_book_add_wrong_name_book_books_skipped()
Добавляем книгу с некоректным названием. Проверяем, что ничего не добавилось

### test_set_book_genre_set_genre_genre_setted()
Добавляем книгу, устанавливаем жанр. Проверяем, что жанр применился

### test_set_book_genre_change_genre_genre_changed()
Добавляем книгу, устанавливаем и меняем жанр. Проверяем, что новый жанр применился

### test_set_book_genre_set_wrong_genre_genre_skipped()
Добавляем книгу, устанавливаем неизвестный жанр. Проверяем, что жанр не применился

### test_get_books_with_specific_genre_get_books_with_genre_books_returned()
Добавляем книги, устанавливаем их жанры. Выводим книги определённого жанра. Проверяем, что их количество совпадает с ожидаемым

### test_get_books_for_children_only_allowed_books_returned()
Добавляем книги, устанавливаем их жанры. Выводим книги, подходящие детям. Проверяем, что выводятся только книги, подходящие детям

### test_add_book_in_favorites_add_two_books_books_added()
Добавляем книги в Избранное. Выводим список избранных книг. Проверяем, что он совпадает с ожидаемым.

### test_delete_book_from_favorites_delete_last_book_favorites_empty()
Удаляем книгу из Избранного. Выводим список избранных книг. Проверяем, что она пропала из списка Избранное.

