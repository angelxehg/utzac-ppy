def capturaCalificaciones():
    print("\33[0mCapturando calificaciones...")
    lista = []
    for i in range(1, 11):
        calif = int(
            input("\33[0mIngrese calificación " + str(i) + ": \33[33m"))
        lista.append(calif)
    return lista


def capturaPrecios():
    print("\33[0mCapturando precios...")
    tupla = ()
    for i in range(1, 11):
        calif = float(input("\33[0mIngrese precio " + str(i) + ": \33[33m"))
        tupla += (calif,)
    return tupla


def procesarLista(lista):
    print("\33[0mProcesando lista...")
    print("\33[0mPrimer elemento: \33[32m", lista[0])
    print("\33[0mUltimo elemento: \33[32m", lista[-1])
    print("\33[0mPrimeros 3 elementos: \33[32m", lista[0:3])
    print("\33[0mUltimos 3 elementos: \33[32m", lista[-3:10])
    print("\33[0mElemento mayor: \33[32m", sorted(lista)[-1])
    print("\33[0mElemento menor: \33[32m", sorted(lista)[0])


def procesarTupla(tupla):
    print("\33[0mProcesando tupla...")
    print("\33[0mPrimer elemento: \33[34m", tupla[0])
    print("\33[0mUltimo elemento: \33[34m", tupla[-1])
    print("\33[0mPrimeros 3 elementos: \33[34m", tupla[0:3])
    print("\33[0mUltimos 3 elementos: \33[34m", tupla[-3:10])
    print("\33[0mElemento mayor: \33[34m", sorted(tupla)[-1])
    print("\33[0mElemento menor: \33[34m", sorted(tupla)[0])


calificaciones = capturaCalificaciones()
print(calificaciones)
procesarLista(calificaciones)

precios = capturaPrecios()
print(precios)
procesarTupla(precios)

print("\33[0m")
