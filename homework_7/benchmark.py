"""Повторяемое сравнение алгоритмов на одинаковых входных данных."""

import random
from statistics import median
from time import perf_counter

from homework_6.compare.compare import merge_sort_recursive
from homework_7.Heapsort.heapsort import heapsort
from homework_7.Makeheap.makeheap import makeheap, makeheap_n_log_n


def measure(function, data: list[int], repeats: int = 7) -> float:
    """Медиана времени в миллисекундах; копирование входа не учитывается."""
    timings = []
    expected = sorted(data)
    for _ in range(repeats):
        values = data.copy()
        start = perf_counter()
        result = function(values)
        timings.append((perf_counter() - start) * 1000)
        if function in (makeheap, makeheap_n_log_n):
            assert sorted(result) == expected
            assert all(result[(i - 1) // 2] <= result[i] for i in range(1, len(result)))
        else:
            assert result == expected
    return median(timings)


def main() -> None:
    rng = random.Random(42)
    print("Случайный массив: n | makeheap_n_log_n | makeheap | heapsort | sorted | mergesort (мс)")
    for size in (1_000, 5_000, 20_000):
        data = [rng.randrange(-1_000_000, 1_000_001) for _ in range(size)]
        timings = [
            measure(function, data)
            for function in (makeheap_n_log_n, makeheap, heapsort, sorted, merge_sort_recursive)
        ]
        print(f"{size} | " + " | ".join(f"{value:.3f}" for value in timings))
    print("Убывающий массив: n | makeheap_n_log_n | makeheap (мс)")
    for size in (1_000, 5_000, 20_000):
        data = list(range(size, 0, -1))
        timings = [measure(function, data) for function in (makeheap_n_log_n, makeheap)]
        print(f"{size} | " + " | ".join(f"{value:.3f}" for value in timings))


if __name__ == "__main__":
    main()
