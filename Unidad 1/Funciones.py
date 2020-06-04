# Función sin parametros ni retorno
def Ejemplo():
    print("Hola mundo!")
    s = 5+7
    print(s)

# Función con parametros sin retorno


def EjemploParam(n1, n2):
    """function(a, b) -> list"""
    s = n1 + n2
    print(s)

# Función sin parametros con retorno


def EjemploRetorno():
    s = 5 + 6
    return s

# Función con parametros y retorno


def EjemploRetorno2(n1, n2):
    s = n1 + n2
    return s


Ejemplo()
EjemploParam(1, 2)
print(EjemploRetorno())
print(EjemploRetorno(5, 6))
