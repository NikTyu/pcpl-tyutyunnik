from colorama import Fore, init

from lab_python_oop.circle import Circle
from lab_python_oop.rectangle import Rectangle
from lab_python_oop.square import Square


N = 23


def main():
    init(autoreset=True)
    print("Вариант: {}".format(N))
    figures = (
        (Rectangle(N, N, "синий"), Fore.BLUE),
        (Circle(N, "зеленый"), Fore.GREEN),
        (Square(N, "красный"), Fore.RED),
    )
    for figure, console_color in figures:
        print(console_color + repr(figure))
    print("Внешний пакет: colorama; вызван init(autoreset=True).")


if __name__ == "__main__":
    main()
