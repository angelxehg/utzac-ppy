import sqlite3

comida = input("Nueva comida: ")

try:
    db = sqlite3.connect("db.sqlite3")
    cursor = db.cursor()
    sentence = """ INSERT INTO rest(comida) VALUES (?);"""
    cursor.execute(sentence, [comida])
    db.commit()
    print("Comida insertada")
except sqlite3.OperationalError as error:
    print("Error:", error)
