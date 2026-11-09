import math

from .color import Color
from .shape import Shape


class Circle(Shape):
    NAME = "Круг"

    def __init__(self, radius, color):
        self.radius = self._positive(radius)
        self.color = Color(color)

    def area(self):
        return math.pi * self.radius ** 2

    def __repr__(self):
        return "{}: радиус={:g}, цвет={}, площадь={:.2f}".format(
            self.get_name(), self.radius, self.color.value,
            self.area())
