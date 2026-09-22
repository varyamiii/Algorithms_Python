import unittest

from homework_2.validate.validate import validate_stack_sequences


class ValidateStackSequencesTests(unittest.TestCase):
    def test_example_true(self) -> None:
        self.assertTrue(validate_stack_sequences([1, 2, 3, 4, 5], [1, 3, 5, 4, 2]))

    def test_example_false(self) -> None:
        self.assertFalse(validate_stack_sequences([1, 2, 3], [3, 1, 2]))

    def test_single_element(self) -> None:
        self.assertTrue(validate_stack_sequences([1], [1]))

    def test_same_order(self) -> None:
        self.assertTrue(validate_stack_sequences([1, 2, 3], [1, 2, 3]))

    def test_full_reverse(self) -> None:
        self.assertTrue(validate_stack_sequences([1, 2, 3, 4], [4, 3, 2, 1]))

    def test_impossible_permutation(self) -> None:
        self.assertFalse(validate_stack_sequences([1, 2, 3, 4, 5], [4, 3, 5, 1, 2]))

    def test_large_sequence(self) -> None:
        pushed = list(range(1, 100_001))
        popped = list(range(100_000, 0, -1))
        self.assertTrue(validate_stack_sequences(pushed, popped))


if __name__ == "__main__":
    unittest.main()
