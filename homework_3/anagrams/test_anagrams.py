import unittest
from typing import List

from homework_3.anagrams.anagrams import group_anagrams


def normalize(groups: List[List[str]]) -> List[List[str]]:
    """Упорядочивает результат, чтобы сравнение не зависело от порядка групп."""
    return sorted(
        (sorted(group) for group in groups),
        key=lambda group: (len(group), group),
    )


class GroupAnagramsTests(unittest.TestCase):
    def test_several_groups(self) -> None:
        words = ["arc", "car", "elbow", "below", "state", "taste", "cat"]
        expected = [["arc", "car"], ["elbow", "below"], ["state", "taste"], ["cat"]]
        self.assertEqual(normalize(group_anagrams(words)), normalize(expected))

    def test_empty_input(self) -> None:
        self.assertEqual(group_anagrams([]), [])

    def test_single_word(self) -> None:
        self.assertEqual(group_anagrams(["python"]), [["python"]])

    def test_empty_strings(self) -> None:
        words = ["", "a", ""]
        expected = [["", ""], ["a"]]
        self.assertEqual(normalize(group_anagrams(words)), normalize(expected))

    def test_repeated_letters(self) -> None:
        words = ["aab", "aba", "baa", "abb"]
        expected = [["aab", "aba", "baa"], ["abb"]]
        self.assertEqual(normalize(group_anagrams(words)), normalize(expected))

    def test_case_is_significant(self) -> None:
        words = ["Listen", "silent", "enlist"]
        self.assertEqual(group_anagrams(words), [["Listen"], ["silent", "enlist"]])


if __name__ == "__main__":
    unittest.main()
