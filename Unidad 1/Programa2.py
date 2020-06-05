def crearAgenda():
    print("Creando agenda...")
    agenda = {}
    while True:
        nombre = input(
            "\nIngrese un nombre, o presione enter para finalizar: ")
        if nombre == "":
            return agenda
        telefono = input("Ingrese un número de telefono:")
        agenda.update({nombre: telefono})
        print(len(agenda), "elementos creados")


def mostrarAgenda(agenda):
    print("Imprimendo agenda...")
    for clave in agenda.keys():
        print("\nNombre:", clave)
        print("Teléfono:", agenda[clave])
    print(len(agenda), "elementos mostrados")
    input("Presione una tecla...")


def editarElemento(agenda):
    clave = input("Inserte nombre de elemento a editar:")
    if clave in agenda.keys():
        tel = input("Inserte nuevo teléfono:")
        agenda[clave] = tel
    else:
        input("No se encontro clave...")
    return agenda


def eliminarElemento(agenda):
    clave = input("Inserte nombre a eliminar a eliminar:")
    if clave in agenda.keys():
        del agenda[clave]
    else:
        input("No se encontro clave...")
    return agenda


agenda = {}

while True:
    print("- - - - - - - - - - -")
    print("Menú de la agenda")
    print("- - - - - - - - - - -")
    print("1. Crear agenda")
    print("2. Ver agenda")
    print("3. Editar elemento")
    print("4. Eliminar elemento")
    print("- - - - - - - - - - -")
    print("0. Salir")
    print("- - - - - - - - - - -")
    op = int(input("Ingrese una opción: "))
    if op == 0:
        break
    elif op == 1:
        agenda = crearAgenda()
    elif op == 2:
        mostrarAgenda(agenda)
    elif op == 3:
        agenda = editarElemento(agenda)
    elif op == 4:
        agenda = eliminarElemento(agenda)
