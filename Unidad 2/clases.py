class Ejemplo:

    nombre = ""

    def __init__(self, nombre):
        self.nombre = nombre

    def mi_nombre(self):
        return self.nombre


nombre = input("Introduce un nombre: ")
ob = Ejemplo(nombre)
print("Nombre:", ob.mi_nombre())
