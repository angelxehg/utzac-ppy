from datetime import date
from helpers.Palette import Palette

y = int(input("¿En qué año naciste? (YYYY): "))
m = int(input("¿En qué mes naciste? (MM): "))
d = int(input("¿En qué dia naciste? (DD): "))

td = date.today()

if td.month > m:
    print("Edad:", Palette.AZUL, td.year - y, Palette.CIERRE)
elif td.month == m and td.day >= d:
    print("Edad:", Palette.AZUL, td.year - y, Palette.CIERRE)
else:
    print("Edad:", Palette.AZUL, td.year - y - 1, Palette.CIERRE)
