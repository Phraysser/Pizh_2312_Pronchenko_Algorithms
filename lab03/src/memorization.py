import time
from functools import lru_cache
from typing import Callable, List

import matplotlib.pyplot as plt


# Глобальные счетчики вызовов
naive_call_counter: int = 0
memo_call_counter: int = 0


def fibonacci_recursive(n: int) -> int:
    """
    Наивная рекурсивная реализация Фибоначчи.

    Сложность: время O(phi^n), память (стек) O(n).
    """
    global naive_call_counter
    naive_call_counter += 1
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


@lru_cache(maxsize=None)
def fibonacci_cached(n: int) -> int:
    """
    Рекурсивная реализация Фибоначчи с мемоизацией (LRU-кеш).

    Сложность: время O(n), память O(n) (кеш + стек).
    """
    global memo_call_counter
    memo_call_counter += 1
    if n <= 1:
        return n
    return fibonacci_cached(n - 1) + fibonacci_cached(n - 2)


def measure_execution_time(
    func: Callable[[int], int],
    value: int,
    repetitions: int = 1
) -> float:
    """
    Возвращает среднее время выполнения func(value) в секундах.

    Очистка кеша (если есть) выполняется перед запуском.
    """
    clear_cache = getattr(func, "cache_clear", None)
    if callable(clear_cache):
        clear_cache()

    execution_times: List[float] = []
    for _ in range(max(1, repetitions)):
        start_time = time.perf_counter()
        func(value)
        end_time = time.perf_counter()
        execution_times.append(end_time - start_time)
    return sum(execution_times) / len(execution_times)


def plot_execution_times(
    values: List[int],
    recursive_times: List[float],
    cached_times: List[float],
    filename: str
) -> None:
    """Строит и сохраняет график времени (сек)."""
    plt.figure(figsize=(8, 5))
    plt.plot(values, recursive_times, marker="o", label="Наивная рекурсия")
    plt.plot(values, cached_times, marker="s", label="Мемоизация (lru_cache)")
    plt.title("Сравнение времени вычисления чисел Фибоначчи")
    plt.xlabel("n")
    plt.ylabel("Время (сек)")
    plt.grid(True, linestyle="--", linewidth=0.5)
    plt.legend()
    plt.savefig(filename, dpi=300, bbox_inches="tight")
    plt.show()
    plt.close()


def main() -> None:
    """Запускает эксперимент и сохраняет результаты."""
    test_values: List[int] = list(range(5, 36, 5))
    recursive_times: List[float] = []
    cached_times: List[float] = []
    recursive_calls: List[int] = []
    cached_calls: List[int] = []

    for n_val in test_values:
        # Сбрасываем счетчики
        global naive_call_counter, memo_call_counter
        naive_call_counter = 0
        memo_call_counter = 0

        # Наивная версия (внимание: для n > ~30 долго)
        time_recursive = measure_execution_time(fibonacci_recursive, n_val, 1)
        recursive_times.append(time_recursive)
        recursive_calls.append(naive_call_counter)

        # Мемоизированная версия (несколько прогонов для устойчивости)
        time_cached = measure_execution_time(fibonacci_cached, n_val, 3)
        cached_times.append(time_cached)
        cached_calls.append(memo_call_counter)

    # Печать результатов
    print(
        f"{'n':>3} | {'naive(s)':>10} | {'naive_calls':>11} |"
        f"{'memo(s)':>10} | {'memo_calls':>10}"
        )
    print("-" * 60)
    for i, n_val in enumerate(test_values):
        print(
            f"{n_val:3d} | {recursive_times[i]:10.6f} |"
            f"{recursive_calls[i]:11d} | "
            f"{cached_times[i]:10.6f} | {cached_calls[i]:10d}"
        )

    # Сохранение графика времени
    plot_execution_times(
        test_values,
        recursive_times,
        cached_times,
        "fib_time_comparison.png"
    )


if __name__ == "__main__":
    main()
