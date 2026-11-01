import sys
import math
from functools import reduce

MSG_BAD_ARG = 'Некорректное значение в командной строке: "{}"'
MSG_BAD_INPUT = 'Некорректное значение: "{}". Повторите ввод.'


def parse_coef(coef_str):
    try:
        coef = float(coef_str)
    except ValueError:
        return None
    match coef:
        case x if math.isfinite(x):
            return x
        case _:
            return None


def ask_coef(prompt):
    coef_str = input(prompt)
    match parse_coef(coef_str):
        case None:
            print(MSG_BAD_INPUT.format(coef_str))
            return ask_coef(prompt)
        case coef:
            return coef


def get_coef(argv, index, prompt):
    match argv[index:index + 1]:
        case []:
            return ask_coef(prompt)
        case [coef_str]:
            match parse_coef(coef_str):
                case None:
                    print(MSG_BAD_ARG.format(coef_str))
                    return ask_coef(prompt)
                case coef:
                    return coef


def discriminant(a, b, c):
    return b * b - 4 * a * c


def x_roots(y):
    match y:
        case 0:
            return (0.0,)
        case y if y > 0:
            return (-math.sqrt(y), math.sqrt(y))
        case _:
            return ()


def y_roots(a, b, d):
    match d:
        case 0:
            return (-b / (2.0 * a),)
        case d if d > 0:
            return ((-b + math.sqrt(d)) / (2.0 * a),
                    (-b - math.sqrt(d)) / (2.0 * a))
        case _:
            return ()


def all_x_roots(ys):
    roots = reduce(lambda acc, y: acc | set(x_roots(y)), ys, set())
    return tuple(sorted(roots))


def solve(a, b, c):
    match (a, b, c):
        case (0, 0, 0):
            return ('identity', None, ())
        case (0, 0, _):
            return ('contradiction', None, ())
        case (0, _, _):
            return ('degenerate', None, all_x_roots((-c / b,)))
        case _:
            d = discriminant(a, b, c)
            return ('biquadratic', d, all_x_roots(y_roots(a, b, d)))


fmt = lambda x: '{:.6g}'.format(x)

sign = lambda x: '-' if x < 0 else '+'

equation_to_str = lambda a, b, c: '{}*x^4 {} {}*x^2 {} {} = 0'.format(
    fmt(a), sign(b), fmt(abs(b)), sign(c), fmt(abs(c)))

ROOT_WORDS = {2: 'Два корня', 3: 'Три корня', 4: 'Четыре корня'}


def describe_case(kind, d):
    match (kind, d):
        case ('identity', _):
            return 'Корнем является любое действительное число'
        case ('contradiction', _):
            return 'Уравнение не имеет решений'
        case ('degenerate', _):
            return 'A = 0: уравнение вырождается в B*x^2 + C = 0'
        case ('biquadratic', 0):
            return ('Дискриминант D = 0\n'
                    'D = 0: вспомогательное уравнение имеет один корень')
        case ('biquadratic', d) if d > 0:
            return ('Дискриминант D = {}\n'
                    'D > 0: вспомогательное уравнение имеет два корня'
                    ).format(fmt(d))
        case ('biquadratic', d):
            return ('Дискриминант D = {}\nD < 0: вспомогательное уравнение '
                    'не имеет действительных корней').format(fmt(d))


def describe_roots(kind, roots):
    match (kind, roots):
        case ('identity' | 'contradiction', _):
            return None
        case (_, ()):
            return 'Действительных корней нет'
        case (_, (x,)):
            return 'Один корень: {}'.format(fmt(x))
        case (_, roots):
            return '{}: {}'.format(ROOT_WORDS[len(roots)],
                                   ', '.join(map(fmt, roots)))


def main():
    a, b, c = map(lambda arg: get_coef(sys.argv, *arg),
                  ((1, 'Введите коэффициент A: '),
                   (2, 'Введите коэффициент B: '),
                   (3, 'Введите коэффициент C: ')))
    kind, d, roots = solve(a, b, c)
    lines = ('Уравнение: ' + equation_to_str(a, b, c),
             describe_case(kind, d),
             describe_roots(kind, roots))
    print('\n'.join(filter(None, lines)))


if __name__ == "__main__":
    main()
