import unittest

from homework_7.Makeheap.makeheap import makeheap, makeheap_n_log_n


class MakeheapTests(unittest.TestCase):
    def test_both_methods_build_valid_heap_and_keep_all_values(self) -> None:
        cases = [
            [], [7], [2, 1], [9, 4, 7, 1, 5, 3],
            [1, 2, 3, 4, 5], [5, 4, 3, 2, 1],
            [3, 3, 1, 3, 1], [-2, 8, 0, -10, 4],
            list(range(100, -1, -1)),
        ]
        for method in (makeheap_n_log_n, makeheap):
            for case in cases:
                with self.subTest(method=method.__name__, case=case):
                    values = case.copy()
                    self.assertIs(method(values), values)
                    self.assertEqual(sorted(values), sorted(case))
                    for child in range(1, len(values)):
                        self.assertLessEqual(values[(child - 1) // 2], values[child])


if __name__ == "__main__":
    unittest.main()
