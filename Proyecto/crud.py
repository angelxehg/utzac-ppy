import sqlite3
from sqlite3 import Error
from os import system, name


def clear():
    """ Clear console output """
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


def q_select():
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


def q_insert(comida):
    try:
        db = sqlite3.connect("db.sqlite3")
        cursor = db.cursor()
        sentence = """ INSERT INTO rest(comida) VALUES (?);"""
        cursor.execute(sentence, [comida])
        db.commit()
        print("Comida insertada")
    except sqlite3.OperationalError as error:
        print("Error:", error)


def q_update(id, newval):
    try:
        db = sqlite3.connect("db.sqlite3")
        cursor = db.cursor()
        sentence = """ UPDATE rest SET comida = (?) WHERE rowid = (?);"""
        cursor.execute(sentence, [newval, id])
        db.commit()
        print("Comida actualizada")
    except sqlite3.OperationalError as error:
        print("Error:", error)


def q_delete(id):
    try:
        db = sqlite3.connect("db.sqlite3")
        cursor = db.cursor()
        sentence = """ DELETE FROM rest WHERE rowid = (?);"""
        cursor.execute(sentence, [id])
        db.commit()
        print("Comida eliminada")
    except sqlite3.OperationalError as error:
        print("Error:", error)


def list():
    clear()
    print("List of records:")
    q_select()
    input("\nPress a key to continue...")


def create():
    clear()
    print("Create a record")
    comida = input("Nueva comida: ")
    q_insert(comida)
    input("\nPress a key to continue...")


def update():
    clear()
    print("Update a record")
    q_select()
    sel_id = int(input("\nID del elemento: "))
    newval = input("Nuevo valor: ")
    q_update(sel_id, newval)
    input("\nPress a key to continue...")


def remove():
    clear()
    print("Remove a record")
    q_select()
    sel_id = int(input("\nID del elemento: "))
    q_delete(sel_id)
    input("\nPress a key to continue...")


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
    if op == 1:
        list()
    elif op == 2:
        create()
    elif op == 3:
        update()
    elif op == 4:
        remove()
    else:
        break
