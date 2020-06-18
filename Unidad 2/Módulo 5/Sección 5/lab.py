def readint(prompt, min, max):
    while True:
        try:
            num = int(input(prompt))
        except:
            print("Error: entrada incorrecta")
            continue
        try:
            assert num >= min
            assert num <= max
            return num
        except:
            print(
                "Error: el valor no está dentro del rango permitido (" + str(min) + ", " + str(max) + ")")
            continue


v = readint("Ingresa un numero de -10 a 10: ", -10, 10)

print("El numero es:", v)
