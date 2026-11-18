import unittest
from contextlib import redirect_stdout
from io import StringIO

from homework_6.compare.compare import (
    measure_time,
    merge_sort_recursive,
    merge_sort_recursive_timed,
    quick_sort_recursive,
    quick_sort_recursive_timed,
)


class CompareTests(unittest.TestCase):
    def test_sort_cases(self) -> None:
        cases = [
            [], [7], [3, 1, 2], [5, 5, 5, 5],
            [-3, 8, 0, -3, 2], list(range(30)), list(range(30, 0, -1)),
            [8, 3, 5, 1, 7, 3],
        ]
        for sort in (merge_sort_recursive, quick_sort_recursive):
            for values in cases:
                with self.subTest(sort=sort.__name__, values=values):
                    original = values.copy()
                    self.assertEqual(sort(values), sorted(values))
                    self.assertEqual(values, original)

    def test_large_ordered_input_does_not_exhaust_stack(self) -> None:
        values = list(range(1200))
        self.assertEqual(quick_sort_recursive(values), values)

    def test_timed_versions_return_sorted_values(self) -> None:
        output = StringIO()
        with redirect_stdout(output):
            self.assertEqual(merge_sort_recursive_timed([3, 1, 2]), [1, 2, 3])
            self.assertEqual(quick_sort_recursive_timed([3, 1, 2]), [1, 2, 3])
        self.assertIn("merge_sort_recursive_timed:", output.getvalue())
        self.assertIn("quick_sort_recursive_timed:", output.getvalue())

    def test_decorator_preserves_metadata_return_and_exception(self) -> None:
        @measure_time
        def add(a: int, b: int) -> int:
            """Сумма."""
            return a + b

        @measure_time
        def fail() -> None:
            raise RuntimeError("ошибка")

        output = StringIO()
        with redirect_stdout(output):
            self.assertEqual(add(2, 3), 5)
            with self.assertRaises(RuntimeError):
                fail()
        self.assertEqual(add.__name__, "add")
        self.assertEqual(add.__doc__, "Сумма.")
        self.assertIn("add:", output.getvalue())
        self.assertIn("fail:", output.getvalue())


if __name__ == "__main__":
    unittest.main()
