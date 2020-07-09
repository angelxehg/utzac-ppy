cadena = input("\33[0mIngrese la cadena a separar: \33[34m")
separador = input("\33[0mIngrese el carácter espaciador: \33[34m")[0]
separada = ""
for i in range(len(cadena)):
    if i % 3 == 0 and i != 0:
        separada += separador
    separada += cadena[i]
print("\33[0m")
print("Resultado:\33[33m", separada, "\33[0m")
