"""Построение всех уникальных перестановок массива."""

from typing import List, Sequence, TextIO

from homework_5.tracer.tracer import trace


def permutations(
    nums: Sequence[int],
    *,
    visualize: bool = False,
    stream: TextIO | None = None,
) -> List[List[int]]:
    """Возвращает все уникальные перестановки элементов ``nums``.

    Исходная последовательность не изменяется. При ``visualize=True`` каждый
    рекурсивный вызов и его результат выводятся декоратором из первой задачи.
    """
    initial_values = tuple(nums)

    def build_permutations(remaining: tuple[int, ...]) -> List[List[int]]:
        if not remaining:
            return [[]]

        result: List[List[int]] = []
        used_at_this_depth: set[int] = set()

        for index, value in enumerate(remaining):
            if value in used_at_this_depth:
                continue
            used_at_this_depth.add(value)

            rest = remaining[:index] + remaining[index + 1 :]
            for tail in recursive_call(rest):
                result.append([value, *tail])

        return result

    recursive_call = (
        trace(stream=stream)(build_permutations)
        if visualize
        else build_permutations
    )
    return recursive_call(initial_values)


def main() -> None:
    print("Введите целые числа через пробел:")
    numbers = [int(item) for item in input().split()]
    print("Стек рекурсивных вызовов:")
    result = permutations(numbers, visualize=True)
    print("Все перестановки:", result)


if __name__ == "__main__":
    main()
