"""
Модуль анализа и сравнения алгоритмов.
Сравнивает Жадный подход vs Полный перебор для задачи о рюкзаке (0-1).
"""
import timeit
import random
import matplotlib.pyplot as plt
from itertools import combinations
from greedy_algorithms import interval_scheduling, fractional_knapsack, huffman_encoding, Item

# --- Вспомогательные функции для анализа ---

def knapsack_01_brute_force(items, capacity):
    """
    Полный перебор для задачи о рюкзаке 0-1 (предметы нельзя делить).
    Сложность: O(2^N) - очень медленно.
    """
    best_value = 0
    best_combination = []
    n = len(items)
    
    # Перебор всех возможных комбинаций (битмаска или itertools)
    for r in range(1, n + 1):
        for combo in combinations(items, r):
            weight = sum(i.weight for i in combo)
            value = sum(i.value for i in combo)
            if weight <= capacity and value > best_value:
                best_value = value
                best_combination = combo
                
    return best_value, best_combination

def knapsack_01_greedy(items, capacity):
    """
    Попытка применить жадный подход (по удельной стоимости) к задаче 0-1.
    Берем предмет целиком или не берем вообще.
    """
    # Сортируем по v/w
    sorted_items = sorted(items, key=lambda x: x.value / x.weight, reverse=True)
    total_value = 0
    current_weight = 0
    chosen_items = []
    
    for item in sorted_items:
        if current_weight + item.weight <= capacity:
            current_weight += item.weight
            total_value += item.value
            chosen_items.append(item)
            
    return total_value, chosen_items


def compare_greedy_vs_optimal():
    """
    Демонстрация того, что жадный алгоритм НЕ оптимален для дискретного рюкзака (0-1).
    """
    print("\n--- Сравнение Жадного подхода и Полного перебора (Рюкзак 0-1) ---")
    
    # Пример, где жадный алгоритм ошибается
    # Вместимость 50.
    # Предмет A: вес 10, цена 60 (уд. цена 6)
    # Предмет B: вес 20, цена 100 (уд. цена 5)
    # Предмет C: вес 30, цена 120 (уд. цена 4)
    capacity = 50
    items = [
        Item(10, 60),
        Item(20, 100),
        Item(30, 120)
    ]
    
    print(f"Вместимость: {capacity}")
    print("Предметы (вес, цена):", [(i.weight, i.value) for i in items])
    
    # 1. Жадный выбор (0-1)
    greedy_val, greedy_items = knapsack_01_greedy(items, capacity)
    print(f"\n[Жадный 0-1] Результат: {greedy_val}")
    print(f"Выбрано: {[(i.weight, i.value) for i in greedy_items]}")
    print("Логика: Взял (10, 60), потом (20, 100). Места осталось 20. (30, 120) не влез.")
    
    # 2. Оптимальный (Полный перебор)
    opt_val, opt_items = knapsack_01_brute_force(items, capacity)
    print(f"\n[Оптимальный] Результат: {opt_val}")
    print(f"Выбрано: {[(i.weight, i.value) for i in opt_items]}")
    print("Логика: Взял (20, 100) и (30, 120). Общий вес 50. Цена 220.")
    
    print(f"\nВывод: Жадный алгоритм ошибся на {opt_val - greedy_val} единиц стоимости.")


def measure_huffman_performance():
    """Замер производительности алгоритма Хаффмана."""
    sizes = [1000, 5000, 10000, 50000, 100000]
    times = []
    
    print("\n--- Замер производительности Хаффмана ---")
    for size in sizes:
        # Генерация случайного текста
        text = "".join(random.choices("abcdefghijklmnopqrstuvwxyz", k=size))
        
        t = timeit.timeit(lambda: huffman_encoding(text), number=10) / 10 * 1000
        times.append(t)
        print(f"Размер: {size:<10} | Время: {t:.4f} мс")
        
    plt.figure(figsize=(10, 6))
    plt.plot(sizes, times, 'g-o', label='Huffman Encoding O(N)')
    plt.title('Производительность алгоритма Хаффмана')
    plt.xlabel('Длина текста (символы)')
    plt.ylabel('Время (мс)')
    plt.legend()
    plt.grid(True)
    try:
        plt.savefig('huffman_performance.png')
        print("График сохранен как huffman_performance.png")
    except:
        pass

if __name__ == "__main__":
    compare_greedy_vs_optimal()
    measure_huffman_performance()