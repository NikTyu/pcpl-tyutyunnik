import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch

from lab_python_fp.cm_timer import cm_timer_1, cm_timer_2
from lab_python_fp.field import field
from lab_python_fp.gen_random import gen_random
from lab_python_fp.print_result import print_result
from lab_python_fp.process_data import f1, f2, f3, f4
from lab_python_fp.sort import data
from lab_python_fp.unique import Unique


class LabTests(unittest.TestCase):
    def test_field_modes(self):
        data = [{"x": False, "y": 0}, {"x": None, "y": 1}, {}, {"x": ""}]
        self.assertEqual(list(field(data, "x")), [False, ""])
        self.assertEqual(
            list(field(data, "x", "y")),
            [{"x": False, "y": 0}, {"y": 1}, {"x": ""}],
        )
        with self.assertRaises(ValueError):
            list(field(data))

    def test_random_generator(self):
        numbers = list(gen_random(50, -3, 3))
        self.assertEqual(len(numbers), 50)
        self.assertTrue(all(-3 <= n <= 3 for n in numbers))
        self.assertEqual(list(gen_random(2, 4, 4)), [4, 4])
        self.assertEqual(list(gen_random(0, 4, 4)), [])

    def test_unique(self):
        words = ["А", "а", "Б", "Б"]
        self.assertEqual(list(Unique(words)), ["А", "а", "Б"])
        iterator = Unique((w for w in words), ignore_case=True)
        self.assertIs(iter(iterator), iterator)
        self.assertEqual(list(iterator), ["А", "Б"])
        with self.assertRaises(StopIteration):
            next(iterator)

    def test_sort_stability(self):
        expected = [123, 100, -100, -30, 30, 4, -4, 1, -1, 0]
        self.assertEqual(sorted(data, key=abs, reverse=True), expected)
        self.assertEqual(sorted(data, key=lambda x: abs(x), reverse=True), expected)

    def test_decorator(self):
        @print_result
        def identity(value, *, suffix=""):
            return value + suffix if isinstance(value, str) else value

        for value, expected in [(42, "42"), (["a", "b"], "a\nb"),
                                ({"a": 1}, "a = 1")]:
            with self.subTest(value=value), redirect_stdout(io.StringIO()) as out:
                self.assertIs(identity(value), value)
            self.assertEqual(out.getvalue(), f"identity\n{expected}\n")
        with redirect_stdout(io.StringIO()):
            self.assertEqual(identity("a", suffix="b"), "ab")
        self.assertEqual(identity.__name__, "identity")

    def test_both_timers_and_exception_propagation(self):
        for timer in (cm_timer_1, cm_timer_2):
            with self.subTest(timer=timer), redirect_stdout(io.StringIO()) as out:
                with timer():
                    pass
                with self.assertRaisesRegex(RuntimeError, "test"):
                    with timer():
                        raise RuntimeError("test")
            self.assertRegex(out.getvalue(), r"^time: \d+\.\d+\ntime: \d+\.\d+\n$")

    def test_pipeline(self):
        titles = [{"job-name": "Программист C#"}, {"name": "ПРОГРАММИСТ C#"},
                  {"title": "программист Java"}, {"name": "Программистка"},
                  {"job-name": "Аналитик"}, {"job-name": None}, {}]
        with redirect_stdout(io.StringIO()):
            self.assertEqual(f1(titles), ["Аналитик", "Программист C#",
                                          "программист Java", "Программистка"])
            with patch("lab_python_fp.gen_random.randint", side_effect=[100_000, 200_000]):
                rows = f4(f3(f2(f1(titles))))
            self.assertEqual(f4([]), [])
        self.assertEqual(rows, [
            "Программист C# с опытом Python, зарплата 100000 руб.",
            "программист Java с опытом Python, зарплата 200000 руб.",
        ])


if __name__ == "__main__":
    unittest.main()
