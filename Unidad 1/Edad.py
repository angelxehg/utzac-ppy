from datetime import date
from Paleta import Paleta

y = int(input("¿En qué año naciste? (YYYY): "))
m = int(input("¿En qué mes naciste? (MM): "))
d = int(input("¿En qué dia naciste? (DD): "))

td = date.today()

if td.month > m:
    print("Edad:", Paleta.AZUL, td.year - y, Paleta.CIERRE)
elif td.month == m and td.day >= d:
    print("Edad:", Paleta.AZUL, td.year - y, Paleta.CIERRE)
else:
    print("Edad:", Paleta.AZUL, td.year - y - 1, Paleta.CIERRE)
