"""
Модуль тестирования функциональности кучи и сортировок.
"""
import unittest
import random
from heap import MinHeap
from heapsort import heapsort, heapsort_inplace
from priority_queue import PriorityQueue


class TestHeapDataStructures(unittest.TestCase):

    def test_min_heap_operations(self):
        """Тест основных операций MinHeap (insert, extract)."""
        h = MinHeap()
        data = [10, 4, 15, 2, 20]
        for x in data:
            h.insert(x)

        # Ожидаемый порядок извлечения (сортировка): 2, 4, 10, 15, 20
        self.assertEqual(h.extract(), 2)
        self.assertEqual(h.extract(), 4)
        self.assertEqual(h.peek(), 10)  # Проверка peek
        self.assertEqual(h.extract(), 10)
        self.assertEqual(h.extract(), 15)
        self.assertEqual(h.extract(), 20)

    def test_build_heap(self):
        """Тест построения кучи из массива (O(N))."""
        h = MinHeap()
        arr = [9, 3, 7, 1, 5]
        h.build_heap(arr)
        # Корень должен быть минимальным (1)
        self.assertEqual(h.peek(), 1)
        # Проверяем, что это валидная куча, извлекая все элементы
        result = []
        while h.peek() is not None:
            result.append(h.extract())
        self.assertEqual(result, [1, 3, 5, 7, 9])

    def test_heapsort_class(self):
        """Тест внешней функции heapsort."""
        data = [random.randint(-100, 100) for _ in range(100)]
        sorted_data = heapsort(data)
        self.assertEqual(sorted_data, sorted(data))

    def test_heapsort_inplace(self):
        """Тест in-place сортировки."""
        data = [random.randint(-100, 100) for _ in range(100)]
        original_copy = data[:]
        heapsort_inplace(data)
        self.assertEqual(data, sorted(original_copy))

    def test_priority_queue(self):
        """Тест приоритетной очереди."""
        pq = PriorityQueue()
        # Добавляем задачи в разнобой
        pq.enqueue("task_low", 10)
        pq.enqueue("task_urgent", 1)
        pq.enqueue("task_normal", 5)

        # Должны выходить в порядке приоритета: 1 -> 5 -> 10
        self.assertEqual(pq.dequeue(), "task_urgent")
        self.assertEqual(pq.dequeue(), "task_normal")
        self.assertEqual(pq.dequeue(), "task_low")


if __name__ == '__main__':
    unittest.main()