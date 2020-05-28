from Paleta import Paleta

# Obtener calificaciones
mat = int(input("Introduce la calificación de" +
                Paleta.AZUL + " Matemáticas: " + Paleta.CIERRE))
fis = int(input("Introduce la calificación de" +
                Paleta.AZUL + " Física: " + Paleta.CIERRE))
qui = int(input("Introduce la calificación de" +
                Paleta.AZUL + " Química: " + Paleta.CIERRE))
comp = int(input("Introduce la calificación de" +
                 Paleta.AZUL + " Computación: " + Paleta.CIERRE))
elc = int(input("Introduce la calificación de" +
                Paleta.AZUL + " Electricidad: " + Paleta.CIERRE))

# Obtener promedio
suma = int(mat+fis+qui+comp+elc)
prom = float(suma/5)

if (prom >= 9):
    aprobado = Paleta.VERDE
elif (prom >= 8):
    aprobado = Paleta.AMARILLO
else:
    aprobado = Paleta.ROJO

# Mostrar promedio
print("El promedio es:", aprobado, prom, Paleta.CIERRE)
