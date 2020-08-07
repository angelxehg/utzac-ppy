import sqlite3

comida = input("Nombre comida: ")

try:
    db = sqlite3.connect("db.sqlite3")
    cursor = db.cursor()
    sentence = """ DELETE FROM rest WHERE comida = (?);"""
    cursor.execute(sentence, [comida])
    db.commit()
    print("Comida eliminada")
except sqlite3.OperationalError as error:
    print("Error:", error)
