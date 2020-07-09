class Numbers():

    def __init__(self, num1, num2):
        self.__num1 = num1
        self.__num2 = num2

    def added(self):
        return self.__num1 + self.__num2

    def subtracted(self):
        return self.__num1 - self.__num2

    def multiplied(self):
        return self.__num1 * self.__num2

    def divided(self):
        return self.__num1 / self.__num2


numbs = Numbers(
    int(input("Ingrese el primer número: ")),
    int(input("Ingrese el segundo número: "))
)

print("Sumado:", numbs.added())
print("Restado:", numbs.subtracted())
print("Multiplicado:", numbs.multiplied())
print("Dividido:", numbs.divided())
