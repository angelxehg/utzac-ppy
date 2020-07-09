class PizzaError(Exception):
    def __init__(self, pizza, mensaje):
        Exception.__init__(mensaje)
        self.pizza = pizza


class DemasiadoQuesoError(PizzaError):
    def __init__(self, pizza, queso, mensaje):
        PizzaError._init__(self, pizza, mensaje)
        self.queso = queso
