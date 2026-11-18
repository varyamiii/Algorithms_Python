"""Итеративные merge sort и quicksort."""

from homework_6.compare.compare import _partition


def merge_sort_iterative(nums: list[int]) -> list[int]:
    """Сортировка слиянием снизу вверх без рекурсии и изменения входа."""
    result = nums.copy()
    size = len(result)
    buffer = result.copy()
    width = 1
    while width < size:
        for start in range(0, size, 2 * width):
            middle = min(start + width, size)
            end = min(start + 2 * width, size)
            left, right, target = start, middle, start
            while left < middle and right < end:
                if result[left] <= result[right]:
                    buffer[target] = result[left]
                    left += 1
                else:
                    buffer[target] = result[right]
                    right += 1
                target += 1
            while left < middle:
                buffer[target] = result[left]
                left += 1
                target += 1
            while right < end:
                buffer[target] = result[right]
                right += 1
                target += 1
        result, buffer = buffer, result
        width *= 2
    return result


def quick_sort_iterative(nums: list[int]) -> list[int]:
    """Быстрая сортировка с явным стеком диапазонов."""
    result = nums.copy()
    if len(result) < 2:
        return result

    stack = [(0, len(result) - 1)]
    while stack:
        low, high = stack.pop()
        while low < high:
            pivot_index = _partition(result, low, high)
            # Больший диапазон откладываем, меньший обрабатываем сразу.
            if pivot_index - low < high - pivot_index:
                if pivot_index + 1 < high:
                    stack.append((pivot_index + 1, high))
                high = pivot_index - 1
            else:
                if low < pivot_index - 1:
                    stack.append((low, pivot_index - 1))
                low = pivot_index + 1
    return result


def main() -> None:
    values = [8, 3, 5, 1, 7, 3]
    print("Merge sort:", merge_sort_iterative(values))
    print("Quicksort:", quick_sort_iterative(values))


if __name__ == "__main__":
    main()
