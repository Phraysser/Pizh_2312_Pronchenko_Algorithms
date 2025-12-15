"""
Модуль алгоритмов сортировки кучей (Heapsort).
"""
from heap import MinHeap


def heapsort(array):
    """
    Сортировка с использованием класса MinHeap.
    Создает новый отсортированный массив.
    """
    heap = MinHeap()  # O(1)
    heap.build_heap(array)  # O(N) - построение кучи

    sorted_array = []  # O(1)
    # Извлекаем элементы по одному. В MinHeap корень - минимум.
    while heap.peek() is not None:  # N итераций
        val = heap.extract()  # O(log N)
        sorted_array.append(val)  # O(1)

    return sorted_array
    # Общая сложность: O(N) + N * O(log N) = O(N log N)


def heapsort_inplace(array):
    """
    In-place сортировка кучей (без выделения доп. памяти под кучу).
    """
    n = len(array)  # O(1)

    # Внутренняя функция просеивания для Max-Heap
    def sift_down_max(n_size, i):
        largest = i  # O(1)
        left = 2 * i + 1  # O(1)
        right = 2 * i + 2  # O(1)

        # Ищем максимум среди родителя и детей
        if left < n_size and array[left] > array[largest]:  # O(1)
            largest = left
        if right < n_size and array[right] > array[largest]:  # O(1)
            largest = right

        if largest != i:
            array[i], array[largest] = array[largest], array[i]  # O(1) swap
            sift_down_max(n_size, largest)  # O(log N) рекурсивный вызов

    # 1. Построение Max-Heap
    # Идем от середины к началу
    for i in range(n // 2 - 1, -1, -1):  # O(N) итераций
        sift_down_max(n, i)
    # Сложность этапа 1: O(N)

    # 2. Сортировка (извлечение элементов)
    for i in range(n - 1, 0, -1):  # N итераций
        # Текущий корень (максимум) отправляем в конец неотсортированной части
        array[i], array[0] = array[0], array[i]  # O(1)
        # Восстанавливаем свойство кучи для уменьшенного размера i
        sift_down_max(i, 0)  # O(log N)
    # Сложность этапа 2: O(N log N)

    return array
    # Общая сложность: O(N log N)