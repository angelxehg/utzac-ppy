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


def mostrarAgenda(agenda):
    print("Imprimendo agenda...")
    for clave in agenda.keys():
        print("\nNombre:", clave)
        print("Teléfono:", agenda[clave])


def editarElemento(agenda):
    clave = input("Inserte nombre de elemento a editar:")
    if clave in agenda.keys():
        tel = input("Inserte nuevo teléfono:")
        agenda[clave] = tel
    return agenda


def eliminarElemento(agenda):
    clave = input("Inserte nombre a eliminar a eliminar:")
    if clave in agenda.keys():
        del agenda[clave]
    return agenda


agenda = crearAgenda()
mostrarAgenda(agenda)
agenda = editarElemento(agenda)
mostrarAgenda(agenda)
agenda = eliminarElemento(agenda)
mostrarAgenda(agenda)
