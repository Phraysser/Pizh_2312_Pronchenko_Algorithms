from __future__ import annotations
from typing import Optional, List
from binary_search_tree import TreeNode

def inorder_recursive(node: Optional[TreeNode], res: List[int]) -> None:
    """Рекурсивный in-order обход: O(n) по времени и O(h) по памяти (стек вызовов)."""
    if node is None:
        return
    inorder_recursive(node.left, res)
    res.append(node.key)
    inorder_recursive(node.right, res)

def preorder_recursive(node: Optional[TreeNode], res: List[int]) -> None:
    """Рекурсивный pre-order обход: O(n) по времени и O(h) по памяти."""
    if node is None:
        return
    res.append(node.key)
    preorder_recursive(node.left, res)
    preorder_recursive(node.right, res)

def postorder_recursive(node: Optional[TreeNode], res: List[int]) -> None:
    """Рекурсивный post-order обход: O(n) по времени и O(h) по памяти."""
    if node is None:
        return
    postorder_recursive(node.left, res)
    postorder_recursive(node.right, res)
    res.append(node.key)

def inorder_iterative(root: Optional[TreeNode]) -> List[int]:
    """Итеративный in-order обход с использованием явного стека.
    Временная сложность: O(n), память O(h).
    """
    res: List[int] = []
    stack: List[TreeNode] = []
    node = root
    while stack or node:
        while node:
            stack.append(node)
            node = node.left
        node = stack.pop()
        res.append(node.key)
        node = node.right
    return res