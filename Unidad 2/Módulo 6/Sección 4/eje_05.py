class conClase:
    varia = 1
    def __init__(self):
        self.var = 2

    def metodo(self):
        pass

    def __oculto(self):
        pass

obj = conClase()

print(obj.__dict__)
print(conClase.__dict__)