"""
Модуль реализации жадных алгоритмов.
Включает:
1. Выбор заявок (Interval Scheduling).
2. Непрерывный рюкзак (Fractional Knapsack).
3. Кодирование Хаффмана (Huffman Coding).
"""
import heapq
from collections import Counter, namedtuple


# --- 1. Задача о выборе заявок (Interval Scheduling) ---

def interval_scheduling(intervals):
    """
    Выбирает максимальное количество непересекающихся интервалов.
    """
    # Сортируем по времени окончания (end)
    sorted_intervals = sorted(intervals, key=lambda x: x[1])  # O(N log N) - Timsort

    selected = []  # O(1) - создание списка
    last_finish_time = -1  # O(1) - инициализация

    for interval in sorted_intervals:  # O(N) - проход по всем интервалам
        start, end = interval  # O(1) - распаковка
        if start >= last_finish_time:  # O(1) - сравнение
            selected.append(interval)  # O(1) - добавление в список
            last_finish_time = end  # O(1) - обновление времени

    return selected  # O(1) - возврат результата
    # Общая сложность: O(N log N) + O(N) * O(1) = O(N log N)


# --- 2. Задача о непрерывном рюкзаке (Fractional Knapsack) ---

Item = namedtuple('Item', ['weight', 'value'])

def fractional_knapsack(items, capacity):
    """
    Решает задачу о непрерывном рюкзаке.
    """
    # Сортируем по удельной стоимости (v/w) по убыванию
    sorted_items = sorted(
        items, 
        key=lambda x: x.value / x.weight, 
        reverse=True
    )  # O(N log N) - сортировка

    total_value = 0.0  # O(1)
    current_weight = 0.0  # O(1)
    fractions = []  # O(1)

    for item in sorted_items:  # O(N) - итерация по предметам
        if current_weight == capacity:  # O(1) - проверка заполненности
            break  # O(1)

        if current_weight + item.weight <= capacity:  # O(1) - влезает ли целиком
            current_weight += item.weight  # O(1)
            total_value += item.value  # O(1)
            fractions.append((item, 1.0))  # O(1) - append
        else:
            # Берем часть предмета
            remain = capacity - current_weight  # O(1)
            fraction = remain / item.weight  # O(1)
            total_value += item.value * fraction  # O(1)
            current_weight += remain  # O(1)
            fractions.append((item, fraction))  # O(1)
            break  # O(1) - рюкзак полон, выход

    return total_value, fractions  # O(1)
    # Общая сложность: O(N log N) + O(N) = O(N log N)


# --- 3. Код Хаффмана (Huffman Coding) ---

class HuffmanNode:
    """Узел дерева Хаффмана."""
    def __init__(self, char, freq):
        self.char = char  # O(1)
        self.freq = freq  # O(1)
        self.left = None  # O(1)
        self.right = None  # O(1)

    def __lt__(self, other):
        return self.freq < other.freq  # O(1) - сравнение для кучи

def build_huffman_tree(text):
    """
    Строит дерево Хаффмана.
    N - длина текста, K - количество уникальных символов (размер алфавита).
    """
    if not text:  # O(1)
        return None  # O(1)

    frequency = Counter(text)  # O(N) - проход по тексту для подсчета

    # Создание списка узлов
    heap = [HuffmanNode(char, freq) for char, freq in frequency.items()]  # O(K)
    heapq.heapify(heap)  # O(K) - построение кучи из массива

    while len(heap) > 1:  # O(K) - цикл выполняется K-1 раз
        node1 = heapq.heappop(heap)  # O(log K) - извлечение минимума
        node2 = heapq.heappop(heap)  # O(log K) - извлечение второго минимума

        merged = HuffmanNode(None, node1.freq + node2.freq)  # O(1)
        merged.left = node1  # O(1)
        merged.right = node2  # O(1)

        heapq.heappush(heap, merged)  # O(log K) - вставка нового узла

    return heap[0]  # O(1) - корень дерева
    # Общая сложность: O(N) + O(K) + O(K * log K) = O(N + K log K).
    # Обычно K (алфавит) << N (текст), поэтому можно считать O(N).

def generate_huffman_codes(node, prefix="", code_map=None):
    """
    Рекурсивный обход дерева для генерации кодов.
    K - количество узлов в дереве (2*unique_chars - 1).
    """
    if code_map is None:  # O(1)
        code_map = {}  # O(1)

    if node is not None:  # O(1)
        if node.char is not None:  # O(1) - это лист
            code_map[node.char] = prefix if prefix else "0"  # O(1)
        else:
            # Рекурсивные вызовы
            generate_huffman_codes(node.left, prefix + "0", code_map)  # T(n/2)
            generate_huffman_codes(node.right, prefix + "1", code_map)  # T(n/2)
            
    return code_map  # O(1)
    # Общая сложность: O(K) - посещаем каждый узел один раз.

def huffman_encoding(text):
    """Обертка для кодирования текста."""
    root = build_huffman_tree(text)  # O(N + K log K)
    codes = generate_huffman_codes(root)  # O(K)
    
    # Генерация закодированной строки
    encoded_text = "".join([codes[char] for char in text])  # O(N) - проход по тексту
    
    return encoded_text, codes, root  # O(1)
    # Общая сложность: O(N + K log K) + O(K) + O(N) = O(N)