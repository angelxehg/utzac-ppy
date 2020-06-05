print("Calculadora\n")

n1 = float(input("Ingresa el primer número: "))
n2 = float(input("Ingresa el segundo número: "))

op = input("Escoge una operación: (+, -, *, /, %): ")


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
print("Operación:", n1, op, n2)
print("Resultado:", r)
