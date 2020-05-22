# Obtener calificaciones
mat = int(input("Introduce la calificación de Matemáticas: "))
fis = int(input("Introduce la calificación de Física: "))
qui = int(input("Introduce la calificación de Química: "))
comp = int(input("Introduce la calificación de Computación: "))
elc = int(input("Introduce la calificación de Electricidad: "))

# Obtener promedio
suma = int(mat+fis+qui+comp+elc)
prom = float(suma/5)

# Mostrar promedio
print("El promedio es ", prom)
