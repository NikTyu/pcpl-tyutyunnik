from .rectangle import Rectangle


class Square(Rectangle):
    NAME = "Квадрат"

    def __init__(self, side, color):
        super().__init__(side, side, color)

    def __repr__(self):
        return "{}: сторона={:g}, цвет={}, площадь={:.2f}".format(
            self.get_name(), self.width, self.color.value,
            self.area())
