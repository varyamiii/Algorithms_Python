"""Сортировка кучей по возрастанию без дополнительного массива."""


def _sift_down_max(arr: list[int], start: int, size: int) -> None:
    index = start
    while 2 * index + 1 < size:
        child = 2 * index + 1
        if child + 1 < size and arr[child + 1] > arr[child]:
            child += 1
        if arr[index] >= arr[child]:
            break
        arr[index], arr[child] = arr[child], arr[index]
        index = child


def heapsort(arr: list[int]) -> list[int]:
    """Сортирует arr на месте; возвращает тот же список для удобства."""
    size = len(arr)
    for index in range(size // 2 - 1, -1, -1):
        _sift_down_max(arr, index, size)
    for end in range(size - 1, 0, -1):
        arr[0], arr[end] = arr[end], arr[0]
        _sift_down_max(arr, 0, end)
    return arr


def main() -> None:
    values = [8, 3, 5, 1, 7, 3]
    print("Heapsort:", heapsort(values))


if __name__ == "__main__":
    main()
