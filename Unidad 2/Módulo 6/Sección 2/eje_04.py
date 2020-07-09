class Pila:
    def __init__(self):
        self.__listaPila = []

    def push(self, val):
        self.__listaPila.append(val)

    def pop(self):
        val = self.__listaPila[-1]
        del self.__listaPila[-1]
        return val

class SumarPila(Pila):
    def __init__(self):
        Pila.__init__(self)
        self.__sum = 0

    @property
    def sum(self):
        return self.__sum

    def push(self, val):
        self.__sum += val
        Pila.push(self, val)

    def pop(self):
        val = Pila.pop(self)
        self.__sum -= val
        return val

pila = SumarPila()
pila.push(5)
pila.push(3)
pila.push(1)
print(pila.sum)
