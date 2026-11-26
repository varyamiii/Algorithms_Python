"""Поиск k-го наибольшего элемента при помощи minheap размера k."""

import heapq

from homework_7.Makeheap.makeheap import _sift_down, makeheap


def _validate_k(nums: list[int], k: int) -> None:
    if not isinstance(k, int) or isinstance(k, bool) or not 1 <= k <= len(nums):
        raise ValueError("k должно быть целым числом от 1 до len(nums)")


def k_th_largest(nums: list[int], k: int) -> int:
    """Собственная куча; входной список не изменяется."""
    _validate_k(nums, k)
    heap = nums[:k]
    makeheap(heap)
    for index in range(k, len(nums)):
        value = nums[index]
        if value > heap[0]:
            heap[0] = value
            _sift_down(heap, 0, k)
    return heap[0]


def k_th_largest_heapq(nums: list[int], k: int) -> int:
    """Та же идея с библиотечной реализацией minheap."""
    _validate_k(nums, k)
    heap = nums[:k]
    heapq.heapify(heap)
    for index in range(k, len(nums)):
        value = nums[index]
        if value > heap[0]:
            heapq.heapreplace(heap, value)
    return heap[0]


def main() -> None:
    values = [3, 2, 1, 5, 6, 4]
    print("Своя куча:", k_th_largest(values, 2))
    print("heapq:", k_th_largest_heapq(values, 2))


if __name__ == "__main__":
    main()
