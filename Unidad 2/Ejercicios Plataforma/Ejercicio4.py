cadena = input("\33[0mIngrese la cadena a separar: \33[34m")
separador = input("\33[0mIngrese el carácter espaciador: \33[34m")[0]
for i in range(10):
    cadena = cadena.replace(str(i), separador)
print("\33[0m")
print("Resultado:\33[33m", cadena, "\33[0m")
