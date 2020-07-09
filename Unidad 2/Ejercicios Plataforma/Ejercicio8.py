cadena = input("\33[0mIngrese una frase con espacios: \33[34m")
palabras = cadena.split()
letras_inicio = [palabra[0] for palabra in palabras]
cadena_cc = ' '.join([p[0].upper() + p[1:] for p in palabras])
palabras_cc = cadena_cc.split()


def inicia_a(palabra):
    return palabra[0] == 'A'


palabras_a = list(filter(inicia_a, palabras_cc))

print("\33[0mPrimera letra de cada palabra :\33[33m", letras_inicio, "\33[0m")
print("\33[0mCadena en formato Cammel Case :\33[33m", cadena_cc, "\33[0m")
print("\33[0mPalabras que inician con A :\33[33m", palabras_a, "\33[0m")
