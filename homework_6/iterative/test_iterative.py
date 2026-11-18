import random
import unittest

from homework_6.iterative.iterative import merge_sort_iterative, quick_sort_iterative


class IterativeTests(unittest.TestCase):
    def test_typical_and_edge_cases(self) -> None:
        cases = [
            [], [1], [2, 1], [4, 1, 3, 2], [0, 0, 0],
            [-5, 2, -1, 2, 0], list(range(100)), list(range(100, 0, -1)),
        ]
        for sort in (merge_sort_iterative, quick_sort_iterative):
            for values in cases:
                with self.subTest(sort=sort.__name__, values=values):
                    original = values.copy()
                    self.assertEqual(sort(values), sorted(values))
                    self.assertEqual(values, original)

    def test_deterministic_random_cases(self) -> None:
        randomizer = random.Random(42)
        for size in (3, 17, 64, 257):
            values = [randomizer.randrange(-20, 21) for _ in range(size)]
            self.assertEqual(merge_sort_iterative(values), sorted(values))
            self.assertEqual(quick_sort_iterative(values), sorted(values))

    def test_large_sorted_input(self) -> None:
        values = list(range(1500))
        self.assertEqual(quick_sort_iterative(values), values)


if __name__ == "__main__":
    unittest.main()
