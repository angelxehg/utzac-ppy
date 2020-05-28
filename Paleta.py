class Paleta:

    NEGRO = '\33[30m'
    ROJO = '\33[31m'
    VERDE = '\33[32m'
    AMARILLO = '\33[33m'
    AZUL = '\33[34m'
    PURPURA = '\33[35m'
    BEIGE = '\33[36m'
    BLANCO = '\33[37m'

    CIERRE = '\33[0m'

    @staticmethod
    @staticmethod
    def muestra(self):
        x = 0
        for i in range(24):
            colors = ""
            for j in range(5):
                code = str(x+j)
                colors = colors + "\33[" + code + "m\\33[" + code + "m\033[0m "
            print(colors)
            x = x+5
