from helpers.Color import Color

print("Ingresa tus datos personales")
nombre = input("Nombre: ")
apellido = input("Apellido: ")
edad = int(input("Edad: "))
fecha = input("Fecha de nacimiento: ")
ciudad = input("Ciudad de origen: ")

print("\nDatos obtenidos:")
print("Nombre completo:", Color.YELLOW, nombre, apellido, Color.DEFAULT)
print("Fecha de nacimiento:", Color.YELLOW, fecha, Color.DEFAULT)
print("Edad:", Color.YELLOW, edad, Color.DEFAULT)
print("Ciudad de origen:", Color.YELLOW, ciudad, Color.DEFAULT)
