from helpers.Palette import Palette

print("Calculadora\n")

n1 = float(input(Palette.CIERRE + "Ingresa el primer número: " + Palette.AZUL))
n2 = float(input(Palette.CIERRE + "Ingresa el segundo número: " + Palette.AZUL))

op = input(Palette.CIERRE +
           "Escoge una operación: (+, -, *, /, %): " + Palette.ROJO)


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
print(Palette.CIERRE + "Operación:" + Palette.AZUL,
      n1, Palette.ROJO, op, Palette.AZUL, n2)
print(Palette.CIERRE + "Resultado:" + Palette.VERDE, r, Palette.CIERRE)
