import sqlite3

try:
    db = sqlite3.connect("db.sqlite3")
    cursor = db.cursor()
    sentence = """ SELECT * FROM rest;"""
    cursor.execute(sentence)
    dishes = cursor.fetchall()
    print(dishes)
except sqlite3.OperationalError as error:
    print("Error:", error)
