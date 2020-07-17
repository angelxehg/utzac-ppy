class Potencia(object):
    def __init__(self, arg):
        self._arg = arg

    def __call__(self, a, b):
        retval = self._arg(a, b)
        return retval ** 2


@Potencia
def multiplicar(a, b):
    return a * b
