import sqlite3
from random import randint, shuffle


def read_sqlite_table():
    sqlite_connection = sqlite3.connect('guesswhodb.db')
    cursor = sqlite_connection.cursor()
    # print("Подключен к SQLite")

    sqlite_select_query = """SELECT * from guessswhodb"""
    cursor.execute(sqlite_select_query)
    records = cursor.fetchall()
    raw = randint(0, len(records) - 1)
    example = records[raw]
    cursor.close()
    return example
# print(read_sqlite_table()[1])
