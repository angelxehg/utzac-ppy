miTupla = (1, 10, 100, 1000)

print("Elemento 0: ", miTupla[0])
print("Elemento 1: ", miTupla[1])
print("Elemento despues de 1: ", miTupla[1:])
print("Elementos desde la pos -2 ", miTupla[:-2])

print("\nTodos los elementos")
for elemento in miTupla:
    print(elemento)

t1 = miTupla + (1000, 10000)
t2 = miTupla * 3
print("Tupla 1:", t1)
print("Longitud t1:", len(t1))
print("Tupla 2:", t2)
print("Longitud t2:", len(t2))
print(10 in miTupla)
print(-10 not in miTupla)

miTuplaFloat = (1.3, 1.5, 1.8)
print("Tupla flotante:", miTuplaFloat)


def funcionTupla(estaTupla):
    """Datos de la tupla"""
    print("Desde el método")
    print("Elemento 0: ", estaTupla[0])
    print("Elemento 1: ", estaTupla[1])
    print("Elemento despues de 1: ", estaTupla[1:])
    print("Elementos desde la pos -2 ", estaTupla[:-2])


funcionTupla(t1)
