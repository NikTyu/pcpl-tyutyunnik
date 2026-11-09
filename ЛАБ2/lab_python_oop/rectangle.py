from .color import Color
from .shape import Shape


class Rectangle(Shape):
    NAME = "Прямоугольник"

    def __init__(self, width, height, color):
        self.width = self._positive(width)
        self.height = self._positive(height)
        self.color = Color(color)

    def area(self):
        return self.width * self.height

    def __repr__(self):
        return (
            "{}: ширина={:g}, высота={:g}, "
            "цвет={}, площадь={:.2f}"
        ).format(self.get_name(), self.width, self.height,
                 self.color.value, self.area())
