from app.db import get_connection, close_connection
from app.local_db import setup_local_db, save_query, get_popular_queries
from app.search import search_movies_by_keyword, search_movies_by_genre_and_year

def main():
    remote_connection = get_connection()
    if not remote_connection:
        return

    local_connection = setup_local_db()

    while True:
        print("\nОпции:")
        print("1. Поиск фильмов по ключевому слову")
        print("2. Поиск фильмов по жанру и году")
        print("3. Показать популярные поисковые запросы")
        print("4. Выход")

        choice = input("Выберите опцию: ")
        if choice == "1":
            keyword = input("Введите ключевое слово: ")
            if not keyword.strip():
                print("Ошибка: ключевое слово не может быть пустым.")
                continue

            results = search_movies_by_keyword(remote_connection, keyword)
            if results:
                for row in results:
                    print(f"Название: {row[0]}, Описание: {row[1]}")
                save_query(local_connection, keyword)
            else:
                print("Ничего не найдено.")

        elif choice == "2":
            genre = input("Введите жанр: ")
            year = input("Введите год выпуска: ")
            if not genre.strip() or not year.strip() or not year.isdigit():
                print("Ошибка: некорректный ввод данных.")
                continue

            results = search_movies_by_genre_and_year(remote_connection, genre, int(year))
            if results:
                for row in results:
                    print(f"Название: {row[0]}, Жанр: {row[1]}, Год: {row[2]}")
                save_query(local_connection, f"Жанр: {genre}, Год: {year}")
            else:
                print("Ничего не найдено.")

        elif choice == "3":
            popular_queries = get_popular_queries(local_connection)
            if popular_queries:
                for row in popular_queries:
                    print(f"Запрос: {row[0]}, Количество: {row[1]}")
            else:
                print("Нет популярных запросов.")

        elif choice == "4":
            close_connection(remote_connection)
            local_connection.close()
            print("Программа завершена.")
            break

        else:
            print("Ошибка: некорректный выбор.")

if __name__ == "__main__":
    main()
