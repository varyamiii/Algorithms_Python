import unittest
from contextlib import redirect_stdout
from io import StringIO
from unittest.mock import patch

from homework_3.hash_table.hash_table import HashTable, main


class CollidingKey:
    """Ключ с постоянным хешем для проверки обработки коллизий."""

    def __init__(self, value: str) -> None:
        self.value = value

    def __hash__(self) -> int:
        return 1

    def __eq__(self, other: object) -> bool:
        return isinstance(other, CollidingKey) and self.value == other.value


class HashTableTests(unittest.TestCase):
    def test_insert_and_search(self) -> None:
        table = HashTable()
        table.insert("name", "Ada")
        table.insert("age", 36)

        self.assertEqual(table.search("name"), "Ada")
        self.assertEqual(table.search("age"), 36)
        self.assertEqual(len(table), 2)

    def test_existing_key_is_updated_without_changing_size(self) -> None:
        table = HashTable()
        table.insert("language", "C")
        table.insert("language", "Python")

        self.assertEqual(table.search("language"), "Python")
        self.assertEqual(len(table), 1)

    def test_collisions_are_stored_in_one_bucket(self) -> None:
        table = HashTable(initial_capacity=2)
        first_key = CollidingKey("first")
        second_key = CollidingKey("second")
        table.insert(first_key, 10)
        table.insert(second_key, 20)

        self.assertEqual(table.search(first_key), 10)
        self.assertEqual(table.search(second_key), 20)

    def test_delete_returns_value_and_removes_only_requested_key(self) -> None:
        table = HashTable()
        first_key = CollidingKey("first")
        second_key = CollidingKey("second")
        table.insert(first_key, 10)
        table.insert(second_key, 20)

        self.assertEqual(table.delete(first_key), 10)
        self.assertNotIn(first_key, table)
        self.assertIn(second_key, table)
        self.assertEqual(len(table), 1)

    def test_missing_key_raises_key_error(self) -> None:
        table = HashTable()

        with self.assertRaises(KeyError):
            table.search("missing")
        with self.assertRaises(KeyError):
            table.delete("missing")

    def test_table_grows_and_keeps_all_values(self) -> None:
        table = HashTable(initial_capacity=2, max_load_factor=0.75)
        initial_capacity = table.capacity

        for number in range(100):
            table.insert(number, number * number)

        self.assertGreater(table.capacity, initial_capacity)
        self.assertLessEqual(table.load_factor, 0.75)
        self.assertEqual(len(table), 100)
        for number in range(100):
            self.assertEqual(table.search(number), number * number)

    def test_table_respects_small_load_factor(self) -> None:
        table = HashTable(initial_capacity=1, max_load_factor=0.1)
        table.insert("key", "value")

        self.assertLessEqual(table.load_factor, 0.1)
        self.assertEqual(table.search("key"), "value")

    def test_dictionary_style_operations(self) -> None:
        table = HashTable()
        table["answer"] = 42

        self.assertEqual(table["answer"], 42)
        self.assertIn("answer", table)
        del table["answer"]
        self.assertNotIn("answer", table)

    def test_keys_values_items_and_clear(self) -> None:
        table = HashTable()
        table.insert("a", 1)
        table.insert("b", 2)
        capacity_before_clear = table.capacity

        self.assertCountEqual(table.keys(), ["a", "b"])
        self.assertCountEqual(table.values(), [1, 2])
        self.assertCountEqual(table.items(), [["a", 1], ["b", 2]])

        table.clear()
        self.assertEqual(len(table), 0)
        self.assertEqual(table.capacity, capacity_before_clear)
        self.assertEqual(table.items(), [])

    def test_storage_uses_lists(self) -> None:
        table = HashTable()
        table.insert("key", "value")

        self.assertIsInstance(table._buckets, list)
        for bucket in table._buckets:
            self.assertIsInstance(bucket, list)
            for entry in bucket:
                self.assertIsInstance(entry, list)

    def test_invalid_settings(self) -> None:
        with self.assertRaises(ValueError):
            HashTable(initial_capacity=0)
        with self.assertRaises(ValueError):
            HashTable(max_load_factor=0)
        with self.assertRaises(ValueError):
            HashTable(max_load_factor=1.1)

    @patch(
        "builtins.input",
        side_effect=[
            "1",
            "planet",
            "Mars",
            "2",
            "planet",
            "3",
            "planet",
            "4",
            "0",
        ],
    )
    def test_console_menu_accepts_user_values(self, _mocked_input: object) -> None:
        output = StringIO()

        with redirect_stdout(output):
            main()

        console_output = output.getvalue()
        self.assertIn("Пара сохранена.", console_output)
        self.assertIn("Найденное значение: Mars", console_output)
        self.assertIn("Удалено значение: Mars", console_output)
        self.assertIn("Все пары: []", console_output)
        self.assertIn("Работа завершена.", console_output)


if __name__ == "__main__":
    unittest.main()
