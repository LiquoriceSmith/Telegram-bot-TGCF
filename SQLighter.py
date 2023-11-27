import sqlite3
from random import randint, shuffle
from config import database_name


def read_sqlite_table():  # Чтение из БД
    sqlite_connection = sqlite3.connect(database_name)  # Подключение к определенной БД
    cursor = sqlite_connection.cursor()  # Подключение курсора
    sqlite_select_query = """SELECT * from guesswhodb"""  # Запрос к таблице
    cursor.execute(sqlite_select_query)  # Чтение результатов запроса (двумерный массив)
    records = cursor.fetchall()  # fetchAll() возвращает массив, содержащий все строки результирующего набора
    raw = randint(0, len(records) - 1)  # Случайная строка из двумерного массива
    example = records[raw]
    cursor.close()
    return example
