import unittest

from homework_2.merge_lists.merge_lists import (
    build_list,
    merge_with_dummy,
    merge_without_dummy,
    to_python_list,
)


class MergeListsTests(unittest.TestCase):
    def setUp(self) -> None:
        self.merge_functions = (merge_with_dummy, merge_without_dummy)

    def check(self, values1, values2, expected) -> None:
        for merge in self.merge_functions:
            with self.subTest(merge=merge.__name__):
                merged = merge(build_list(values1), build_list(values2))
                self.assertEqual(to_python_list(merged), expected)

    def test_example(self) -> None:
        self.check([1, 2, 4], [1, 3, 4], [1, 1, 2, 3, 4, 4])

    def test_both_empty(self) -> None:
        self.check([], [], [])

    def test_first_empty(self) -> None:
        self.check([], [1, 2, 3], [1, 2, 3])

    def test_second_empty(self) -> None:
        self.check([1, 2, 3], [], [1, 2, 3])

    def test_different_lengths(self) -> None:
        self.check([1, 5, 9], [2, 3, 4, 10, 11], [1, 2, 3, 4, 5, 9, 10, 11])

    def test_duplicates(self) -> None:
        self.check([2, 2, 2], [2, 2], [2, 2, 2, 2, 2])

    def test_disjoint_ranges(self) -> None:
        self.check([1, 2, 3], [4, 5, 6], [1, 2, 3, 4, 5, 6])


if __name__ == "__main__":
    unittest.main()
