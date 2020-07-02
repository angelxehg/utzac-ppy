class Animal():

    def acciones(self):
        return []


class Perro(Animal):

    def acciones(self):
        return ['ladrar', 'comer', 'caminar', 'respirar']


class Ave(Animal):

    def acciones(self):
        return ['volar', 'comer', 'respirar']


ave = Ave()
perro = Perro()
animal = Animal()


def polimorfismo(animal):
    return animal.acciones()


print(polimorfismo(ave))
print(polimorfismo(perro))
print(polimorfismo(animal))
