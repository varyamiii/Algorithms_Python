import unittest

from homework_7.Heapsort.heapsort import heapsort


class HeapsortTests(unittest.TestCase):
    def test_sorting_and_in_place_behavior(self) -> None:
        cases = [
            [], [3], [2, 1], [8, 3, 5, 1, 7, 3],
            [1, 2, 3, 4, 5], [5, 4, 3, 2, 1],
            [0, -2, 7, -2, 10, 0], [4] * 50,
            list(range(200, -1, -1)),
        ]
        for case in cases:
            with self.subTest(case=case):
                values = case.copy()
                self.assertIs(heapsort(values), values)
                self.assertEqual(values, sorted(case))


if __name__ == "__main__":
    unittest.main()
