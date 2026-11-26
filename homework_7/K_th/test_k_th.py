import unittest

from homework_7.K_th.k_th import k_th_largest, k_th_largest_heapq


class KthLargestTests(unittest.TestCase):
    def test_typical_boundary_and_duplicate_cases(self) -> None:
        cases = [
            ([3, 2, 1, 5, 6, 4], 2, 5),
            ([3, 2, 3, 1, 2, 4, 5, 5, 6], 4, 4),
            ([7], 1, 7),
            ([4, 4, 4, 4], 3, 4),
            ([-7, -2, -10, 0], 1, 0),
            ([-7, -2, -10, 0], 4, -10),
            ([5, 1, 5, 2], 2, 5),
            (list(range(100)), 73, 27),
        ]
        for method in (k_th_largest, k_th_largest_heapq):
            for nums, k, expected in cases:
                with self.subTest(method=method.__name__, nums=nums, k=k):
                    original = nums.copy()
                    self.assertEqual(method(nums, k), expected)
                    self.assertEqual(nums, original)

    def test_invalid_k(self) -> None:
        for method in (k_th_largest, k_th_largest_heapq):
            for nums, k in (([], 1), ([1], 0), ([1], 2), ([1], -1), ([1], 1.5), ([1], True)):
                with self.subTest(method=method.__name__, nums=nums, k=k):
                    with self.assertRaises(ValueError):
                        method(nums, k)


if __name__ == "__main__":
    unittest.main()
