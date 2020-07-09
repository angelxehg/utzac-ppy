cadena = input("\33[0mIngrese la cadena a separar: \33[34m")
separador = input("\33[0mIngrese el carácter separador: \33[34m")[0]
separada = separador.join(cadena)
print("\33[0m")
print("Resultado:\33[33m", separada, "\33[0m")
