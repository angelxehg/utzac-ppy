from helpers.Palette import Palette

print("Ingresa tus datos personales")
nombre = input("Nombre: ")
apellido = input("Apellido: ")
edad = int(input("Edad: "))
fecha = input("Fecha de nacimiento: ")
ciudad = input("Ciudad de origen: ")

print("\nDatos obtenidos:")
print("Nombre completo:", Palette.AMARILLO, nombre, apellido, Palette.CIERRE)
print("Fecha de nacimiento:", Palette.AMARILLO, fecha, Palette.CIERRE)
print("Edad:", Palette.AMARILLO, edad, Palette.CIERRE)
print("Ciudad de origen:", Palette.AMARILLO, ciudad, Palette.CIERRE)
