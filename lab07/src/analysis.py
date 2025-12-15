"""
Модуль экспериментального анализа производительности.
"""
import timeit
import random
import matplotlib.pyplot as plt
from heap import MinHeap
from heapsort import heapsort_inplace

# Характеристики ПК (Заполнить своими данными)
PC_INFO = """
Характеристики ПК для тестирования:
- Процессор: Intel Core i3-10110U @ 2.60GHz
- Оперативная память: 8 GB DDR4
- ОС: Windows 11
- Python: 3.13.2
"""


def measure_build_heap():
    """Сравнение последовательной вставки и алгоритма build_heap."""
    sizes = [1000, 5000, 10000, 20000, 50000]
    times_insert = []
    times_build = []

    print("\n--- Сравнение методов построения кучи ---")
    print(f"{'Size':<10} | {'Insert (ms)':<15} | {'Build (ms)':<15}")

    for size in sizes:
        data = [random.randint(0, 100000) for _ in range(size)]

        # 1. Последовательная вставка (O(N log N))
        def test_insert():
            h = MinHeap()
            for item in data:
                h.insert(item)

        t_ins = timeit.timeit(test_insert, number=5) / 5 * 1000
        times_insert.append(t_ins)

        # 2. Build Heap (O(N))
        def test_build():
            h = MinHeap()
            h.build_heap(data)

        t_build = timeit.timeit(test_build, number=5) / 5 * 1000
        times_build.append(t_build)

        print(f"{size:<10} | {t_ins:<15.4f} | {t_build:<15.4f}")

    # Построение графика
    plt.figure(figsize=(10, 6))
    plt.plot(sizes, times_insert, 'r-o', label='Sequential Insert O(N log N)')
    plt.plot(sizes, times_build, 'g-o', label='Build Heap O(N)')
    plt.title('Сравнение методов построения кучи')
    plt.xlabel('Количество элементов (N)')
    plt.ylabel('Время (мс)')
    plt.legend()
    plt.grid(True)
    try:
        plt.savefig('build_heap_comparison.png')
        print("График сохранен как build_heap_comparison.png")
    except Exception as e:
        print(f"Ошибка сохранения графика: {e}")


def measure_sorting():
    """Сравнение Heapsort, QuickSort (sorted) и MergeSort."""
    sizes = [1000, 5000, 10000, 20000, 50000]
    times_heapsort = []
    times_python_sort = []  # Timsort (оптимизированный MergeSort)

    print("\n--- Сравнение сортировок ---")
    print(f"{'Size':<10} | {'Heapsort (ms)':<15} | {'Python Sort (ms)':<15}")

    for size in sizes:
        data = [random.randint(0, 100000) for _ in range(size)]
        data_copy = data[:]

        # 1. Heapsort In-place (O(N log N))
        t_heap = timeit.timeit(
            lambda: heapsort_inplace(data[:]), number=5
        ) / 5 * 1000
        times_heapsort.append(t_heap)

        # 2. Python Sorted (Timsort - O(N log N), highly optimized C)
        t_py = timeit.timeit(
            lambda: sorted(data_copy), number=5
        ) / 5 * 1000
        times_python_sort.append(t_py)

        print(f"{size:<10} | {t_heap:<15.4f} | {t_py:<15.4f}")

    plt.figure(figsize=(10, 6))
    plt.plot(sizes, times_heapsort, 'b-o', label='Heapsort O(N log N)')
    plt.plot(sizes, times_python_sort, 'm-o', label='Python Sort (Timsort)')
    plt.title('Сравнение сортировок')
    plt.xlabel('Количество элементов (N)')
    plt.ylabel('Время (мс)')
    plt.legend()
    plt.grid(True)
    try:
        plt.savefig('sorting_comparison.png')
        print("График сохранен как sorting_comparison.png")
    except Exception as e:
        print(f"Ошибка сохранения графика: {e}")


def visualize_heap_structure():
    """Визуализация структуры небольшой кучи."""
    print("\n--- Визуализация дерева кучи ---")
    h = MinHeap()
    data = [10, 5, 20, 1, 3, 25, 100, 0]
    h.build_heap(data)
    print(f"Исходные данные (после build_heap): {h.heap}")
    h.print_tree()


if __name__ == "__main__":
    print(PC_INFO)
    visualize_heap_structure()
    measure_build_heap()
    measure_sorting()