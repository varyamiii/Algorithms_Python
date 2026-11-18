import random
import unittest

from homework_6.k_th.k_th import find_kth_largest


class KthTests(unittest.TestCase):
    def test_examples(self) -> None:
        self.assertEqual(find_kth_largest([3, 2, 1, 5, 6, 4], 2), 5)
        self.assertEqual(find_kth_largest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4), 4)

    def test_boundaries_and_duplicates(self) -> None:
        self.assertEqual(find_kth_largest([8], 1), 8)
        self.assertEqual(find_kth_largest([5, 5, 5], 2), 5)
        self.assertEqual(find_kth_largest([-4, -1, -8, -1], 1), -1)
        self.assertEqual(find_kth_largest([-4, -1, -8, -1], 4), -8)
        self.assertEqual(find_kth_largest([9, 9, 2, 1], 2), 9)

    def test_invalid_k(self) -> None:
        for values, k in (([], 1), ([1], 0), ([1], 2), ([1], -1)):
            with self.subTest(values=values, k=k):
                with self.assertRaises(ValueError):
                    find_kth_largest(values, k)

    def test_all_ranks_and_input_preserved(self) -> None:
        randomizer = random.Random(123)
        for size in (2, 7, 31, 100):
            values = [randomizer.randrange(-10, 11) for _ in range(size)]
            original = values.copy()
            expected = sorted(values, reverse=True)
            for k in range(1, size + 1):
                self.assertEqual(find_kth_largest(values, k), expected[k - 1])
            self.assertEqual(values, original)


if __name__ == "__main__":
    unittest.main()
