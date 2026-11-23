import argparse
import json
import re
from pathlib import Path

if __package__:
    from .cm_timer import cm_timer_1
    from .field import field
    from .gen_random import gen_random
    from .print_result import print_result
    from .unique import Unique
else:
    from cm_timer import cm_timer_1
    from field import field
    from gen_random import gen_random
    from print_result import print_result
    from unique import Unique


TITLE_KEYS = ("job-name", "name", "title")
PROGRAMMER = re.compile(r"^программист\b", re.IGNORECASE)


def titles(data):
    for vacancy in data:
        for title in field((vacancy,), *TITLE_KEYS):
            for key in TITLE_KEYS:
                value = title.get(key)
                if isinstance(value, str) and value.strip():
                    yield value.strip()
                    break


@print_result
def f1(arg):
    return sorted(Unique(titles(arg), ignore_case=True), key=str.casefold)


@print_result
def f2(arg):
    return list(filter(PROGRAMMER.match, arg))


@print_result
def f3(arg):
    return list(map(lambda job: f"{job} с опытом Python", arg))


@print_result
def f4(arg):
    salaries = gen_random(len(arg), 100_000, 200_000)
    return [f"{job}, зарплата {salary} руб."
            for job, salary in zip(arg, salaries)]


def main():
    parser = argparse.ArgumentParser(description="Обработка вакансий")
    demo = Path(__file__).resolve().parent.parent / "data_demo.json"
    parser.add_argument("path", type=Path, nargs="?", default=demo)
    args = parser.parse_args()
    try:
        with args.path.open(encoding="utf-8-sig") as source:
            data = json.load(source)
        if not isinstance(data, list) or any(
            not isinstance(item, dict) for item in data
        ):
            raise ValueError("Ожидается JSON-массив объектов")
    except (OSError, ValueError) as exc:
        parser.error(str(exc))
    with cm_timer_1():
        f4(f3(f2(f1(data))))


if __name__ == "__main__":
    main()
