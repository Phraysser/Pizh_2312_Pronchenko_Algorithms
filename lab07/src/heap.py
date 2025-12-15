"""
Модуль реализации структуры данных MinHeap (Куча).
"""
import math


class MinHeap:
    """
    Реализация Min-Heap на основе динамического массива.
    Свойство кучи: значение в любом узле меньше или равно значениям его потомков.
    """

    def __init__(self):
        """Инициализация пустой кучи."""
        self.heap = []  # O(1) - создание пустого списка

    def _sift_up(self, index):
        """
        Всплытие элемента (sift-up).
        Поднимает элемент вверх, пока выполняется условие кучи.
        """
        while index > 0:  # O(log N) - в худшем случае проход от листа до корня
            parent_index = (index - 1) // 2  # O(1) - вычисление индекса родителя

            # Сравниваем элемент с родителем
            if self.heap[index] < self.heap[parent_index]:  # O(1) - сравнение
                # Меняем местами с родителем
                self.heap[index], self.heap[parent_index] = (
                    self.heap[parent_index],
                    self.heap[index],
                )  # O(1) - обмен элементов
                index = parent_index  # O(1) - переход на уровень выше
            else:
                break  # O(1) - условие кучи выполнено

    def _sift_down(self, index):
        """
        Погружение элемента (sift-down).
        Опускает элемент вниз, пока выполняется условие кучи.
        """
        size = len(self.heap)  # O(1)
        while True:  # O(log N) - в худшем случае спуск от корня до листа
            left_child = 2 * index + 1  # O(1)
            right_child = 2 * index + 2  # O(1)
            smallest = index  # O(1)

            # Проверяем левого потомка
            if (left_child < size and
                    self.heap[left_child] < self.heap[smallest]):  # O(1)
                smallest = left_child  # O(1)

            # Проверяем правого потомка
            if (right_child < size and
                    self.heap[right_child] < self.heap[smallest]):  # O(1)
                smallest = right_child  # O(1)

            # Если элемент больше одного из потомков, меняем местами
            if smallest != index:  # O(1)
                self.heap[index], self.heap[smallest] = (
                    self.heap[smallest],
                    self.heap[index],
                )  # O(1) - обмен
                index = smallest  # O(1) - переход на уровень ниже
            else:
                break  # O(1) - позиция найдена

    def insert(self, value):
        """
        Вставка нового элемента в кучу.
        """
        self.heap.append(value)  # O(1) - добавление в конец массива
        self._sift_up(len(self.heap) - 1)  # O(log N) - восстановление свойства
        # Общая сложность: O(log N)

    def extract(self):
        """
        Извлечение минимального элемента (корня).
        """
        if not self.heap:
            raise IndexError("Куча пуста")  # O(1)

        min_val = self.heap[0]  # O(1) - запоминаем корень
        last_val = self.heap.pop()  # O(1) - удаляем последний элемент

        if self.heap:  # Если куча не стала пустой
            self.heap[0] = last_val  # O(1) - ставим последний элемент в корень
            self._sift_down(0)  # O(log N) - восстанавливаем свойство кучи

        return min_val  # O(1)
        # Общая сложность: O(log N)

    def peek(self):
        """
        Просмотр минимального элемента без удаления.
        """
        if not self.heap:
            return None  # O(1)
        return self.heap[0]  # O(1)

    def build_heap(self, array):
        """
        Построение кучи из произвольного массива.
        """
        self.heap = array[:]  # O(N) - копирование массива
        # Начинаем с последнего родителя и идем до корня
        # Индекс последнего родителя: (n // 2) - 1
        for i in range((len(self.heap) // 2) - 1, -1, -1):  # O(N) итераций
            self._sift_down(i)  # Сложность меняется от высоты, сумма дает O(N)
        # Общая сложность: O(N)

    def print_tree(self):
        """
        Текстовая визуализация дерева кучи (вспомогательный метод).
        """
        if not self.heap:
            print("(Empty heap)")
            return

        h = int(math.log2(len(self.heap))) + 1
        for i in range(h):
            items_on_level = 2**i
            start_index = 2**i - 1
            end_index = start_index + items_on_level
            level_items = self.heap[start_index:end_index]
            spacing = " " * (2 ** (h - i + 1))
            print(spacing.join(map(str, level_items)).center(80))