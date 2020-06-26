class Number():

    def __init__(self, number):
        self.__number = number

    def square(self):
        return self.__number ** 2

    def pair(self):
        return self.__number % 2 == 0

    def root(self):
        return self.__number ** (1 / 2)

    def fact(self):
        if self.__number <= 1:
            return 1
        else:
            return self.__number * Number(self.__number - 1).fact()


num = Number(int(input("Ingrese un número: ")))
print("Al cuadrado:", num.square())
print("es par?:", "Si" if num.pair() else "No")
print("Raíz del número:", num.root())
print("Factorial:", num.fact())
