entrada = ""
numero = 0
while True:
    entrada = input("\33[0mIngrese un número: \33[34m")
    try:
        numero = int(entrada)
        entrada = str(numero)
        break
    except:
        print("\33[31mNúmero no es entero!!")

formateado = ""
for i in range(len(entrada)):
    if i % 3 == 0 and i != 0:
        formateado = "," + formateado
    formateado = entrada[-1 - i] + formateado

print("\33[0mNúmero con formato:\33[33m", formateado, "\33[0m")
