import sys
import math

MSG_BAD_ARG = 'Некорректное значение в командной строке: "{}"'
MSG_BAD_INPUT = 'Некорректное значение: "{}". Повторите ввод.'


class CoefReader:
    def __init__(self, argv):
        self.argv = argv

    @staticmethod
    def parse(coef_str):
        try:
            coef = float(coef_str)
        except ValueError:
            return None
        if not math.isfinite(coef):
            return None
        return coef

    def read(self, index, prompt):
        if index < len(self.argv):
            coef = self.parse(self.argv[index])
            if coef is not None:
                return coef
            print(MSG_BAD_ARG.format(self.argv[index]))
        while True:
            coef_str = input(prompt)
            coef = self.parse(coef_str)
            if coef is not None:
                return coef
            print(MSG_BAD_INPUT.format(coef_str))


class BiquadraticEquation:
    ROOT_WORDS = {2: 'Два корня', 3: 'Три корня', 4: 'Четыре корня'}

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    @staticmethod
    def fmt(x):
        return '{:.6g}'.format(x)

    def __str__(self):
        sign = lambda x: '-' if x < 0 else '+'
        return '{}*x^4 {} {}*x^2 {} {} = 0'.format(
            self.fmt(self.a), sign(self.b), self.fmt(abs(self.b)),
            sign(self.c), self.fmt(abs(self.c)))

    @property
    def discriminant(self):
        return self.b * self.b - 4 * self.a * self.c

    @property
    def is_identity(self):
        return self.a == 0.0 and self.b == 0.0 and self.c == 0.0

    def _y_roots(self):
        if self.a == 0.0:
            return [-self.c / self.b] if self.b != 0.0 else []
        d = self.discriminant
        if d < 0.0:
            return []
        if d == 0.0:
            return [-self.b / (2.0 * self.a)]
        sq_d = math.sqrt(d)
        return [(-self.b + sq_d) / (2.0 * self.a),
                (-self.b - sq_d) / (2.0 * self.a)]

    @staticmethod
    def _x_roots(y):
        if y > 0.0:
            sq_y = math.sqrt(y)
            return [-sq_y, sq_y]
        if y == 0.0:
            return [0.0]
        return []

    def roots(self):
        result = set()
        for y in self._y_roots():
            result.update(self._x_roots(y))
        return sorted(result)

    def print_solution(self):
        print('Уравнение:', self)
        if self.is_identity:
            print('Корнем является любое действительное число')
            return
        if self.a == 0.0 and self.b == 0.0:
            print('Уравнение не имеет решений')
            return
        if self.a == 0.0:
            print('A = 0: уравнение вырождается в B*x^2 + C = 0')
        else:
            d = self.discriminant
            print('Дискриминант D = {}'.format(self.fmt(d)))
            if d < 0.0:
                print('D < 0: вспомогательное уравнение '
                      'не имеет действительных корней')
            elif d == 0.0:
                print('D = 0: вспомогательное уравнение имеет один корень')
            else:
                print('D > 0: вспомогательное уравнение имеет два корня')

        roots = self.roots()
        if len(roots) == 0:
            print('Действительных корней нет')
        elif len(roots) == 1:
            print('Один корень: {}'.format(self.fmt(roots[0])))
        else:
            print('{}: {}'.format(self.ROOT_WORDS[len(roots)],
                                  ', '.join(self.fmt(r) for r in roots)))


def main():
    reader = CoefReader(sys.argv)
    a = reader.read(1, 'Введите коэффициент A: ')
    b = reader.read(2, 'Введите коэффициент B: ')
    c = reader.read(3, 'Введите коэффициент C: ')
    BiquadraticEquation(a, b, c).print_solution()


if __name__ == "__main__":
    main()
