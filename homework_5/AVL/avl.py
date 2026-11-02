"""AVL-дерево с операциями вставки, удаления и поиска."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Generic, Iterator, List, Optional, TypeVar


Key = TypeVar("Key")


@dataclass
class AVLNode(Generic[Key]):
    key: Key
    height: int = 1
    left: Optional[AVLNode[Key]] = None
    right: Optional[AVLNode[Key]] = None


class AVL(Generic[Key]):
    """Сбалансированное дерево поиска без повторяющихся ключей."""

    def __init__(self) -> None:
        self._root: Optional[AVLNode[Key]] = None
        self._size = 0

    @staticmethod
    def _height(node: Optional[AVLNode[Key]]) -> int:
        return node.height if node is not None else 0

    @classmethod
    def _update_height(cls, node: AVLNode[Key]) -> None:
        node.height = 1 + max(cls._height(node.left), cls._height(node.right))

    @classmethod
    def _balance_factor(cls, node: AVLNode[Key]) -> int:
        return cls._height(node.left) - cls._height(node.right)

    @classmethod
    def _rotate_right(cls, root: AVLNode[Key]) -> AVLNode[Key]:
        new_root = root.left
        if new_root is None:  # Защита внутреннего инварианта.
            return root

        moved_subtree = new_root.right
        new_root.right = root
        root.left = moved_subtree
        cls._update_height(root)
        cls._update_height(new_root)
        return new_root

    @classmethod
    def _rotate_left(cls, root: AVLNode[Key]) -> AVLNode[Key]:
        new_root = root.right
        if new_root is None:  # Защита внутреннего инварианта.
            return root

        moved_subtree = new_root.left
        new_root.left = root
        root.right = moved_subtree
        cls._update_height(root)
        cls._update_height(new_root)
        return new_root

    @classmethod
    def _rebalance(cls, node: AVLNode[Key]) -> AVLNode[Key]:
        cls._update_height(node)
        balance = cls._balance_factor(node)

        if balance > 1:
            if node.left is not None and cls._balance_factor(node.left) < 0:
                node.left = cls._rotate_left(node.left)
            return cls._rotate_right(node)

        if balance < -1:
            if node.right is not None and cls._balance_factor(node.right) > 0:
                node.right = cls._rotate_right(node.right)
            return cls._rotate_left(node)

        return node

    @classmethod
    def _insert(
        cls, node: Optional[AVLNode[Key]], key: Key
    ) -> tuple[AVLNode[Key], bool]:
        if node is None:
            return AVLNode(key), True

        if key < node.key:
            node.left, inserted = cls._insert(node.left, key)
        elif key > node.key:
            node.right, inserted = cls._insert(node.right, key)
        else:
            return node, False

        return cls._rebalance(node), inserted

    def insert(self, key: Key) -> bool:
        """Вставляет ключ; возвращает False, если такой ключ уже был."""
        self._root, inserted = self._insert(self._root, key)
        if inserted:
            self._size += 1
        return inserted

    @classmethod
    def _delete(
        cls, node: Optional[AVLNode[Key]], key: Key
    ) -> tuple[Optional[AVLNode[Key]], bool]:
        if node is None:
            return None, False

        if key < node.key:
            node.left, deleted = cls._delete(node.left, key)
        elif key > node.key:
            node.right, deleted = cls._delete(node.right, key)
        else:
            deleted = True
            if node.left is None:
                return node.right, True
            if node.right is None:
                return node.left, True

            successor = node.right
            while successor.left is not None:
                successor = successor.left
            node.key = successor.key
            node.right, _ = cls._delete(node.right, successor.key)

        if not deleted:
            return node, False
        return cls._rebalance(node), True

    def delete(self, key: Key) -> bool:
        """Удаляет ключ; возвращает False, если ключ не найден."""
        self._root, deleted = self._delete(self._root, key)
        if deleted:
            self._size -= 1
        return deleted

    def search(self, key: Key) -> bool:
        """Возвращает True, если ключ находится в дереве."""
        current = self._root
        while current is not None:
            if key < current.key:
                current = current.left
            elif key > current.key:
                current = current.right
            else:
                return True
        return False

    def inorder(self) -> List[Key]:
        """Возвращает ключи по возрастанию."""
        return list(self)

    def __iter__(self) -> Iterator[Key]:
        def traverse(node: Optional[AVLNode[Key]]) -> Iterator[Key]:
            if node is not None:
                yield from traverse(node.left)
                yield node.key
                yield from traverse(node.right)

        return traverse(self._root)

    def to_ascii(self) -> str:
        """Строит компактную текстовую визуализацию дерева."""
        if self._root is None:
            return "<empty>"

        lines = [str(self._root.key)]

        def add_children(node: AVLNode[Key], prefix: str) -> None:
            children = [
                (label, child)
                for label, child in (("L", node.left), ("R", node.right))
                if child is not None
            ]
            for index, (label, child) in enumerate(children):
                is_last = index == len(children) - 1
                connector = "`-- " if is_last else "|-- "
                lines.append(f"{prefix}{connector}{label}: {child.key}")
                child_prefix = prefix + ("    " if is_last else "|   ")
                add_children(child, child_prefix)

        add_children(self._root, "")
        return "\n".join(lines)

    @property
    def root(self) -> Optional[AVLNode[Key]]:
        return self._root

    @property
    def height(self) -> int:
        return self._height(self._root)

    def __len__(self) -> int:
        return self._size

    def __contains__(self, key: object) -> bool:
        return self.search(key)  # type: ignore[arg-type]


def main() -> None:
    tree: AVL[int] = AVL()
    for value in (30, 20, 10, 25, 40, 50):
        tree.insert(value)
        print(f"После вставки {value}:")
        print(tree.to_ascii(), "\n")

    tree.delete(20)
    print("После удаления 20:")
    print(tree.to_ascii())


if __name__ == "__main__":
    main()
