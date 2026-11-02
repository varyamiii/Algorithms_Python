import math
import random
import unittest
from typing import Optional

from homework_5.AVL.avl import AVL, AVLNode


def assert_avl_invariants(
    test_case: unittest.TestCase,
    node: Optional[AVLNode[int]],
    lower: Optional[int] = None,
    upper: Optional[int] = None,
) -> int:
    if node is None:
        return 0

    if lower is not None:
        test_case.assertGreater(node.key, lower)
    if upper is not None:
        test_case.assertLess(node.key, upper)

    left_height = assert_avl_invariants(test_case, node.left, lower, node.key)
    right_height = assert_avl_invariants(test_case, node.right, node.key, upper)
    test_case.assertLessEqual(abs(left_height - right_height), 1)
    test_case.assertEqual(node.height, 1 + max(left_height, right_height))
    return node.height


class AVLTests(unittest.TestCase):
    def assert_valid(self, tree: AVL[int]) -> None:
        assert_avl_invariants(self, tree.root)
        self.assertEqual(len(tree), len(tree.inorder()))

    def test_insert_search_and_sorted_traversal(self) -> None:
        tree: AVL[int] = AVL()
        for value in (40, 10, 60, 20, 50, 70, 30):
            self.assertTrue(tree.insert(value))

        self.assertEqual(tree.inorder(), [10, 20, 30, 40, 50, 60, 70])
        self.assertTrue(tree.search(50))
        self.assertFalse(tree.search(99))
        self.assertIn(20, tree)
        self.assertNotIn(21, tree)
        self.assert_valid(tree)

    def test_all_four_rotation_cases(self) -> None:
        cases = (
            (30, 20, 10),  # правое вращение (LL)
            (10, 20, 30),  # левое вращение (RR)
            (30, 10, 20),  # двойное левое-правое (LR)
            (10, 30, 20),  # двойное правое-левое (RL)
        )
        for values in cases:
            with self.subTest(values=values):
                tree: AVL[int] = AVL()
                for value in values:
                    tree.insert(value)
                self.assertIsNotNone(tree.root)
                self.assertEqual(tree.root.key, 20)  # type: ignore[union-attr]
                self.assertEqual(tree.inorder(), [10, 20, 30])
                self.assert_valid(tree)

    def test_duplicate_is_ignored(self) -> None:
        tree: AVL[int] = AVL()
        self.assertTrue(tree.insert(5))
        self.assertFalse(tree.insert(5))
        self.assertEqual(tree.inorder(), [5])
        self.assertEqual(len(tree), 1)

    def test_delete_leaf_node_with_one_child_and_with_two_children(self) -> None:
        tree: AVL[int] = AVL()
        for value in (40, 20, 60, 10, 30, 50, 70, 25):
            tree.insert(value)

        self.assertTrue(tree.delete(10))  # лист
        self.assertTrue(tree.delete(30))  # после первого удаления имеет ребёнка 25
        self.assertTrue(tree.delete(60))  # два ребёнка
        self.assertEqual(tree.inorder(), [20, 25, 40, 50, 70])
        self.assert_valid(tree)

    def test_delete_can_trigger_rebalancing(self) -> None:
        tree: AVL[int] = AVL()
        for value in (9, 5, 10, 0, 6, 11, -1, 1, 2):
            tree.insert(value)

        self.assertTrue(tree.delete(10))
        self.assertEqual(tree.inorder(), [-1, 0, 1, 2, 5, 6, 9, 11])
        self.assert_valid(tree)

    def test_delete_missing_key_and_empty_tree(self) -> None:
        tree: AVL[int] = AVL()
        self.assertFalse(tree.search(1))
        self.assertFalse(tree.delete(1))
        self.assertEqual(tree.inorder(), [])
        self.assertEqual(tree.to_ascii(), "<empty>")
        self.assertEqual(tree.height, 0)
        self.assert_valid(tree)

    def test_many_operations_keep_tree_balanced(self) -> None:
        tree: AVL[int] = AVL()
        values = list(range(200))
        random.Random(42).shuffle(values)
        for value in values:
            tree.insert(value)

        self.assertLessEqual(tree.height, math.ceil(1.45 * math.log2(202)))
        self.assert_valid(tree)

        for value in values[::3]:
            self.assertTrue(tree.delete(value))
        expected = sorted(set(values) - set(values[::3]))
        self.assertEqual(tree.inorder(), expected)
        self.assert_valid(tree)

    def test_ascii_visualization(self) -> None:
        tree: AVL[int] = AVL()
        for value in (20, 10, 30, 25):
            tree.insert(value)

        self.assertEqual(
            tree.to_ascii(),
            "20\n|-- L: 10\n`-- R: 30\n    `-- L: 25",
        )


if __name__ == "__main__":
    unittest.main()
