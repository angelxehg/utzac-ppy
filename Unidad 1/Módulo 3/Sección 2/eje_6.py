bloques = int(input("Ingrese el número de bloques:"))
altura = 0

while(bloques > altura + 1):
	altura += 1
	bloques -= altura

print("La altura de la pirámide:", altura)
