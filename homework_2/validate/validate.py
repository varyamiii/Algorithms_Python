from typing import List


def validate_stack_sequences(pushed: List[int], popped: List[int]) -> bool:
    """Проверяет, можно ли получить popped из pushed операциями push/pop."""
    stack: List[int] = []
    pop_index = 0

    for value in pushed:
        stack.append(value)
        while stack and stack[-1] == popped[pop_index]:
            stack.pop()
            pop_index += 1

    return len(stack) == 0


def main() -> None:
    print("Введите последовательность pushed через пробел и нажмите Enter:")
    pushed = [int(item) for item in input().split()]
    print("Введите последовательность popped через пробел и нажмите Enter:")
    popped = [int(item) for item in input().split()]
    print(validate_stack_sequences(pushed, popped))


if __name__ == "__main__":
    main()
