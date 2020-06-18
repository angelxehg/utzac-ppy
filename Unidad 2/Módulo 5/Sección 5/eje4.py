def badFun(n):
    raise ZeroDivisionError


try:
    badFun(0)
except ArithmeticError:
    print("¿Que pasó? ¿Un error?")

print("FIN.")
