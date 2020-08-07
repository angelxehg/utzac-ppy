import sqlite3
from sqlite3 import Error
from os import system, name


def clear():
    """ Clear console output """
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


def sql_select():
    try:
        db = sqlite3.connect("db.sqlite3")
        cursor = db.cursor()
        sentence = """ SELECT rowid, comida FROM rest;"""
        cursor.execute(sentence)
        dishes = cursor.fetchall()
        for dish in dishes:
            print("{}: {}".format(dish[0], dish[1]))
    except sqlite3.OperationalError as error:
        print("Error:", error)


def sql_insert(comida):
    try:
        db = sqlite3.connect("db.sqlite3")
        cursor = db.cursor()
        sentence = """ INSERT INTO rest(comida) VALUES (?);"""
        cursor.execute(sentence, [comida])
        db.commit()
        print("Comida insertada")
    except sqlite3.OperationalError as error:
        print("Error:", error)


def sql_update(id, newval):
    try:
        db = sqlite3.connect("db.sqlite3")
        cursor = db.cursor()
        sentence = """ UPDATE rest SET comida = (?) WHERE rowid = (?);"""
        cursor.execute(sentence, [newval, id])
        db.commit()
        print("Comida actualizada")
    except sqlite3.OperationalError as error:
        print("Error:", error)


def sql_delete(id):
    try:
        db = sqlite3.connect("db.sqlite3")
        cursor = db.cursor()
        sentence = """ DELETE FROM rest WHERE rowid = (?);"""
        cursor.execute(sentence, [id])
        db.commit()
        print("Comida eliminada")
    except sqlite3.OperationalError as error:
        print("Error:", error)


while True:
    clear()
    print("""
CRUD Restaurant

Options:
1. List all records
2. Create a new record
3. Update a record
4. Remove a record

0. Exit
    """)
    op = int(input("Select an option: "))
    clear()
    if op == 1:
        print("List of records:")
        sql_select()
        input("\nPress a key to continue...")
    elif op == 2:
        print("Create a record")
        comida = input("Nueva comida: ")
        sql_insert(comida)
        input("\nPress a key to continue...")
    elif op == 3:
        print("Update a record")
        sql_select()
        sel_id = int(input("\nID del elemento: "))
        newval = input("Nuevo valor: ")
        sql_update(sel_id, newval)
        input("\nPress a key to continue...")
    elif op == 4:
        print("Remove a record")
        sql_select()
        sel_id = int(input("\nID del elemento: "))
        sql_delete(sel_id)
        input("\nPress a key to continue...")
    else:
        break
