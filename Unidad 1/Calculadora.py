from Paleta import Paleta

print("Calculadora\n")

n1 = float(input(Paleta.CIERRE + "Ingresa el primer número: " + Paleta.AZUL))
n2 = float(input(Paleta.CIERRE + "Ingresa el segundo número: " + Paleta.AZUL))

op = input(Paleta.CIERRE +
           "Escoge una operación: (+, -, *, /, %): " + Paleta.ROJO)


def selector(n1, n2, op):
    if op == '+':
        return n1 + n2
    elif op == '-':
        return n1 - n2
    elif op == '*':
        return n1 * n2
    elif op == '/':
        return n1 / n2
    elif op == '%':
        return n1 % n2
    else:
        return 0


r = selector(n1, n2, op[0])
print(Paleta.CIERRE + "Operación:" + Paleta.AZUL,
      n1, Paleta.ROJO, op, Paleta.AZUL, n2)
print(Paleta.CIERRE + "Resultado:" + Paleta.VERDE, r, Paleta.CIERRE)
