from random import randrange


def roll():
    """ Juego Dado """
    print("\n\33[0m¡Lanzamiento Dado!\n")
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
    print("\n\33[0m¡Lanzamiento moneda!\n")
    c = randrange(1, 2)
    if c == 1:
        print("\33[32mCara!\33[0m")
    else:
        print("\33[32mCruz!\33[0m")


def rps():
    """ Piedra, Papel o Tijera """
    print("\n\33[0m¡Piedra, Papel o Tijera!\n")
    op = {1: "Piedra", 2: "Papel", 3: "Tijera"}
    destroys = {1: 3, 2: 1, 3: 2}
    mach = randrange(1, 3)
    play = int(
        input("\33[0mEscoja un número: (1) Piedra, (2) Papel, (3) Tijera, : "))
    if play not in range(1, 4):
        print("\33[31mOpción invalida!!")
    else:
        print("\33[0mJugador:\33[34m", op[play])
        print("\33[0mMáquina:\33[34m", op[mach])
        if mach == play:
            print("\33[31mNo gana nadie")
        elif play == destroys[mach]:
            print("\33[33mGana Máquina")
        else:
            print("\33[32mGana Usuario")


def lotto():
    """ Lotería """
    print("\n\33[0m¡Lotería!\n")
    player = []
    while len(player) < 4:
        nf = len(player) + 1
        num = int(
            input("\33[0mIngrese un número entre 1 y 9: (Recuadro " + str(nf) + ") \33[34m"))
        if num not in range(1, 10):
            print("\33[31mNúmero fuera de rango!")
        else:
            player.append(num)
    print("\33[0mSus números son \33[34m", player)
    mach = [randrange(1, 9) for i in range(4)]
    print("\33[0mLos números ganadores son \33[34m", mach)
    prize = 1000000
    per = 0.0
    for i in range(len(player)):
        if mach[i] == player[i]:
            per += 0.25
        else:
            break
    print("\33[32mHa ganado ", prize * per,
          " (acertó ", per * 100, "% al inicio\33[0m")


roll()
coin()
rps()
lotto()
