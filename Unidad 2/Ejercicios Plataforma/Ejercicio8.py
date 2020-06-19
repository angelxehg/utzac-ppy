cadena = input("\33[0mIngrese una frase con espacios: \33[34m")
letras = [palabra[0] for palabra in cadena.split()]
print("\33[0mPrimera letra de cada palabra :\33[33m", letras, "\33[0m")
