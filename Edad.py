from datetime import date

y = int(input("¿En qué año naciste? (YYYY): "))
m = int(input("¿En qué mes naciste? (MM): "))
d = int(input("¿En qué dia naciste? (DD): "))

td = date.today()

if td.month > m:
    print("Edad:", td.year - y)
elif td.month == m and td.day >= d:
    print("Edad:", td.year - y)
else:
    print("Edad:", td.year - y - 1)
