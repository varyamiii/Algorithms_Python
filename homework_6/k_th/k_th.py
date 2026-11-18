"""Quickselect для поиска k-го по величине элемента с учётом повторов."""


def find_kth_largest(nums: list[int], k: int) -> int:
    """Возвращает k-й элемент по убыванию, не изменяя входной список.

    Повторяющиеся значения занимают отдельные позиции. k начинается с 1.
    """
    if not 1 <= k <= len(nums):
        raise ValueError("k должен быть от 1 до длины массива")

    values = nums.copy()
    target = len(values) - k
    low, high = 0, len(values) - 1
    while low <= high:
        pivot = values[(low + high) // 2]
        less, current, greater = low, low, high
        while current <= greater:
            if values[current] < pivot:
                values[less], values[current] = values[current], values[less]
                less += 1
                current += 1
            elif values[current] > pivot:
                values[current], values[greater] = values[greater], values[current]
                greater -= 1
            else:
                current += 1
        if target < less:
            high = less - 1
        elif target > greater:
            low = greater + 1
        else:
            return values[target]

    raise AssertionError("недостижимое состояние quickselect")


def main() -> None:
    print(find_kth_largest([3, 2, 1, 5, 6, 4], 2))
    print(find_kth_largest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))


if __name__ == "__main__":
    main()
