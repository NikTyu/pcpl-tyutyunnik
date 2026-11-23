data = [4, -30, 30, 100, -100, 123, 1, 0, -1, -4]


if __name__ == "__main__":
    print("С lambda:", sorted(data, key=lambda x: abs(x), reverse=True))
    print("Без lambda:", sorted(data, key=abs, reverse=True))
