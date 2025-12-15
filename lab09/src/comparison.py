"""
Модуль сравнительного анализа алгоритмов ДП.
"""
import timeit
import random
import matplotlib.pyplot as plt
import sys
from dynamic_programming import (
    fib_recursive, fib_memo, fib_tabulation,
    knapsack_01
)

# Увеличиваем лимит рекурсии для тестов
sys.setrecursionlimit(20000)

def compare_fibonacci():
    """Сравнение времени выполнения подходов к числам Фибоначчи."""
    # Для рекурсии берем маленькие n, иначе зависнет
    ns_small = [10, 15, 20, 25, 30, 35]
    times_rec = []
    times_memo_small = []
    
    print("\n--- Фибоначчи: Наивная рекурсия vs ДП ---")
    for n in ns_small:
        t_rec = timeit.timeit(lambda: fib_recursive(n), number=3) / 3 * 1000
        t_memo = timeit.timeit(lambda: fib_memo(n, {}), number=100) / 100 * 1000
        times_rec.append(t_rec)
        times_memo_small.append(t_memo)
        print(f"N={n:<3} | Rec: {t_rec:>8.4f} ms | Memo: {t_memo:>8.4f} ms")

    # Для ДП берем большие n
    ns_large = [100, 500, 1000, 2000, 5000]
    times_memo = []
    times_tab = []
    
    print("\n--- Фибоначчи: Мемоизация vs Табуляция (Большие N) ---")
    for n in ns_large:
        t_memo = timeit.timeit(lambda: fib_memo(n, {}), number=100) / 100 * 1000
        t_tab = timeit.timeit(lambda: fib_tabulation(n), number=100) / 100 * 1000
        times_memo.append(t_memo)
        times_tab.append(t_tab)
        print(f"N={n:<4} | Memo: {t_memo:>8.4f} ms | Tab: {t_tab:>8.4f} ms")

    # График 1: Рекурсия vs ДП
    plt.figure(figsize=(10, 5))
    plt.plot(ns_small, times_rec, 'r-o', label='Naive Recursive O(2^n)')
    plt.plot(ns_small, times_memo_small, 'g-o', label='DP Memoization O(n)')
    plt.title('Фибоначчи: Экспоненциальный рост рекурсии')
    plt.xlabel('N')
    plt.ylabel('Время (мс)')
    plt.legend()
    plt.grid(True)
    plt.savefig('fib_recursion_vs_dp.png')

    # График 2: Memo vs Tabulation
    plt.figure(figsize=(10, 5))
    plt.plot(ns_large, times_memo, 'g-o', label='Top-Down (Memo)')
    plt.plot(ns_large, times_tab, 'b-o', label='Bottom-Up (Tabulation)')
    plt.title('Фибоначчи: Сравнение методов ДП')
    plt.xlabel('N')
    plt.ylabel('Время (мс)')
    plt.legend()
    plt.grid(True)
    plt.savefig('fib_dp_methods.png')


def analyze_knapsack_greedy_vs_dp():
    """
    Сравнение корректности: Жадный (по удельной цене) vs ДП для задачи 0-1.
    Жадный алгоритм для 0-1 рюкзака часто дает неоптимальный результат.
    """
    print("\n--- Рюкзак 0-1: Проверка оптимальности ДП vs Жадный ---")
    
    # Пример (как в лекции):
    # W=50. Items: (10, 60), (20, 100), (30, 120).
    # Уд. цены: 6, 5, 4.
    capacity = 50
    items = [(10, 60), (20, 100), (30, 120)]
    
    # 1. Жадный подход (имитация для 0-1)
    # Берем самый "плотный" (10, 60). Ост. 40.
    # Берем следующий (20, 100). Ост. 20.
    # Следующий (30, 120) не лезет.
    # Итог жадного: 160.
    
    # 2. ДП решение
    dp_val, selected = knapsack_01(items, capacity, visualize=True)
    
    print(f"Предметы: {items}")
    print(f"Вместимость: {capacity}")
    print(f"Жадный результат (эвристика): 160 (10+20кг)")
    print(f"ДП результат (оптимальный): {dp_val} (выбрано: {selected})")
    
    if dp_val > 160:
        print("ВЫВОД: ДП нашел лучшее решение, чем жадный алгоритм!")
    else:
        print("В данном случае решения совпали.")

if __name__ == "__main__":
    compare_fibonacci()
    analyze_knapsack_greedy_vs_dp()