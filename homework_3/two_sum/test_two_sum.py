import unittest

from homework_3.two_sum.two_sum import two_sum


class TwoSumTests(unittest.TestCase):
    def test_pair_in_middle(self) -> None:
        self.assertEqual(two_sum([12, 7, 2, 9, 20], 11), (2, 3))

    def test_duplicate_values(self) -> None:
        self.assertEqual(two_sum([6, 1, 6, 2], 12), (0, 2))

    def test_negative_values(self) -> None:
        self.assertEqual(two_sum([-7, 2, 9, 4], -3), (0, 3))

    def test_zero_values(self) -> None:
        self.assertEqual(two_sum([0, 8, 0], 0), (0, 2))

    def test_pair_at_array_edges(self) -> None:
        self.assertEqual(two_sum([6, 1, 2, 3, 14], 20), (0, 4))

    def test_missing_pair_raises_error(self) -> None:
        with self.assertRaises(ValueError):
            two_sum([1, 2, 3], 10)


if __name__ == "__main__":
    unittest.main()
