from math import pi, sqrt, pow


class Figure:

    @property
    def area(self):
        return 0.0

    @property
    def perimeter(self):
        return 0.0

    def __str__(self):
        return '(' + self.__class__.__name__ + ') | Area: ' + str(self.area) + ' | Perimeter: ' + str(self.perimeter)


class Circle(Figure):

    def __init__(self, radius=1.0):
        self.radius = radius

    @property
    def area(self):
        return pi * self.radius * self.radius

    @property
    def perimeter(self):
        return pi * self.radius * 2


class Rectangle(Figure):

    def __init__(self, height=1.0, width=1.0):
        self.height = height
        self.width = width

    @property
    def area(self):
        return self.height * self.width

    @property
    def perimeter(self):
        return (self.height + self.width) * 2


class RightTriangle(Rectangle):

    def __init__(self, height=1.0, width=1.0):
        super(RightTriangle, self).__init__(height, width)

    @property
    def area(self):
        return self.height * self.width / 2

    @property
    def hypotenuse(self):
        return sqrt(pow(self.height, 2) + pow(self.width, 2))

    @property
    def perimeter(self):
        return self.height + self.width + self.hypotenuse


figures = [
    Figure(),
    Circle(5.0),
    Rectangle(5.0, 6.0),
    RightTriangle(5.0, 6.0)
]

for figure in figures:
    print(figure)
