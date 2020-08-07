import sqlite3

comida = input("Nombre comida: ")
nuevo = input("Nuevo nombre comida: ")

try:
    db = sqlite3.connect("db.sqlite3")
    cursor = db.cursor()
    sentence = """ UPDATE rest SET comida = (?) WHERE comida = (?);"""
    cursor.execute(sentence, [nuevo, comida])
    db.commit()
    print("Comida actualizada")
except sqlite3.OperationalError as error:
    print("Error:", error)
