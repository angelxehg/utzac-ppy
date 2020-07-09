def potenciasDe2(n):
    potencia = 1
    for i in range(n):
        yield potencia
        potencia *= 2

for v in potenciasDe2(8):
    print(v)
