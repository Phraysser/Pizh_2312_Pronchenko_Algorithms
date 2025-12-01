from __future__ import annotations
from typing import Optional, Any, List


class TreeNode:
    """
    Узел дерева.
    """
    def __init__(self, key: int) -> None:
        self.key: int = key  # O(1)
        self.left: Optional[TreeNode] = None  # O(1)
        self.right: Optional[TreeNode] = None  # O(1)

    def __repr__(self) -> str:
        return f"TreeNode({self.key})"  # O(1)


class BinarySearchTree:
    """
    Бинарное дерево поиска (BST).
    Все публичные методы документированы с указанием временной сложности.
    """
    def __init__(self) -> None:
        self.root: Optional[TreeNode] = None  # O(1)

    # ------------------ Insert ------------------
    def insert(self, key: int) -> None:
        """Вставка ключа в BST.
        Средняя сложность: O(log n), худшая (вырожденное дерево): O(n).
        """
        if self.root is None:  # O(1)
            self.root = TreeNode(key)  # O(1)
            return
        node = self.root  # O(1)
        while True:  # цикл по высоте дерева -> O(h) = O(log n) avg, O(n) worst
            if key < node.key:  # O(1)
                if node.left is None:  # O(1)
                    node.left = TreeNode(key)  # O(1)
                    return
                node = node.left  # O(1)
            else:
                if node.right is None:  # O(1)
                    node.right = TreeNode(key)  # O(1)
                    return
                node = node.right  # O(1)

    # ------------------ Search ------------------
    def search(self, key: int) -> Optional[TreeNode]:
        """Поиск узла по ключу.
        Средняя: O(log n), худшая: O(n).
        """
        node = self.root  # O(1)
        while node is not None:  # O(h)
            if key == node.key:  # O(1)
                return node  # O(1)
            node = node.left if key < node.key else node.right  # O(1)
        return None  # O(1)

    # ------------------ Find min/max ------------------
    def find_min(self, node: Optional[TreeNode]) -> Optional[TreeNode]:
        """Найти минимум в поддереве. Сложность: O(h) -> O(n) worst, O(log n) avg."""
        if node is None:  # O(1)
            return None
        while node.left is not None:  # O(h)
            node = node.left  # O(1)
        return node  # O(1)

    def find_max(self, node: Optional[TreeNode]) -> Optional[TreeNode]:
        """Найти максимум в поддереве. Сложность: O(h)."""
        if node is None:
            return None
        while node.right is not None:
            node = node.right
        return node

    # ------------------ Delete ------------------
    def delete(self, key: int) -> None:
        """Удаление узла с ключом key. Сложность: O(h) -> O(log n) avg, O(n) worst."""
        self.root = self._delete_rec(self.root, key)  # O(h)

    def _delete_rec(self, node: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        """Вспомогательная рекурсивная функция удаления. Сложность O(h)."""
        if node is None:  # O(1)
            return None
        if key < node.key:  # O(1)
            node.left = self._delete_rec(node.left, key)  # O(h)
        elif key > node.key:  # O(1)
            node.right = self._delete_rec(node.right, key)  # O(h)
        else:
            # найден узел для удаления
            if node.left is None and node.right is None:  # лист - O(1)
                return None  # O(1)
            if node.left is None:  # только правый потомок - O(1)
                return node.right  # O(1)
            if node.right is None:  # только левый потомок - O(1)
                return node.left  # O(1)
            # два ребёнка: найти преемника (min в правом поддереве)
            succ = self.find_min(node.right)  # O(h)
            assert succ is not None
            node.key = succ.key  # замена значения - O(1)
            node.right = self._delete_rec(node.right, succ.key)  # удалить преемника - O(h)
        return node  # O(1)

    def inorder(self) -> List[int]:
        """Рекурсивный in-order traversal: O(n)."""
        res: List[int] = []

        def _in(n: Optional[TreeNode]) -> None:
            if n is None:
                return
            _in(n.left)  # O(size left)
            res.append(n.key)  # O(1)
            _in(n.right)  # O(size right)

        _in(self.root)  # O(n)
        return res  # O(1)

    def preorder(self) -> List[int]:
        """Рекурсивный pre-order traversal: O(n)."""
        res: List[int] = []

        def _pre(n: Optional[TreeNode]) -> None:
            if n is None:
                return
            res.append(n.key)
            _pre(n.left)
            _pre(n.right)

        _pre(self.root)
        return res

    def postorder(self) -> List[int]:
        """Рекурсивный post-order traversal: O(n)."""
        res: List[int] = []

        def _post(n: Optional[TreeNode]) -> None:
            if n is None:
                return
            _post(n.left)
            _post(n.right)
            res.append(n.key)

        _post(self.root)
        return res

    # ------------------ Iterative in-order ------------------
    def inorder_iterative(self) -> List[int]:
        """Итеративный in-order обход с явным стеком. Сложность O(n), память O(h)."""
        res: List[int] = []
        stack: List[TreeNode] = []
        node = self.root
        while stack or node:
            while node:
                stack.append(node)  # O(1) per push
                node = node.left
            node = stack.pop()  # O(1)
            res.append(node.key)  # O(1)
            node = node.right
        return res

    def height(self, node: Optional[TreeNode] = None) -> int:
        """Высота поддерева: O(n) (посещает все узлы в худшем случае)."""
        if node is None:
            node = self.root
        def _h(n: Optional[TreeNode]) -> int:
            if n is None:
                return 0
            left_h = _h(n.left)
            right_h = _h(n.right)
            return 1 + max(left_h, right_h)
        return _h(node)

    def is_valid_bst(self) -> bool:
        """Проверка корректности BST: O(n)."""
        def _check(node: Optional[TreeNode], low: Any, high: Any) -> bool:
            if node is None:
                return True
            if not (low < node.key < high):
                return False
            return _check(node.left, low, node.key) and _check(node.right, node.key, high)
        import math
        return _check(self.root, -math.inf, math.inf)

    def text_visualize(self) -> str:
        """Текстовая визуализация (отступы). Сложность O(n)."""
        lines: List[str] = []
        def _viz(n: Optional[TreeNode], depth: int) -> None:
            if n is None:
                return
            _viz(n.right, depth + 1)
            lines.append("    " * depth + str(n.key))
            _viz(n.left, depth + 1)
        _viz(self.root, 0)
        return "\n".join(lines)

    def build_from_list(self, values: List[int]) -> None:
        """Поэлементная вставка из списка. Сложность: O(n*h) общей — зависит от порядка."""
        for v in values:
            self.insert(v)