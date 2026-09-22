from typing import Any, Optional


class Node:
    def __init__(self, value: Any, next_node: "Optional[Node]" = None) -> None:
        self.value = value
        self.next = next_node


class LinkedStack:
    """Стек (LIFO) на основе односвязного списка."""

    def __init__(self) -> None:
        self.head: Optional[Node] = None
        self.size = 0

    def is_empty(self) -> bool:
        return self.head is None

    def push(self, value: Any) -> None:
        self.head = Node(value, self.head)
        self.size += 1

    def pop(self) -> Any:
        if self.head is None:
            raise IndexError("pop из пустого стека")

        top_node = self.head
        self.head = top_node.next
        self.size -= 1
        return top_node.value

    def peek(self) -> Any:
        if self.head is None:
            raise IndexError("peek из пустого стека")

        return self.head.value

    def __len__(self) -> int:
        return self.size


class LinkedQueue:
    """Очередь (FIFO) на основе односвязного списка."""

    def __init__(self) -> None:
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None
        self.size = 0

    def is_empty(self) -> bool:
        return self.head is None

    def enqueue(self, value: Any) -> None:
        new_node = Node(value)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def dequeue(self) -> Any:
        if self.head is None:
            raise IndexError("dequeue из пустой очереди")

        front_node = self.head
        self.head = front_node.next
        if self.head is None:
            self.tail = None
        self.size -= 1
        return front_node.value

    def peek(self) -> Any:
        if self.head is None:
            raise IndexError("peek из пустой очереди")

        return self.head.value

    def __len__(self) -> int:
        return self.size


def main() -> None:
    print("Введите целые числа через пробел и нажмите Enter:")
    numbers = [int(item) for item in input().split()]

    stack = LinkedStack()
    for value in numbers:
        stack.push(value)
    print("Стек (LIFO):", [stack.pop() for _ in range(len(stack))])

    queue = LinkedQueue()
    for value in numbers:
        queue.enqueue(value)
    print("Очередь (FIFO):", [queue.dequeue() for _ in range(len(queue))])


if __name__ == "__main__":
    main()
