from __future__ import annotations

from dataclasses import dataclass
from typing import Any, List, Optional


@dataclass
class TreeNode:
    """Узел бинарного дерева."""

    value: Any
    left: Optional[TreeNode] = None
    right: Optional[TreeNode] = None


class BinarySearchTree:
    """Бинарное дерево поиска без повторяющихся значений."""

    def __init__(self) -> None:
        self.root: Optional[TreeNode] = None

    def insert(self, value: Any) -> TreeNode:
        """Вставляет значение и возвращает созданный или найденный узел.

        Если значение уже есть в дереве, структура дерева не изменяется.
        """
        if self.root is None:
            self.root = TreeNode(value)
            return self.root

        current = self.root
        while True:
            if value == current.value:
                return current

            if value < current.value:
                if current.left is None:
                    current.left = TreeNode(value)
                    return current.left
                current = current.left
            else:
                if current.right is None:
                    current.right = TreeNode(value)
                    return current.right
                current = current.right

    def preorder(self) -> List[Any]:
        return preorder(self.root)

    def inorder(self) -> List[Any]:
        return inorder(self.root)

    def postorder(self) -> List[Any]:
        return postorder(self.root)

    def reverse_preorder(self) -> List[Any]:
        return reverse_preorder(self.root)

    def reverse_inorder(self) -> List[Any]:
        return reverse_inorder(self.root)

    def reverse_postorder(self) -> List[Any]:
        return reverse_postorder(self.root)


def preorder(root: Optional[TreeNode]) -> List[Any]:
    """Обход NLR: узел, левое поддерево, правое поддерево."""
    result: List[Any] = []

    def visit(node: Optional[TreeNode]) -> None:
        if node is None:
            return
        result.append(node.value)
        visit(node.left)
        visit(node.right)

    visit(root)
    return result


def inorder(root: Optional[TreeNode]) -> List[Any]:
    """Обход LNR: левое поддерево, узел, правое поддерево."""
    result: List[Any] = []

    def visit(node: Optional[TreeNode]) -> None:
        if node is None:
            return
        visit(node.left)
        result.append(node.value)
        visit(node.right)

    visit(root)
    return result


def postorder(root: Optional[TreeNode]) -> List[Any]:
    """Обход LRN: левое поддерево, правое поддерево, узел."""
    result: List[Any] = []

    def visit(node: Optional[TreeNode]) -> None:
        if node is None:
            return
        visit(node.left)
        visit(node.right)
        result.append(node.value)

    visit(root)
    return result


def reverse_preorder(root: Optional[TreeNode]) -> List[Any]:
    """Обратный preorder NRL: узел, правое поддерево, левое."""
    result: List[Any] = []

    def visit(node: Optional[TreeNode]) -> None:
        if node is None:
            return
        result.append(node.value)
        visit(node.right)
        visit(node.left)

    visit(root)
    return result


def reverse_inorder(root: Optional[TreeNode]) -> List[Any]:
    """Обратный inorder RNL: правое поддерево, узел, левое."""
    result: List[Any] = []

    def visit(node: Optional[TreeNode]) -> None:
        if node is None:
            return
        visit(node.right)
        result.append(node.value)
        visit(node.left)

    visit(root)
    return result


def reverse_postorder(root: Optional[TreeNode]) -> List[Any]:
    """Обратный postorder RLN: правое поддерево, левое, узел."""
    result: List[Any] = []

    def visit(node: Optional[TreeNode]) -> None:
        if node is None:
            return
        visit(node.right)
        visit(node.left)
        result.append(node.value)

    visit(root)
    return result


def is_valid_bst(root: Optional[TreeNode]) -> bool:
    """Проверяет строгое свойство BST для всего дерева.

    Все значения в левом поддереве должны быть меньше значения узла, а все
    значения в правом поддереве — больше. Повторяющиеся значения запрещены.
    """

    def validate(
        node: Optional[TreeNode],
        lower_bound: Any,
        upper_bound: Any,
        has_lower_bound: bool,
        has_upper_bound: bool,
    ) -> bool:
        if node is None:
            return True
        if has_lower_bound and node.value <= lower_bound:
            return False
        if has_upper_bound and node.value >= upper_bound:
            return False

        return validate(
            node.left,
            lower_bound,
            node.value,
            has_lower_bound,
            True,
        ) and validate(
            node.right,
            node.value,
            upper_bound,
            True,
            has_upper_bound,
        )

    return validate(root, None, None, False, False)


def is_balanced(root: Optional[TreeNode]) -> bool:
    """Проверяет баланс высот за один обход снизу вверх."""

    def height_or_unbalanced(node: Optional[TreeNode]) -> int:
        if node is None:
            return 0

        left_height = height_or_unbalanced(node.left)
        if left_height == -1:
            return -1

        right_height = height_or_unbalanced(node.right)
        if right_height == -1:
            return -1

        if abs(left_height - right_height) > 1:
            return -1
        return max(left_height, right_height) + 1

    return height_or_unbalanced(root) != -1


def main() -> None:
    tree = BinarySearchTree()
    raw_values = input("Введите значения узлов через пробел: ").split()

    try:
        values = [int(value) for value in raw_values]
    except ValueError:
        print("Все значения должны быть целыми числами.")
        return

    for value in values:
        tree.insert(value)

    print("Preorder:", tree.preorder())
    print("Inorder:", tree.inorder())
    print("Postorder:", tree.postorder())
    print("Reverse preorder:", tree.reverse_preorder())
    print("Reverse inorder:", tree.reverse_inorder())
    print("Reverse postorder:", tree.reverse_postorder())
    print("Корректное BST:", is_valid_bst(tree.root))
    print("Сбалансировано:", is_balanced(tree.root))


if __name__ == "__main__":
    main()
