cadena1 = input("\33[0mIngrese la primera cadena: \33[34m")
cadena2 = input("\33[0mIngrese la segunda cadena: \33[34m")
if cadena1.find(cadena2) >= 0:
    print("\33[33m", cadena2, "\33[0m está en\33[33m", cadena1, "\33[0m")
else:
    print("\33[33m", cadena2, "\33[0m no es parte de\33[33m", cadena1, "\33[0m")
lista = [cadena1, cadena2]
lista.sort()
print("\33[33m", lista[0], "\33[0m está antes que\33[33m", lista[1], "\33[0m")
