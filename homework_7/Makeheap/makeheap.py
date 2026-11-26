"""Два способа построения minheap непосредственно в исходном списке."""


def _sift_down(arr: list[int], start: int, size: int) -> None:
    """Опускает элемент start в куче из первых size элементов."""
    index = start
    while 2 * index + 1 < size:
        child = 2 * index + 1
        if child + 1 < size and arr[child + 1] < arr[child]:
            child += 1
        if arr[index] <= arr[child]:
            break
        arr[index], arr[child] = arr[child], arr[index]
        index = child


def makeheap_n_log_n(arr: list[int]) -> list[int]:
    """Строит minheap последовательными вставками: O(n log n) времени."""
    for index in range(1, len(arr)):
        child = index
        while child > 0:
            parent = (child - 1) // 2
            if arr[parent] <= arr[child]:
                break
            arr[parent], arr[child] = arr[child], arr[parent]
            child = parent
    return arr


def makeheap(arr: list[int]) -> list[int]:
    """Строит minheap снизу вверх: O(n) времени."""
    for index in range(len(arr) // 2 - 1, -1, -1):
        _sift_down(arr, index, len(arr))
    return arr


def main() -> None:
    values = [9, 4, 7, 1, 5, 3]
    print("Вставка:", makeheap_n_log_n(values.copy()))
    print("Снизу вверх:", makeheap(values.copy()))


if __name__ == "__main__":
    main()
