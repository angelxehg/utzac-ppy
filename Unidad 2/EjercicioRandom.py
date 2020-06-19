from random import randrange


def roll():
    """ Juego Dado """
    x = randrange(1, 6)
    y = randrange(1, 6)
    print("\33[0mJugador 1:\33[33m", x, "\33[0m")
    print("\33[0mJugador 2:\33[33m", y, "\33[0m")
    if x < y:
        print("\33[32mGanó el jugador 1\33[0m")
    elif y < x:
        print("\33[32mGanó el jugador 2\33[0m")
    else:
        print("\33[32mNo ganó nadie\33[0m")


def coin():
    """ Lanzar moneda """
    c = randrange(1, 2)
    if c == 1:
        print("\33[32\Cara!\33[0m")
    else:
        print("\33[32\Cruz!\33[0m")


roll()
coin()
