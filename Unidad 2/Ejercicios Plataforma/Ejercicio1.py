cadena = input("\33[0mIngrese una cadena: \33[34m")
print("\33[0mPrimeros caracteres:\33[33m", cadena[0:2])
print("\33[0mÚltimos caracteres:\33[33m", cadena[-3:])
print("\33[0mCada 2 caracteres: \33[33m", end='')
for i in range(len(cadena)):
    if i % 2 == 0:
        print(cadena[i], end='')
print("\33[0m")
reversa = ''.join(reversed(cadena))
espejo = cadena + reversa
print("\33[0mCadena inversa:\33[33m", reversa)
print("\33[0mCadena espejo:\33[33m", espejo)
print("\33[0m")
