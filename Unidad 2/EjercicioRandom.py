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
        print("\33[32\\Cara!\33[0m")
    else:
        print("\33[32\\Cruz!\33[0m")


def rps():
    """ Piedra, Papel o Tijera """
    op = {1: "Piedra", 2: "Papel", 3: "Tijera"}
    destroys = {1: 3, 2: 1, 3: 2}
    mach = randrange(1, 3)
    play = int(input("Escoja un número: (1) Piedra, (2) Papel, (3) Tijera, : "))
    if play not in range(1, 4):
        print("Opción invalida!!")
    else:
        print("Jugador:", op[play])
        print("Máquina:", op[mach])
        if mach == play:
            print("No gana nadie")
        elif play == destroys[mach]:
            print("Gana Máquina")
        else:
            print("Gana Usuario")


def lotto():
    """ Lotería """
    print("¡Lotería!")
    player = []
    while len(player) < 4:
        nf = len(player) + 1
        num = int(
            input("Ingrese un número entre 1 y 9: (Recuadro " + str(nf) + ") "))
        if num not in range(1, 10):
            print("Número fuera de rango!")
        else:
            player.append(num)
    print("Sus números son ", player)
    mach = [randrange(1, 9) for i in range(4)]
    print("Los números ganadores son ", mach)
    prize = 1000000
    per = 0.0
    for i in range(len(player)):
        if mach[i] == player[i]:
            per += 0.25
        else:
            break
    print("Ha ganado ", prize * per)


roll()
coin()
rps()
lotto()
