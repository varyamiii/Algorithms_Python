import unittest

from homework_2.stack_vs_queue.stack_vs_queue import LinkedQueue, LinkedStack


class LinkedStackTests(unittest.TestCase):
    def test_lifo_order(self) -> None:
        stack = LinkedStack()
        for value in (1, 2, 3):
            stack.push(value)

        self.assertEqual([stack.pop(), stack.pop(), stack.pop()], [3, 2, 1])

    def test_peek_does_not_remove(self) -> None:
        stack = LinkedStack()
        stack.push(10)
        stack.push(20)

        self.assertEqual(stack.peek(), 20)
        self.assertEqual(len(stack), 2)

    def test_is_empty_and_len(self) -> None:
        stack = LinkedStack()
        self.assertTrue(stack.is_empty())
        self.assertEqual(len(stack), 0)

        stack.push(1)
        self.assertFalse(stack.is_empty())
        self.assertEqual(len(stack), 1)

    def test_pop_empty_raises(self) -> None:
        stack = LinkedStack()
        with self.assertRaises(IndexError):
            stack.pop()

    def test_peek_empty_raises(self) -> None:
        stack = LinkedStack()
        with self.assertRaises(IndexError):
            stack.peek()

    def test_interleaved_operations(self) -> None:
        stack = LinkedStack()
        stack.push(1)
        stack.push(2)
        self.assertEqual(stack.pop(), 2)
        stack.push(3)
        self.assertEqual(stack.pop(), 3)
        self.assertEqual(stack.pop(), 1)
        self.assertTrue(stack.is_empty())


class LinkedQueueTests(unittest.TestCase):
    def test_fifo_order(self) -> None:
        queue = LinkedQueue()
        for value in (1, 2, 3):
            queue.enqueue(value)

        self.assertEqual([queue.dequeue(), queue.dequeue(), queue.dequeue()], [1, 2, 3])

    def test_peek_does_not_remove(self) -> None:
        queue = LinkedQueue()
        queue.enqueue(10)
        queue.enqueue(20)

        self.assertEqual(queue.peek(), 10)
        self.assertEqual(len(queue), 2)

    def test_is_empty_and_len(self) -> None:
        queue = LinkedQueue()
        self.assertTrue(queue.is_empty())
        self.assertEqual(len(queue), 0)

        queue.enqueue(1)
        self.assertFalse(queue.is_empty())
        self.assertEqual(len(queue), 1)

    def test_dequeue_empty_raises(self) -> None:
        queue = LinkedQueue()
        with self.assertRaises(IndexError):
            queue.dequeue()

    def test_peek_empty_raises(self) -> None:
        queue = LinkedQueue()
        with self.assertRaises(IndexError):
            queue.peek()

    def test_interleaved_operations(self) -> None:
        queue = LinkedQueue()
        queue.enqueue(1)
        queue.enqueue(2)
        self.assertEqual(queue.dequeue(), 1)
        queue.enqueue(3)
        self.assertEqual(queue.dequeue(), 2)
        self.assertEqual(queue.dequeue(), 3)
        self.assertTrue(queue.is_empty())

    def test_reuse_after_empty(self) -> None:
        queue = LinkedQueue()
        queue.enqueue(1)
        queue.dequeue()
        queue.enqueue(2)
        self.assertEqual(queue.dequeue(), 2)


if __name__ == "__main__":
    unittest.main()
