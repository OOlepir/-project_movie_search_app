import sqlite3

def setup_local_db():
    connection = sqlite3.connect('local_search.db')
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS search_queries (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            query_text TEXT NOT NULL
        )
    """)
    connection.commit()
    return connection

def save_query(connection, query_text):
    cursor = connection.cursor()
    cursor.execute("INSERT INTO search_queries (query_text) VALUES (?)", (query_text,))
    connection.commit()

def get_popular_queries(connection):
    cursor = connection.cursor()
    cursor.execute("""
        SELECT query_text, COUNT(*) as count 
        FROM search_queries 
        GROUP BY query_text 
        ORDER BY count DESC 
        LIMIT 10
    """)
    return cursor.fetchall()
