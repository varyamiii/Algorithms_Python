from typing import Dict, List, Tuple


def two_sum(arr: List[int], k: int) -> Tuple[int, int]:
    """Возвращает индексы двух элементов, сумма которых равна k."""
    index_by_value: Dict[int, int] = {}

    for current_index, current_value in enumerate(arr):
        required_value = k - current_value
        if required_value in index_by_value:
            return index_by_value[required_value], current_index

        index_by_value[current_value] = current_index

    raise ValueError("В массиве нет двух элементов с заданной суммой")


def main() -> None:
    print("Введите целые числа через пробел и нажмите Enter:")
    numbers = [int(item) for item in input().split()]
    print("Введите искомую сумму:")
    target = int(input())
    first_index, second_index = two_sum(numbers, target)
    print(first_index, second_index)


if __name__ == "__main__":
    main()
