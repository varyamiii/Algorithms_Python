import unittest

from homework_1.sum.task_2 import max_even_sum


class MaxEvenSumTests(unittest.TestCase):
    def test_single_odd_number(self) -> None:
        self.assertEqual(max_even_sum([9]), 0)

    def test_all_even_numbers(self) -> None:
        self.assertEqual(max_even_sum([2, 4, 8]), 14)

    def test_odd_total_removes_smallest_odd(self) -> None:
        self.assertEqual(max_even_sum([9, 2, 3, 6, 5]), 22)

    def test_even_total_with_odd_numbers(self) -> None:
        self.assertEqual(max_even_sum([1, 2, 3]), 6)

    def test_empty_array(self) -> None:
        self.assertEqual(max_even_sum([]), 0)


if __name__ == "__main__":
    unittest.main()
