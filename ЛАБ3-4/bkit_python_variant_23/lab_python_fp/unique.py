class Unique:
    def __init__(self, items, **kwargs):
        self._items = iter(items)
        self._ignore_case = kwargs.get("ignore_case", False)
        self._seen = set()

    def __iter__(self):
        return self

    def __next__(self):
        for item in self._items:
            key = item
            if self._ignore_case and isinstance(item, str):
                key = item.casefold()
            if key not in self._seen:
                self._seen.add(key)
                return item
        raise StopIteration


if __name__ == "__main__":
    words = ["Б", "б", "А", "а", "Б"]
    print("С учетом регистра:", list(Unique(words)))
    print("Без учета регистра:", list(Unique(words, ignore_case=True)))
    numbers = (n for n in [3, 3, 1, 2, 1])
    print("Из генератора:", list(Unique(numbers)))
