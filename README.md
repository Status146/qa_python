# qa_python_4
___
## Содержание:

### `main.py`  
- приложение BooksCollector - оно позволяет установить жанр книг и добавить их в избранное  
### `tests.py`  
- TestBooksCollector - юнит-тесты, которые покрвают BooksCollector  
### `conftest.py`  
- файл pytest, предназначенный для хранения фикстур

## Описание Юнит-тестов:

### 1. test_add_new_book:

1.1 `test_add_new_book_add_two_books` - исправленый тест успешного добавления двух книг в словарь books_rating  
1.2 `test_add_new_book_add_two_equal_books` - проверка добавления книг с одинаковым именем  
1.3 `test_add_new_book_add_name_not_valid` - проверка на валидность добавленной книги (> 40, =0)

### 2. test_add_book_in_favorites:

2.1 `test_add_book_in_favorites` - успешное добавление книги в Избранное  
2.2 `test_add_book_in_favorites_book_already_in_favorites` - проверка добавления в избранное книг с одинаковым именем  
2.3 `test_add_book_in_favorites_book_not_exist` - проверка добавления в избранное книги, которая отсутствует в get_books_genre

### 3. test_delete_book_from_favorite:

3.1 `test_delete_book_from_favorite` - успешное удаление книги из Избранного  
3.2 `test_delete_book_from_favorite_book_not_exist` - проверка удаления из избранного книги, которая отсутствует в get_books_genre

### 4. test_get_book_genre:

4.1 `test_get_book_genre` - параметризированная успешная проверка получения жанра книги по её имени  
4.2 `test_get_book_genre_no_book_genre` - проверка, что жанр книге присвоен по умолчанию
4.3 `test_get_book_genre_book_not_exist` - проверка жанра у отсутствующей книги

### 5. test_set_book_genre:

5.1 `test_set_book_genre` - успешно устанавливаем книге жанр  
5.2 `test_set_book_genre_book_not_exist` - проверка установки жанра несуществующей книге  
5.3 `test_set_book_genre_genre_not_exist` - проверка установки книге несуществующего жанра

### 6. test_get_books_genre:

6.1 `test_get_books_genre` - успешно получаем словарь books_genre  
6.2 `test_get_books_genre_books_genre_empty` - проверка что словарь books_genre пуст

### 7. test_get_books_for_children:

7.1 `test_get_books_for_children` - успешно возвращаем книги, подходящие детям  
7.2 `test_get_books_for_children_book_not_in_age_rating` - проверка, что неподходящая книга не попала в детские  
7.3 `test_get_books_for_children_genre_not_exist` - проверка, что книга с несуществующим жанром не попала в детские

### 8. test_get_books_with_specific_genre:

8.1 `test_get_books_with_specific_genre` - успешно выводим список книг с определённым жанром

### 9. test_get_list_of_favorites_books:

8.2 `test_get_list_of_favorites_books` - успешно получаем список Избранных книг


