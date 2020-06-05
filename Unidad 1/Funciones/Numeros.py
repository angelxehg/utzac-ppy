# Elabora un programa que contenga cuatro funciones
# 1.Para calcular números pares
# 2.Para calcular la raíz de un numero
# 3.Para calcular si un año es biciesto o no
# 4.Para calcular el factorial de un número

def esPar(num):
    return num % 2 == 0


def raiz(num):
    elev = 1/2
    return num ** elev


def esBisiesto(y):
    if y < 1582:
        return False
    elif y % 4 != 0:
        return False
    elif y % 100 != 0:
        return True
    elif y % 400 != 0:
        return False
    else:
        return True


def fact(num):
    num = int(num)
    if num <= 1:
        # caso base (0 o 1)
        return 1
    else:
        # recursividad
        return num * fact(num - 1)


num = int(input("Ingrese un número entero: "))
yy = int(input("Ingrese un año: "))

if esPar(num):
    print(num, "es par")
else:
    print(num, "no es par")

print("La raiz de", num, "es:", raiz(num))

if esBisiesto(yy):
    print(yy, "es año bisiesto")
else:
    print(yy, "no es año bisiesto")

print("El factorial de", num, "es:", fact(num))
