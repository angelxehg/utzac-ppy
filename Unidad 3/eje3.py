class Cocinero():
    def prepararPlatillo(self):
        self.cuchillo = Cuchillo()
        self.cuchillo.cortarVegetales()
        self.estufa = Estufa()
        self.estufa.boilVegetables()
        self.freidora = Freidora()
        self.freidora.freirVegetales()


class Cuchillo():
    def cortarVegetales(self):
        print("Todos los vegetales fueron cortados")


class Estufa():
    def boilVegetables(self):
        print("Todos los vegetales fueron hervidos")


class Freidora():
    def freirVegetales(self):
        print("Todos los vegetales fueron mezclados y freidos")


if __name__ == "__main__":
    Cocinero = Cocinero()
    Cocinero.prepararPlatillo()
