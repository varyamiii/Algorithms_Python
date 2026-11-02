import unittest
from io import StringIO

from homework_5.permutations.permutations import permutations


class PermutationsTests(unittest.TestCase):
    def test_three_values(self) -> None:
        self.assertEqual(
            permutations([1, 2, 3]),
            [
                [1, 2, 3],
                [1, 3, 2],
                [2, 1, 3],
                [2, 3, 1],
                [3, 1, 2],
                [3, 2, 1],
            ],
        )

    def test_two_values(self) -> None:
        self.assertEqual(permutations([0, 1]), [[0, 1], [1, 0]])

    def test_one_value(self) -> None:
        self.assertEqual(permutations([9]), [[9]])

    def test_empty_input_has_one_empty_permutation(self) -> None:
        self.assertEqual(permutations([]), [[]])

    def test_duplicate_values_produce_unique_permutations(self) -> None:
        self.assertEqual(
            permutations([1, 1, 2]),
            [[1, 1, 2], [1, 2, 1], [2, 1, 1]],
        )

    def test_negative_values_and_input_order(self) -> None:
        self.assertEqual(
            permutations([-1, 2]),
            [[-1, 2], [2, -1]],
        )

    def test_input_is_not_modified(self) -> None:
        numbers = [3, 1, 2]
        original = numbers.copy()

        permutations(numbers)

        self.assertEqual(numbers, original)

    def test_visualization_uses_tracer(self) -> None:
        output = StringIO()

        result = permutations([1, 2], visualize=True, stream=output)

        self.assertEqual(result, [[1, 2], [2, 1]])
        lines = output.getvalue().splitlines()
        self.assertEqual(lines[0], "-> build_permutations((1, 2))")
        self.assertIn("  -> build_permutations((2,))", lines)
        self.assertIn("    <- build_permutations = [[]]", lines)
        self.assertEqual(
            lines[-1],
            "<- build_permutations = [[1, 2], [2, 1]]",
        )


if __name__ == "__main__":
    unittest.main()
