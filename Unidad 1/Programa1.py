def capturaCalificaciones():
    print("Capturando calificaciones...")
    lista = []
    for i in range(1, 11):
        calif = int(input("Ingrese calificación " + str(i) + ": "))
        lista.append(calif)
    return lista


def capturaPrecios():
    print("Capturando precios...")
    tupla = ()
    for i in range(1, 11):
        calif = float(input("Ingrese precio " + str(i) + ": "))
        tupla += (calif,)
    return tupla


def procesarLista(lista):
    print("Procesando lista...")
    print("Primer elemento:", lista[0])
    print("Ultimo elemento:", lista[-1])
    print("Primeros 3 elementos:", lista[0:3])
    print("Ultimos 3 elementos:", lista[-3:10])
    print("Elemento mayor:", sorted(lista)[-1])
    print("Elemento menor:", sorted(lista)[0])


def procesarTupla(tupla):
    print("Procesando tupla...")
    print("Primer elemento:", tupla[0])
    print("Ultimo elemento:", tupla[-1])
    print("Primeros 3 elementos:", tupla[0:3])
    print("Ultimos 3 elementos:", tupla[-3:10])
    print("Elemento mayor:", sorted(tupla)[-1])
    print("Elemento menor:", sorted(tupla)[0])


calificaciones = capturaCalificaciones()
print(calificaciones)
procesarLista(calificaciones)

precios = capturaPrecios()
print(precios)
procesarTupla(precios)
