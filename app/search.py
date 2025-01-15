def search_movies_by_keyword(connection, keyword):
    query = """
        SELECT film.title, film.description 
        FROM film 
        WHERE film.title LIKE %s OR film.description LIKE %s 
        LIMIT 10;
    """
    try:
        cursor = connection.cursor()
        cursor.execute(query, (f"%{keyword}%", f"%{keyword}%"))
        return cursor.fetchall()
    except Exception as e:
        print(f"Ошибка выполнения запроса: {e}")
        return []

def search_movies_by_genre_and_year(connection, genre, year):
    query = """
        SELECT film.title, category.name, film.release_year 
        FROM film
        JOIN film_category ON film.film_id = film_category.film_id
        JOIN category ON film_category.category_id = category.category_id
        WHERE category.name = %s AND film.release_year = %s
        LIMIT 10;
    """
    try:
        cursor = connection.cursor()
        cursor.execute(query, (genre, year))
        return cursor.fetchall()
    except Exception as e:
        print(f"Ошибка выполнения запроса: {e}")
        return []
