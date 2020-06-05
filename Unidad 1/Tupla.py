miTupla = (1, 10, 100, 1000)

print("\33[0mElemento 0:\33[34m", miTupla[0])
print("\33[0mElemento 1:\33[34m", miTupla[1])
print("\33[0mElemento despues de 1:\33[34m", miTupla[1:])
print("\33[0mElementos desde la pos -2 \33[34m", miTupla[:-2])

print("\33[0m\nTodos los elementos:\33[33m")
for elemento in miTupla:
    print(elemento)

t1 = miTupla + (1000, 10000)
t2 = miTupla * 3
print("\33[0mTupla 1:\33[33m", t1)
print("\33[0mLongitud t1:\33[35m", len(t1))
print("\33[0mTupla 2:\33[33m", t2)
print("\33[0mLongitud t2:\33[35m", len(t2))
print('\33[32m')
print(10 in miTupla)
print(-10 not in miTupla)

miTuplaFloat = (1.3, 1.5, 1.8)
print("\33[0mTupla flotante:\33[33m", miTuplaFloat)


def funcionTupla(estaTupla):
    """Datos de la tupla"""
    print("\33[0mDesde el método")
    print("\33[0mElemento 0:\33[31m", estaTupla[0])
    print("\33[0mElemento 1:\33[31m", estaTupla[1])
    print("\33[0mElemento despues de 1:\33[31m", estaTupla[1:])
    print("\33[0mElementos desde la pos -2 \33[31m", estaTupla[:-2])


funcionTupla(t1)
print("\33[0m")
