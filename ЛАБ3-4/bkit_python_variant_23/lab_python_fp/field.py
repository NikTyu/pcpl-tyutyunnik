def field(items, *args):
    if not args:
        raise ValueError("Укажите хотя бы один ключ")

    for item in items:
        if len(args) == 1:
            value = item.get(args[0])
            if value is not None:
                yield value
        else:
            selected = {key: item[key] for key in args
                        if item.get(key) is not None}
            if selected:
                yield selected


if __name__ == "__main__":
    goods = [
        {"title": "Ковер", "price": 2000},
        {"title": "Диван", "price": None},
        {"title": None, "price": 0},
        {"color": "green"},
    ]
    print("Одно поле:", list(field(goods, "title")))
    print("Несколько полей:")
    for item in field(goods, "title", "price"):
        print(item)
