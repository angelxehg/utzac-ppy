import sqlite3

from sqlite3 import Error


def sql_connection():
    try:
        con = sqlite3.connect("db.sqlite3")
    except Error:
        print(Error)
    finally:
        con.close()


sql_connection()
