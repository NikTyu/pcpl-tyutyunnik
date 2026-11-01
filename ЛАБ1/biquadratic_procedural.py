import sys
import math

MSG_BAD_ARG = 'Некорректное значение в командной строке: "{}"'
MSG_BAD_INPUT = 'Некорректное значение: "{}". Повторите ввод.'


def parse_coef(coef_str):
    try:
        coef = float(coef_str)
    except ValueError:
        return None
    if not math.isfinite(coef):
        return None
    return coef


def get_coef(index, prompt):
    if index < len(sys.argv):
        coef = parse_coef(sys.argv[index])
        if coef is not None:
            return coef
        print(MSG_BAD_ARG.format(sys.argv[index]))
    while True:
        coef_str = input(prompt)
        coef = parse_coef(coef_str)
        if coef is not None:
            return coef
        print(MSG_BAD_INPUT.format(coef_str))


def get_discriminant(a, b, c):
    return b * b - 4 * a * c


def get_square_roots(y):
    if y > 0.0:
        sq_y = math.sqrt(y)
        return [-sq_y, sq_y]
    if y == 0.0:
        return [0.0]
    return []


def get_roots(a, b, c):
    y_list = []
    if a == 0.0:
        if b != 0.0:
            y_list.append(-c / b)
    else:
        d = get_discriminant(a, b, c)
        if d == 0.0:
            y_list.append(-b / (2.0 * a))
        elif d > 0.0:
            sq_d = math.sqrt(d)
            y_list.append((-b + sq_d) / (2.0 * a))
            y_list.append((-b - sq_d) / (2.0 * a))
    result = []
    for y in y_list:
        result.extend(get_square_roots(y))
    return sorted(set(result))


def format_number(x):
    return '{:.6g}'.format(x)


def equation_to_str(a, b, c):
    sign = lambda x: '-' if x < 0 else '+'
    return '{}*x^4 {} {}*x^2 {} {} = 0'.format(
        format_number(a), sign(b), format_number(abs(b)),
        sign(c), format_number(abs(c)))

def print_roots(roots):
    len_roots = len(roots)
    if len_roots == 0:
        print('Действительных корней нет')
    elif len_roots == 1:
        print('Один корень: {}'.format(format_number(roots[0])))
    else:
        words = {2: 'Два корня', 3: 'Три корня', 4: 'Четыре корня'}
        print('{}: {}'.format(words[len_roots],
                              ', '.join(format_number(r) for r in roots)))


def main():
    a = get_coef(1, 'Введите коэффициент A: ')
    b = get_coef(2, 'Введите коэффициент B: ')
    c = get_coef(3, 'Введите коэффициент C: ')
    print('Уравнение:', equation_to_str(a, b, c))

    if a == 0.0 and b == 0.0:
        if c == 0.0:
            print('Корнем является любое действительное число')
        else:
            print('Уравнение не имеет решений')
        return

    if a == 0.0:
        print('A = 0: уравнение вырождается в B*x^2 + C = 0')
    else:
        d = get_discriminant(a, b, c)
        print('Дискриминант D = {}'.format(format_number(d)))
        if d < 0.0:
            print('D < 0: вспомогательное уравнение '
                  'не имеет действительных корней')
        elif d == 0.0:
            print('D = 0: вспомогательное уравнение имеет один корень')
        else:
            print('D > 0: вспомогательное уравнение имеет два корня')

    print_roots(get_roots(a, b, c))


if __name__ == "__main__":
    main()
