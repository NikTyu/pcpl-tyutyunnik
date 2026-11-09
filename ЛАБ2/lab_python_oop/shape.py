from abc import ABC, abstractmethod
from math import isfinite


class Shape(ABC):
    NAME = "Геометрическая фигура"

    @classmethod
    def get_name(cls):
        return cls.NAME

    @staticmethod
    def _positive(value):
        if not isfinite(value) or value <= 0:
            raise ValueError("Размер должен быть положительным и конечным")
        return value

    @abstractmethod
    def area(self):
        """Вычислить площадь фигуры."""
        raise NotImplementedError
