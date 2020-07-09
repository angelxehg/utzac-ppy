class Color:

    BLACK = '\33[30m'
    RED = '\33[31m'
    GREEN = '\33[32m'
    YELLOW = '\33[33m'
    BLUE = '\33[34m'
    PURPLE = '\33[35m'
    BEIGE = '\33[36m'
    WHITE = '\33[37m'
    RESET = '\33[0m'


class Edificacion:
    altura = 0
    dueno = ""
    precio = 0
    ubicacion = ""

    def __init__(self, altura, dueno, precio, ubicacion):
        self.altura = altura
        self.dueno = dueno
        self.precio = precio
        self.ubicacion = ubicacion

    def __str__(self):
        cadena = Color.YELLOW + "(Edificio)"
        cadena += Color.RESET + " Dueño: " + Color.BEIGE + self.dueno
        cadena += Color.RESET + " Altura: " + Color.BEIGE + str(self.altura)
        cadena += Color.RESET + " Precio: " + Color.BEIGE + str(self.precio)
        cadena += Color.RESET + " Ubicación: " + Color.BEIGE + self.dueno
        return cadena + Color.RESET

    def get_altura(self):
        return self.altura

    def set_altura(self, altura):
        self.altura = altura

    def get_dueno(self):
        return self.dueno

    def set_dueno(self, dueno):
        self.dueno = dueno

    def get_precio(self):
        return self.precio

    def set_precio(self, precio):
        self.precio = precio

    def get_ubicacion(self):
        return self.ubicacion

    def set_ubicacion(self, ubicacion):
        self.ubicacion = ubicacion


class Casa(Edificacion):

    habitantes = 0

    def __init__(self, altura, dueno, precio, ubicacion, habitantes):
        self.habitantes = habitantes
        super().__init__(altura, dueno, precio, ubicacion)

    def __str__(self):
        base = super().__str__()
        indice = base.find(')') + 1
        cadena = Color.PURPLE + "(Casa)"
        cadena += base[indice:]
        cadena += Color.RESET + " Habitantes: " + \
            Color.BEIGE + str(self.habitantes)
        return cadena + Color.RESET

    def get_habitantes(self):
        return self.habitantes

    def set_habitantes(self, habitantes):
        self.habitantes = habitantes


class Comercial(Edificacion):

    areas_comercio = []

    def __init__(self, altura, dueno, precio, ubicacion, areas_comercio):
        self.areas_comercio = areas_comercio
        super().__init__(altura, dueno, precio, ubicacion)

    def __str__(self):
        base = super().__str__()
        indice = base.find(')') + 1
        cadena = Color.GREEN + "(Comercial)"
        cadena += base[indice:]
        cadena += Color.RESET + " Areas comercio: " + \
            Color.BEIGE + str(len(self.areas_comercio))
        return cadena + Color.RESET

    def get_areas_comercio(self, areas_comercio):
        return self.areas_comercio

    def set_areas_comercio(self, areas_comercio):
        self.areas_comercio = areas_comercio


class Gubernamental(Edificacion):

    seguridad = 0

    def __init__(self, altura, dueno, precio, ubicacion, seguridad):
        self.seguridad = seguridad
        super().__init__(altura, dueno, precio, ubicacion)

    def __str__(self):
        base = super().__str__()
        indice = base.find(')') + 1
        cadena = Color.RED + "(Gubernamental)"
        cadena += base[indice:]
        cadena += Color.RESET + " Seguridad: " + \
            Color.BEIGE + str(self.seguridad)
        return cadena + Color.RESET

    def get_seguridad(self, seguridad):
        return self.seguridad

    def set_seguridad(self, seguridad):
        self.seguridad = seguridad


edificacion_generica = Edificacion(
    15,
    "Angel Hurtado",
    10000,
    "#132 Fake St."
)

casa_angel = Casa(
    6,
    "Angel Hurtado",
    10000,
    "#111 Fake St.",
    3
)

plaza_miguel = Comercial(
    9,
    "Don Miguel",
    15000,
    "#343 Fake St.",
    ['Banco ABC', 'Ropas X', 'Fast Food']
)

gobierno_zac = Gubernamental(
    20,
    "Gobierno Zacatecas",
    25000,
    "#456 Fake St.",
    5
)

edificaciones = [
    edificacion_generica,
    casa_angel,
    plaza_miguel,
    gobierno_zac
]

print("Todos los edificios:")
for edificio in edificaciones:
    print(edificio)
