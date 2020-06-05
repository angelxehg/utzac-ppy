miLista = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
tempLista = []
for elemento in miLista:
    if elemento not in tempLista:
        tempLista.append(elemento)
print("La lista solo con elementos únicos:")
print(tempLista)
