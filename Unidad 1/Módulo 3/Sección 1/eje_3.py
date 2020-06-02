ingreso = float(input("Ingrese el ingreso anual:"))

if ingreso < 85528:
    impuesto = (ingreso * 0.18) - 556.2
else:
    excendente = ingreso - 85528
    impuesto = 14839.2 + (excendente * 0.32)

if impuesto < 0:
    impuesto = 0

impuesto = round(impuesto, 0)
print("El impuesto es: ", impuesto, "pesos")
