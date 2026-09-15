import unittest

from homework_1.palindrome.task_1 import is_palindrome


class IsPalindromeTests(unittest.TestCase):
    def test_odd_number_of_digits(self) -> None:
        self.assertTrue(is_palindrome(1234321))

    def test_even_number_of_digits(self) -> None:
        self.assertTrue(is_palindrome(1221))

    def test_non_palindrome(self) -> None:
        self.assertFalse(is_palindrome(42))

    def test_single_digit(self) -> None:
        self.assertTrue(is_palindrome(7))

    def test_number_ending_in_zero(self) -> None:
        self.assertFalse(is_palindrome(10))

    def test_zero(self) -> None:
        self.assertTrue(is_palindrome(0))


if __name__ == "__main__":
    unittest.main()
