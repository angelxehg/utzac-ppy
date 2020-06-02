numeroSecreto = 777

print(
    """
+==================================+
| Bienvenido a mi juego, muggle!   |
| Introduce un número entero       |
| y adivina qué número he          |
| elegido para ti.                 |
| Entonces,                        |
| ¿Cuál es el número secreto?      |
+==================================+
""")

entrada = int(input("Número secreto: "))

while (entrada != numeroSecreto):
    print("¡Ja, ja! ¡Estás atrapado en mi ciclo!")
    entrada = int(input("Número secreto: "))

print("¡Bien hecho, muggle! Eres libre ahora")
