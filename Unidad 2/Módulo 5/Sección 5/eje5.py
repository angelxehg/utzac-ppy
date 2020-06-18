def badFun(n):
    try:
        return n / 0
    except:
        print("¡Lo hice otra vez!")
        raise


try:
    badFun(0)
except ArithmeticError:
    print("¡Ya veo!")

print("FIN.")
