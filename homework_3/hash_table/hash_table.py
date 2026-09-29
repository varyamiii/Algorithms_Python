from typing import Any, List


class HashTable:
    """Хеш-таблица с разрешением коллизий методом цепочек."""

    def __init__(
        self, initial_capacity: int = 8, max_load_factor: float = 0.75
    ) -> None:
        if initial_capacity <= 0:
            raise ValueError("Размер таблицы должен быть положительным")
        if not 0 < max_load_factor <= 1:
            raise ValueError("Коэффициент заполнения должен быть от 0 до 1")

        self._buckets: List[List[List[Any]]] = [
            [] for _ in range(initial_capacity)
        ]
        self._size = 0
        self._max_load_factor = max_load_factor

    def _bucket_index(self, key: Any) -> int:
        return hash(key) % len(self._buckets)

    def _find_entry(self, key: Any) -> List[Any] | None:
        bucket = self._buckets[self._bucket_index(key)]
        for entry in bucket:
            if entry[0] == key:
                return entry
        return None

    def _resize(self, new_capacity: int) -> None:
        old_buckets = self._buckets
        self._buckets = [[] for _ in range(new_capacity)]

        for bucket in old_buckets:
            for entry in bucket:
                new_bucket_index = self._bucket_index(entry[0])
                self._buckets[new_bucket_index].append(entry)

    def insert(self, key: Any, value: Any) -> None:
        """Добавляет новую пару или заменяет значение существующего ключа."""
        existing_entry = self._find_entry(key)
        if existing_entry is not None:
            existing_entry[1] = value
            return

        while (self._size + 1) / len(self._buckets) > self._max_load_factor:
            self._resize(len(self._buckets) * 2)

        bucket = self._buckets[self._bucket_index(key)]
        bucket.append([key, value])
        self._size += 1

    def search(self, key: Any) -> Any:
        """Возвращает значение ключа или возбуждает KeyError."""
        entry = self._find_entry(key)
        if entry is None:
            raise KeyError(key)
        return entry[1]

    def delete(self, key: Any) -> Any:
        """Удаляет пару и возвращает хранившееся значение."""
        bucket = self._buckets[self._bucket_index(key)]
        for entry_index, entry in enumerate(bucket):
            if entry[0] == key:
                removed_entry = bucket.pop(entry_index)
                self._size -= 1
                return removed_entry[1]
        raise KeyError(key)

    def clear(self) -> None:
        """Удаляет все пары, сохраняя текущую вместимость таблицы."""
        self._buckets = [[] for _ in range(len(self._buckets))]
        self._size = 0

    def keys(self) -> List[Any]:
        return [entry[0] for bucket in self._buckets for entry in bucket]

    def values(self) -> List[Any]:
        return [entry[1] for bucket in self._buckets for entry in bucket]

    def items(self) -> List[List[Any]]:
        return [[entry[0], entry[1]] for bucket in self._buckets for entry in bucket]

    @property
    def capacity(self) -> int:
        return len(self._buckets)

    @property
    def load_factor(self) -> float:
        return self._size / len(self._buckets)

    def __len__(self) -> int:
        return self._size

    def __contains__(self, key: Any) -> bool:
        return self._find_entry(key) is not None

    def __getitem__(self, key: Any) -> Any:
        return self.search(key)

    def __setitem__(self, key: Any, value: Any) -> None:
        self.insert(key, value)

    def __delitem__(self, key: Any) -> None:
        self.delete(key)


def main() -> None:
    table = HashTable()
    print("Хеш-таблица")
    print("1 — вставить или обновить пару")
    print("2 — найти значение по ключу")
    print("3 — удалить пару")
    print("4 — показать все пары")
    print("0 — завершить работу")

    while True:
        command = input("\nВведите номер операции: ").strip()

        if command == "0":
            print("Работа завершена.")
            break

        if command == "1":
            key = input("Введите ключ: ")
            value = input("Введите значение: ")
            table.insert(key, value)
            print("Пара сохранена.")
        elif command == "2":
            key = input("Введите ключ: ")
            try:
                print("Найденное значение:", table.search(key))
            except KeyError:
                print("Ключ не найден.")
        elif command == "3":
            key = input("Введите ключ: ")
            try:
                removed_value = table.delete(key)
                print("Удалено значение:", removed_value)
            except KeyError:
                print("Ключ не найден.")
        elif command == "4":
            print("Все пары:", table.items())
        else:
            print("Неизвестная операция. Введите число от 0 до 4.")


if __name__ == "__main__":
    main()
