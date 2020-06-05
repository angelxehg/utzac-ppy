from helpers.Color import Color

print("Calculadora\n")

n1 = float(input(Color.DEFAULT + "Ingresa el primer número: " + Color.BLUE))
n2 = float(input(Color.DEFAULT + "Ingresa el segundo número: " + Color.BLUE))

op = input(Color.DEFAULT +
           "Escoge una operación: (+, -, *, /, %): " + Color.RED)


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
print(Color.DEFAULT + "Operación:" + Color.BLUE,
      n1, Color.RED, op, Color.BLUE, n2)
print(Color.DEFAULT + "Resultado:" + Color.GREEN, r, Color.DEFAULT)
