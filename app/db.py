import os
from dotenv import load_dotenv
import mysql.connector
from mysql.connector import Error

# Load environment variables
load_dotenv()

db_config = {
    'host': os.getenv('DB_HOST'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'database': 'sakila'
}

def get_connection():
    try:
        connection = mysql.connector.connect(**db_config)
        return connection
    except Error as e:
        print(f"Ошибка подключения к базе данных: {e}")
        return None

def close_connection(connection):
    if connection.is_connected():
        connection.close()
        print("Соединение с базой данных закрыто")
