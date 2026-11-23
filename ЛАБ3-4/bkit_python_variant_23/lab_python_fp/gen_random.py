from random import randint


def gen_random(num_count, begin, end):
    for _ in range(num_count):
        yield randint(begin, end)


if __name__ == "__main__":
    print("Пять чисел от 1 до 3:", list(gen_random(5, 1, 3)))
    print("Совпадающие границы:", list(gen_random(3, 7, 7)))
    print("Нулевое количество:", list(gen_random(0, 1, 3)))
