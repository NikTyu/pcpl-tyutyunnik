import math
import unittest

from .circle import Circle
from .color import Color
from .rectangle import Rectangle
from .shape import Shape
from .square import Square


class ShapeTests(unittest.TestCase):
    def test_abstract_class(self):
        with self.assertRaises(TypeError):
            Shape()

    def test_rectangle_area(self):
        self.assertEqual(Rectangle(3, 7, "синий").area(), 21)

    def test_circle_area(self):
        self.assertAlmostEqual(Circle(2, "зеленый").area(),
                               4 * math.pi)

    def test_square_inheritance(self):
        square = Square(5, "красный")
        self.assertIsInstance(square, Rectangle)
        self.assertEqual((square.width, square.height), (5, 5))
        self.assertEqual(square.area(), 25)

    def test_class_names(self):
        for cls, name in ((Rectangle, "Прямоугольник"),
                          (Circle, "Круг"), (Square, "Квадрат")):
            with self.subTest(cls=cls):
                self.assertEqual(cls.get_name(), name)

    def test_color_property(self):
        color = Color("синий")
        color.value = " зеленый "
        self.assertEqual(color.value, "зеленый")

    def test_color_composition(self):
        first = Rectangle(2, 3, "синий")
        second = Rectangle(2, 3, "синий")
        self.assertIsInstance(first.color, Color)
        first.color.value = "красный"
        self.assertEqual(second.color.value, "синий")

    def test_invalid_color(self):
        for value in ("", "  ", None, 23):
            with self.subTest(value=value):
                with self.assertRaises(ValueError):
                    Color(value)

    def test_invalid_dimensions(self):
        for value in (0, -1, math.inf, math.nan):
            for build in (lambda: Rectangle(value, 1, "синий"),
                          lambda: Rectangle(1, value, "синий"),
                          lambda: Circle(value, "зеленый"),
                          lambda: Square(value, "красный")):
                with self.subTest(value=value, build=build):
                    with self.assertRaises(ValueError):
                        build()

    def test_variant_23_and_repr(self):
        cases = (
            (Rectangle(23, 23, "синий"), 529,
             "Прямоугольник: ширина=23, высота=23, "
             "цвет=синий, площадь=529.00"),
            (Circle(23, "зеленый"), 1661.9025137490005,
             "Круг: радиус=23, цвет=зеленый, площадь=1661.90"),
            (Square(23, "красный"), 529,
             "Квадрат: сторона=23, цвет=красный, площадь=529.00"),
        )
        for figure, expected_area, expected_repr in cases:
            with self.subTest(figure=figure):
                self.assertAlmostEqual(figure.area(), expected_area)
                self.assertEqual(repr(figure), expected_repr)


if __name__ == "__main__":
    unittest.main()
