import sqlite3
from random import randint, shuffle
from config import database_name


def read_sqlite_table():
    sqlite_connection = sqlite3.connect(database_name)
    cursor = sqlite_connection.cursor()
    # print("Подключен к SQLite")
    sqlite_select_query = """SELECT * from guesswhodb"""
    cursor.execute(sqlite_select_query)
    records = cursor.fetchall()
    raw = randint(0, len(records) - 1)
    example = records[raw]
    cursor.close()
    return example

