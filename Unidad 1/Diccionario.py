diccionario = {"gato": "chat", "perro": "chien", "caballo": "cheval"}
telefonos = {"jefe": 5551234567, "Suzy": 22657854310}
vacio = {}

print(diccionario)
print(telefonos)
print("gato...", diccionario["gato"], "\n")

palabras = ['gato', 'leon', 'clave']

for palabra in palabras:
    if palabra in diccionario:
        print(palabra, ">", diccionario[palabra])
    else:
        print(palabra, "no está en el diccionario")

for clave in diccionario.keys():
    print(clave, ">", diccionario[clave])

for key in sorted(diccionario.keys()):
    print(key, ">", diccionario[key])

for french in diccionario.values():
    print(french)

diccionario['gato'] = "minou"
print(diccionario)

diccionario['cisne'] = "cygne"
diccionario.update({"pato": "canard"})
print(diccionario)

del diccionario['perro']
print(diccionario)
