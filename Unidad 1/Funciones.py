def Ejemplo():
    """Función sin parametros ni retorno"""
    print("Hola mundo!")
    s = 5+7
    print(s)


def EjemploParam(n1, n2):
    """Función con parametros sin retorno"""
    s = n1 + n2
    print(s)


def EjemploRetorno():
    """Función sin parametros con retorno"""
    s = 5 + 6
    return s


def EjemploRetorno2(n1, n2):
    """Función con parametros y retorno"""
    s = n1 + n2
    return s


Ejemplo()
EjemploParam(1, 2)
print(EjemploRetorno())
print(EjemploRetorno(5, 6))
