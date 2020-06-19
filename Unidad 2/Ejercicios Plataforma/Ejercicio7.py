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
reverse_len = 0 - len(entrada)
for i in range(reverse_len, 0):
    reverse_index = i - reverse_len
    if reverse_index % 3 == 0 and reverse_index != 0:
        formateado = "," + formateado
    formateado = entrada[-1 - i] + formateado

print("\33[0mNúmero con formato:\33[33m", formateado, "\33[0m")
