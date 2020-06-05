# Elabora una Calculadora suma, resta, multiplicación, división (Con funciones sin retorno y con funciones con valores de retorno).

# Calculadora sin retornos

n1 = int(input("Ingrese primer número: "))
n2 = int(input("Ingrese segundo número: "))
op = input("Escoja operación + - * /: ")
op = op[0]

if op == '+':
    r = n1 + n2
elif op == '-':
    r = n1 - n2
elif op == '*':
    r = n1 * n2
elif op == '/':
    r = n1 / n2
else:
    r = "Operador no soportado"

print("Operación:", n1, op, n2)
print("Resultado:", r)
