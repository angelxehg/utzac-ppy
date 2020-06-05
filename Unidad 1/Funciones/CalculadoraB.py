# Elabora una Calculadora suma, resta, multiplicación, división (Con funciones sin retorno y con funciones con valores de retorno).

# Calculadora con retornos

n1 = int(input("Ingrese primer número: "))
n2 = int(input("Ingrese segundo número: "))
op = input("Escoja operación + - * /: ")


def operacion(n1, n2, op):
    if op[0] == '+':
        return n1 + n2
    elif op[0] == '-':
        return n1 - n2
    elif op[0] == '*':
        return n1 * n2
    elif op[0] == '/':
        return n1 / n2
    else:
        return "Operador no soportado"


print("Operación:", n1, op, n2)
print("Resultado:", operacion(n1, n2, op))
