"""
Модуль реализации приоритетной очереди.
"""
from heap import MinHeap


class PriorityQueue:
    """
    Приоритетная очередь на основе MinHeap.
    item с наименьшим числом priority обслуживается первым.
    """

    def __init__(self):
        self.heap = MinHeap()  # O(1)

    def enqueue(self, item, priority):
        """
        Добавление элемента в очередь с приоритетом.
        :param item: Данные (задача)
        :param priority: Приоритет (число, чем меньше - тем важнее)
        """
        # Python сравнивает кортежи поэлементно: сначала priority, потом item
        self.heap.insert((priority, item))  # O(log N)

    def dequeue(self):
        """
        Извлечение элемента с наивысшим приоритетом (минимальным числом).
        """
        if self.heap.peek() is None:
            raise IndexError("Очередь пуста")  # O(1)

        # extract возвращает кортеж (priority, item)
        priority, item = self.heap.extract()  # O(log N)
        return item  # O(1)

    def peek(self):
        """
        Просмотр элемента с высшим приоритетом.
        """
        result = self.heap.peek()  # O(1)
        if result:
            return result[1]  # Возвращаем только данные (item)
        return None  # O(1)