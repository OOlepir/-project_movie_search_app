def save_search_query(connection, query):
    insert_query = """
        INSERT INTO search_queries (query_text) VALUES (%s);
    """
    try:
        cursor = connection.cursor()
        cursor.execute(insert_query, (query,))
        connection.commit()
    except Error as e:
        print(f"Error saving search query: {e}")

def display_popular_queries(connection):
    query = """
        SELECT query_text, COUNT(*) as count 
        FROM search_queries 
        GROUP BY query_text 
        ORDER BY count DESC 
        LIMIT 10;
    """
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()
    except Error as e:
        print(f"Error retrieving popular queries: {e}")
        return []
