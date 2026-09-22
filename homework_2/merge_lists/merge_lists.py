from typing import List, Optional


class ListNode:
    def __init__(self, value: int, next_node: "Optional[ListNode]" = None) -> None:
        self.value = value
        self.next = next_node


def build_list(values: List[int]) -> Optional[ListNode]:
    """Строит односвязный список из обычного списка значений."""
    head: Optional[ListNode] = None
    for value in reversed(values):
        head = ListNode(value, head)
    return head


def to_python_list(head: Optional[ListNode]) -> List[int]:
    """Переводит односвязный список обратно в обычный список значений."""
    values: List[int] = []
    current = head
    while current is not None:
        values.append(current.value)
        current = current.next
    return values


def merge_with_dummy(
    list1: Optional[ListNode], list2: Optional[ListNode]
) -> Optional[ListNode]:
    """Слияние с фиктивным элементом: убирает особый случай для головы."""
    dummy = ListNode(0)
    tail = dummy

    while list1 is not None and list2 is not None:
        if list1.value <= list2.value:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next

    tail.next = list1 if list1 is not None else list2
    return dummy.next


def merge_without_dummy(
    list1: Optional[ListNode], list2: Optional[ListNode]
) -> Optional[ListNode]:
    """Слияние без фиктивного элемента: голова выбирается вручную."""
    if list1 is None:
        return list2
    if list2 is None:
        return list1

    if list1.value <= list2.value:
        head = list1
        list1 = list1.next
    else:
        head = list2
        list2 = list2.next

    tail = head
    while list1 is not None and list2 is not None:
        if list1.value <= list2.value:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next

    tail.next = list1 if list1 is not None else list2
    return head


def main() -> None:
    print("Введите первый отсортированный список чисел через пробел:")
    values1 = [int(item) for item in input().split()]
    print("Введите второй отсортированный список чисел через пробел:")
    values2 = [int(item) for item in input().split()]

    print(
        "С фиктивным элементом:",
        to_python_list(merge_with_dummy(build_list(values1), build_list(values2))),
    )
    print(
        "Без фиктивного элемента:",
        to_python_list(merge_without_dummy(build_list(values1), build_list(values2))),
    )


if __name__ == "__main__":
    main()
