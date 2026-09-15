import unittest

from homework_1.prime.task_3 import count_primes


class CountPrimesTests(unittest.TestCase):
    def test_regular_limit(self) -> None:
        self.assertEqual(count_primes(20), 8)

    def test_zero(self) -> None:
        self.assertEqual(count_primes(0), 0)

    def test_boundary_two(self) -> None:
        self.assertEqual(count_primes(2), 0)

    def test_first_prime_is_included(self) -> None:
        self.assertEqual(count_primes(3), 1)

    def test_limit_itself_is_not_counted(self) -> None:
        self.assertEqual(count_primes(11), 4)

    def test_larger_limit(self) -> None:
        self.assertEqual(count_primes(100), 25)


if __name__ == "__main__":
    unittest.main()
