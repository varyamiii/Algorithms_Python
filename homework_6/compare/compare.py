"""Рекурсивные merge sort, quicksort и декоратор измерения времени."""

from functools import wraps
from time import perf_counter
from typing import Callable, ParamSpec, TypeVar


P = ParamSpec("P")
R = TypeVar("R")


def measure_time(function: Callable[P, R]) -> Callable[P, R]:
    """Печатает длительность вызова в секундах и возвращает его результат."""

    @wraps(function)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
        start = perf_counter()
        try:
            return function(*args, **kwargs)
        finally:
            print(f"{function.__name__}: {perf_counter() - start:.6f} с")

    return wrapper


def merge_sort_recursive(nums: list[int]) -> list[int]:
    """Возвращает отсортированную копию списка рекурсивным слиянием."""
    if len(nums) < 2:
        return nums.copy()

    middle = len(nums) // 2
    left = merge_sort_recursive(nums[:middle])
    right = merge_sort_recursive(nums[middle:])
    result: list[int] = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


@measure_time
def merge_sort_recursive_timed(nums: list[int]) -> list[int]:
    return merge_sort_recursive(nums)


def _partition(nums: list[int], low: int, high: int) -> int:
    """Ставит последний элемент на окончательную позицию (схема Ломуто)."""
    pivot = nums[high]
    boundary = low
    for index in range(low, high):
        if nums[index] <= pivot:
            nums[boundary], nums[index] = nums[index], nums[boundary]
            boundary += 1
    nums[boundary], nums[high] = nums[high], nums[boundary]
    return boundary


def quick_sort_recursive(nums: list[int]) -> list[int]:
    """Возвращает отсортированную копию списка рекурсивной быстрой сортировкой."""
    result = nums.copy()

    def sort(low: int, high: int) -> None:
        # Рекурсивно обрабатываем меньшую часть: глубина стека O(log n).
        while low < high:
            pivot_index = _partition(result, low, high)
            if pivot_index - low < high - pivot_index:
                sort(low, pivot_index - 1)
                low = pivot_index + 1
            else:
                sort(pivot_index + 1, high)
                high = pivot_index - 1

    sort(0, len(result) - 1)
    return result


@measure_time
def quick_sort_recursive_timed(nums: list[int]) -> list[int]:
    return quick_sort_recursive(nums)


def main() -> None:
    data = list(range(600))
    print("Отсортированный массив из 600 элементов:")
    assert merge_sort_recursive_timed(data) == data
    assert quick_sort_recursive_timed(data) == data


if __name__ == "__main__":
    main()
