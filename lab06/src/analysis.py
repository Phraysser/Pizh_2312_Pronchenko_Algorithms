from __future__ import annotations
import random
import timeit
import matplotlib.pyplot as plt
from binary_search_tree import BinarySearchTree
import platform
from typing import List, Dict

def pc_info() -> str:
    """Вывод информации о ПК. Заполнить CPU и RAM для метода проверки."""
    info = (
        f"Platform: {platform.platform()}\n"
        f"CPU info: Intel(R) Core(TM) i3-1110U\n"
        f"RAM: 8GB\n"
        f"Python: {platform.python_version()}\n"
    )
    return info

def build_balanced_sequence(n: int) -> List[int]:
    """Возвращает последовательность, приближающую баланс дерева.
    Использует рекурсивный выбор медианы.
    Временная сложность: O(n)
    """
    def seq(arr: List[int]) -> List[int]:
        if not arr:
            return []
        mid = len(arr) // 2
        return [arr[mid]] + seq(arr[:mid]) + seq(arr[mid+1:])
    return seq(list(range(1, n+1)))

def run_search_benchmark(sizes: List[int] = [1000, 2000, 5000, 10000]) -> Dict[str, List[float]]:
    """Замер времени поиска в сбалансированном и вырожденном BST.
    Возвращает словарь с результатами поиска для каждого размера дерева.
    """
    results: Dict[str, List[float]] = {'balanced': [], 'degenerate': []}
    for n in sizes:
        # Сбалансированное дерево
        bst_b = BinarySearchTree()
        vals_b = build_balanced_sequence(n)
        for v in vals_b:
            bst_b.insert(v)

        # Вырожденное дерево (вставка по возрастанию)
        bst_d = BinarySearchTree()
        vals_d = list(range(1, n+1))
        for v in vals_d:
            bst_d.insert(v)

        # Случайные цели поиска
        targets = [random.randint(1, n) for _ in range(1000)]

        def bench(tree: BinarySearchTree, targets: List[int]):
            def run() -> None:
                for t in targets:
                    tree.search(t)
            return run

        # Измеряем время
        t_b = timeit.timeit(bench(bst_b, targets), number=5) / 5 * 1000  # ms
        t_d = timeit.timeit(bench(bst_d, targets), number=5) / 5 * 1000  # ms
        results['balanced'].append(t_b)
        results['degenerate'].append(t_d)

    # Построение графика
    plt.figure(figsize=(8, 5))
    plt.plot(sizes, results['balanced'], marker='o', label='balanced')
    plt.plot(sizes, results['degenerate'], marker='o', label='degenerate')
    plt.xlabel('n (size)')
    plt.ylabel('Search time per 1000 searches (ms)')
    plt.title('BST search: balanced vs degenerate')
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)
    plt.legend()
    plt.savefig('bst_search_comparison.png', dpi=300, bbox_inches='tight')
    plt.show()

    return results

if __name__ == "__main__":
    print("PC info:\n", pc_info())
    sizes = [1000, 2000, 5000, 10000]
    res = run_search_benchmark(sizes)
    print(res)