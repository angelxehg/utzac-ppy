# Elabora un programa que  en una función reciba una lista con 5 nombres desde teclado  y en otra función muestre los nombres introducidos en la primera función.


def crearLista():
    print("Creando lista...")
    lista = []
    for i in range(1, 6):
        nombre = input("Ingrese nombre "+str(i)+": ")
        lista.append(nombre)
    return lista


def imprimirLista(lista):
    print("Imprimiendo lista...")
    for nombre in lista:
        print(nombre)


miLista = crearLista()
imprimirLista(miLista)
