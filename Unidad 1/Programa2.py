def crearAgenda():
    print("\33[0mCreando agenda...")
    agenda = {}
    while True:
        nombre = input(
            "\33[0m\nIngrese un nombre, o presione enter para finalizar: \33[33m")
        if nombre == "":
            return agenda
        telefono = input("\33[0mIngrese un número de telefono: \33[33m")
        agenda.update({nombre: telefono})
        print("\33[0m\n", len(agenda), "elementos creados")


def mostrarAgenda(agenda):
    print("\33[0mImprimendo agenda...")
    for clave in agenda.keys():
        print("\33[0m- - - - - - - - - - -")
        print("\33[0m\nNombre: \33[32m", clave)
        print("\33[0mTeléfono: \33[32m", agenda[clave])
        print("\33[0m- - - - - - - - - - -")
    print("\33[0m\n", len(agenda), "elementos mostrados")
    input("\33[0mPresione una tecla...")


def editarElemento(agenda):
    clave = input("\33[0mInserte nombre de elemento a editar: \33[34m")
    if clave in agenda.keys():
        tel = input("\33[0mInserte nuevo teléfono: \33[34m")
        agenda[clave] = tel
    else:
        input("\33[0mNo se encontro clave...")
    return agenda


def eliminarElemento(agenda):
    clave = input("\33[0mInserte nombre a eliminar a eliminar: \33[31m")
    if clave in agenda.keys():
        del agenda[clave]
    else:
        input("\33[0mNo se encontro clave...")
    return agenda


agenda = {}

while True:
    print("\33[0m- - - - - - - - - - -")
    print("\33[0mMenú de la agenda")
    print("\33[0m- - - - - - - - - - -")
    print("\33[0m1. Crear agenda")
    print("\33[0m2. Ver agenda")
    print("\33[0m3. Editar elemento")
    print("\33[0m4. Eliminar elemento")
    print("\33[0m- - - - - - - - - - -")
    print("\33[0m0. Salir")
    print("\33[0m- - - - - - - - - - -")
    op = int(input("\33[0mIngrese una opción: \33[35m"))
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

print("\33[0m")
