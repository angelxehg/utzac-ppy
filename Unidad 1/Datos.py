from Paleta import Paleta

print("Ingresa tus datos personales")
nombre = input("Nombre: ")
apellido = input("Apellido: ")
edad = int(input("Edad: "))
fecha = input("Fecha de nacimiento: ")
ciudad = input("Ciudad de origen: ")

print("\nDatos obtenidos:")
print("Nombre completo:", Paleta.AMARILLO, nombre, apellido, Paleta.CIERRE)
print("Fecha de nacimiento:", Paleta.AMARILLO, fecha, Paleta.CIERRE)
print("Edad:", Paleta.AMARILLO, edad, Paleta.CIERRE)
print("Ciudad de origen:", Paleta.AMARILLO, ciudad, Paleta.CIERRE)
