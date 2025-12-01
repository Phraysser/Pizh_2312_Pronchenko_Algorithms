from __future__ import annotations
from binary_search_tree import BinarySearchTree

def test_insert_and_search() -> None:
    """Проверка вставки и поиска в BST."""
    bst = BinarySearchTree()
    for v in [5, 3, 7, 2, 4, 6, 8]:
        bst.insert(v)
    assert bst.search(4) is not None
    assert bst.search(10) is None
    assert bst.inorder() == [2,3,4,5,6,7,8]

def test_delete_leaf() -> None:
    """Удаление листа."""
    bst = BinarySearchTree()
    for v in [5,3,7]:
        bst.insert(v)
    bst.delete(3)
    assert bst.inorder() == [5,7]

def test_delete_node_with_one_child() -> None:
    """Удаление узла с одним ребенком."""
    bst = BinarySearchTree()
    for v in [5,3,7,2]:
        bst.insert(v)
    bst.delete(3)
    assert bst.inorder() == [2,5,7]

def test_delete_node_with_two_children() -> None:
    """Удаление узла с двумя детьми."""
    bst = BinarySearchTree()
    for v in [5,3,7,2,4,6,8]:
        bst.insert(v)
    bst.delete(3)
    assert bst.inorder() == [2,4,5,6,7,8]

def test_find_min_max_height_is_valid() -> None:
    """Проверка min/max, высоты и корректности BST."""
    bst = BinarySearchTree()
    for v in [5,3,7,2,4]:
        bst.insert(v)
    assert bst.find_min(bst.root).key == 2
    assert bst.find_max(bst.root).key == 7
    assert bst.height() == 3
    assert bst.is_valid_bst() is True