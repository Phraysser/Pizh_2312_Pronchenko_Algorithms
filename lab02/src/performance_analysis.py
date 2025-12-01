"""Сравнение производительности list, LinkedList и deque."""
import timeit
from collections import deque
import matplotlib.pyplot as plt
from linked_list import SingleLinkedList


def measure_execution_time(func, *args, iterations: int = 1000) -> float:
    """Замер времени выполнения функции (среднее, мс)."""
    return timeit.timeit(lambda: func(*args),
                         number=iterations) * (1000 / iterations)


def compare_insert_beginning(sizes: list[int]) -> tuple[list[float],
                                                        list[float]]:
    """Сравнение вставки в начало: list vs SingleLinkedList."""
    list_results, linked_list_results = [], []
    for size in sizes:
        # Тестирование стандартного списка
        test_list: list[int] = []
        time_list = timeit.timeit(lambda: test_list.insert(0, 1),
                                  number=size) * 1000 / size
        list_results.append(time_list)

        # Тестирование связного списка
        linked_list = SingleLinkedList()
        time_linked = timeit.timeit(lambda: linked_list.add_to_beginning(1),
                                    number=size) * 1000 / size
        linked_list_results.append(time_linked)
    return list_results, linked_list_results


def compare_queue_operations(sizes: list[int]) -> tuple[list[float],
                                                        list[float]]:
    """Сравнение удаления из начала: list vs deque."""
    deque_results, list_pop_results = [], []
    for size in sizes:
        # Тестирование deque
        test_deque = deque(range(size))
        time_deque = timeit.timeit(lambda: test_deque.popleft(),
                                   number=size) * 1000 / size
        deque_results.append(time_deque)

        # Тестирование списка
        test_list_queue = list(range(size))
        time_list_pop = timeit.timeit(lambda: test_list_queue.pop(0),
                                      number=size) * 1000 / size
        list_pop_results.append(time_list_pop)
    return deque_results, list_pop_results


def plot_insert_comparison(sizes: list[int], list_times: list[float],
                           linked_list_times: list[float]) -> None:
    """График сравнения вставки."""
    plt.figure(figsize=(10, 6))
    plt.plot(sizes, list_times, "r-o", label="list.insert(0, x)")
    plt.plot(sizes, linked_list_times, "g-o",
             label="SingleLinkedList.add_to_beginning")
    plt.xlabel("Количество операций (N)")
    plt.ylabel("Среднее время операции (мс)")
    plt.title("Вставка в начало: list vs SingleLinkedList")
    plt.grid(True, linestyle="--", linewidth=0.5)
    plt.legend()
    plt.savefig("insert_comparison.png", dpi=300, bbox_inches="tight")


def plot_queue_comparison(sizes: list[int], deque_times: list[float],
                          list_pop_times: list[float]) -> None:
    """График сравнения очередей."""
    plt.figure(figsize=(10, 6))
    plt.plot(sizes, list_pop_times, "r-o", label="list.pop(0)")
    plt.plot(sizes, deque_times, "b-o", label="deque.popleft()")
    plt.xlabel("Количество операций (N)")
    plt.ylabel("Среднее время операции (мс)")
    plt.title("Удаление из начала: list vs deque")
    plt.grid(True, linestyle="--", linewidth=0.5)
    plt.legend()
    plt.savefig("queue_comparison.png", dpi=300, bbox_inches="tight")


def main() -> None:
    """Основной запуск: замеры + графики."""
    test_sizes = [100, 500, 1000, 5000, 10000]
    list_performance, linked_list_performance = compare_insert_beginning(
        test_sizes)
    deque_performance, list_pop_performance = compare_queue_operations(
        test_sizes)

    plot_insert_comparison(test_sizes, list_performance,
                           linked_list_performance)
    plot_queue_comparison(test_sizes, deque_performance, list_pop_performance)

    system_info = """
Характеристики системы для тестирования:
- Процессор: Intel Core i5-10110U @ 2.60GHz
- Оперативная память: 8 GB DDR4
- Операционная система: Windows 11
- Версия Python: 3.13.2
"""
    print(system_info)


if __name__ == "__main__":
    main()
