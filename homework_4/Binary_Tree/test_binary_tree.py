import unittest
from contextlib import redirect_stdout
from io import StringIO
from unittest.mock import patch

from homework_4.Binary_Tree.binary_tree import (
    BinarySearchTree,
    TreeNode,
    inorder,
    is_balanced,
    is_valid_bst,
    main,
    postorder,
    preorder,
    reverse_inorder,
    reverse_postorder,
    reverse_preorder,
)


class BinarySearchTreeTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tree = BinarySearchTree()
        for value in [8, 3, 10, 1, 6, 14, 4, 7, 13]:
            self.tree.insert(value)

    def test_insert_builds_valid_bst(self) -> None:
        self.assertTrue(is_valid_bst(self.tree.root))
        self.assertEqual(self.tree.inorder(), [1, 3, 4, 6, 7, 8, 10, 13, 14])

    def test_duplicate_is_not_inserted_twice(self) -> None:
        existing_node = self.tree.insert(6)

        self.assertEqual(existing_node.value, 6)
        self.assertEqual(self.tree.inorder().count(6), 1)
        self.assertTrue(is_valid_bst(self.tree.root))

    def test_six_traversals(self) -> None:
        self.assertEqual(
            self.tree.preorder(), [8, 3, 1, 6, 4, 7, 10, 14, 13]
        )
        self.assertEqual(
            self.tree.inorder(), [1, 3, 4, 6, 7, 8, 10, 13, 14]
        )
        self.assertEqual(
            self.tree.postorder(), [1, 4, 7, 6, 3, 13, 14, 10, 8]
        )
        self.assertEqual(
            self.tree.reverse_preorder(), [8, 10, 14, 13, 3, 6, 7, 4, 1]
        )
        self.assertEqual(
            self.tree.reverse_inorder(), [14, 13, 10, 8, 7, 6, 4, 3, 1]
        )
        self.assertEqual(
            self.tree.reverse_postorder(), [13, 14, 10, 7, 4, 6, 1, 3, 8]
        )

    def test_empty_tree_traversals_return_empty_lists(self) -> None:
        tree = BinarySearchTree()

        self.assertEqual(tree.preorder(), [])
        self.assertEqual(tree.inorder(), [])
        self.assertEqual(tree.postorder(), [])
        self.assertEqual(tree.reverse_preorder(), [])
        self.assertEqual(tree.reverse_inorder(), [])
        self.assertEqual(tree.reverse_postorder(), [])

    def test_single_node_and_negative_values(self) -> None:
        tree = BinarySearchTree()
        tree.insert(0)
        tree.insert(-2)

        self.assertEqual(tree.preorder(), [0, -2])
        self.assertEqual(tree.inorder(), [-2, 0])

    def test_traversal_functions_accept_arbitrary_tree(self) -> None:
        root = TreeNode("root", TreeNode("left"), TreeNode("right"))

        self.assertEqual(preorder(root), ["root", "left", "right"])
        self.assertEqual(inorder(root), ["left", "root", "right"])
        self.assertEqual(postorder(root), ["left", "right", "root"])
        self.assertEqual(reverse_preorder(root), ["root", "right", "left"])
        self.assertEqual(reverse_inorder(root), ["right", "root", "left"])
        self.assertEqual(reverse_postorder(root), ["right", "left", "root"])


class ValidateBstTests(unittest.TestCase):
    def test_empty_and_single_node_trees_are_valid(self) -> None:
        self.assertTrue(is_valid_bst(None))
        self.assertTrue(is_valid_bst(TreeNode(5)))

    def test_valid_tree_is_accepted(self) -> None:
        root = TreeNode(
            8,
            TreeNode(3, TreeNode(1), TreeNode(6)),
            TreeNode(10, None, TreeNode(14)),
        )

        self.assertTrue(is_valid_bst(root))

    def test_local_order_violation_is_rejected(self) -> None:
        root = TreeNode(8, TreeNode(9), TreeNode(10))

        self.assertFalse(is_valid_bst(root))

    def test_deep_order_violation_is_rejected(self) -> None:
        # 9 находится в левом поддереве 8: локально он больше 3,
        # но нарушает ограничение, заданное корнем.
        root = TreeNode(8, TreeNode(3, None, TreeNode(9)), TreeNode(10))

        self.assertFalse(is_valid_bst(root))

    def test_duplicate_value_is_rejected(self) -> None:
        root = TreeNode(8, TreeNode(3), TreeNode(8))

        self.assertFalse(is_valid_bst(root))

    def test_zero_and_negative_values(self) -> None:
        root = TreeNode(0, TreeNode(-10), TreeNode(5))

        self.assertTrue(is_valid_bst(root))


class BalancedTreeTests(unittest.TestCase):
    def test_empty_and_single_node_trees_are_balanced(self) -> None:
        self.assertTrue(is_balanced(None))
        self.assertTrue(is_balanced(TreeNode(1)))

    def test_balanced_tree_is_accepted(self) -> None:
        root = TreeNode(
            8,
            TreeNode(3, TreeNode(1), TreeNode(6)),
            TreeNode(10, None, TreeNode(14)),
        )

        self.assertTrue(is_balanced(root))

    def test_difference_of_exactly_one_is_allowed(self) -> None:
        root = TreeNode(1, TreeNode(2, TreeNode(3)), TreeNode(4))

        self.assertTrue(is_balanced(root))

    def test_unbalanced_tree_is_rejected(self) -> None:
        root = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4))), None)

        self.assertFalse(is_balanced(root))

    def test_root_can_look_balanced_while_descendant_is_not(self) -> None:
        root = TreeNode(
            1,
            TreeNode(2, TreeNode(3, TreeNode(4))),
            TreeNode(5, None, TreeNode(6, None, TreeNode(7))),
        )

        self.assertFalse(is_balanced(root))


class ConsoleTests(unittest.TestCase):
    @patch("builtins.input", return_value="8 3 10 1 6")
    def test_main_prints_traversals_and_checks(self, _mocked_input: object) -> None:
        output = StringIO()

        with redirect_stdout(output):
            main()

        console_output = output.getvalue()
        self.assertIn("Preorder: [8, 3, 1, 6, 10]", console_output)
        self.assertIn("Inorder: [1, 3, 6, 8, 10]", console_output)
        self.assertIn("Корректное BST: True", console_output)
        self.assertIn("Сбалансировано: True", console_output)

    @patch("builtins.input", return_value="1 two 3")
    def test_main_rejects_non_integer_input(self, _mocked_input: object) -> None:
        output = StringIO()

        with redirect_stdout(output):
            main()

        self.assertIn("Все значения должны быть целыми числами.", output.getvalue())


if __name__ == "__main__":
    unittest.main()
