from datetime import date
from helpers.Color import Color

y = int(input("¿En qué año naciste? (YYYY): "))
m = int(input("¿En qué mes naciste? (MM): "))
d = int(input("¿En qué dia naciste? (DD): "))

td = date.today()

if td.month > m:
    print("Edad:", Color.BLUE, td.year - y, Color.DEFAULT)
elif td.month == m and td.day >= d:
    print("Edad:", Color.BLUE, td.year - y, Color.DEFAULT)
else:
    print("Edad:", Color.BLUE, td.year - y - 1, Color.DEFAULT)
