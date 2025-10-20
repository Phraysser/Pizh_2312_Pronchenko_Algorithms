# sum_analysis.py
import random
import timeit
from typing import List

import matplotlib.pyplot as plt


def read_and_sum(filename: str) -> None:
    """
    Читает два числа из файла и выводит их сумму.
    Сложность: O(1) - постоянное время выполнения.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()  # O(1)

    print("Считанные данные:")
    for line in lines:  # O(1)
        print(f"→ {line.strip()}")

    a: int = int(lines[0].strip())  # O(1)
    b: int = int(lines[1].strip())  # O(1)
    result: int = a + b  # O(1)

    print(f"Результат: {a} + {b} = {result}")


def array_sum(numbers: List[int]) -> int:
    """Вычисляет сумму элементов массива.

    Сложность: O(N), где N - количество элементов.
    """
    total: int = 0  # O(1)
    for num in numbers:  # O(N)
        total += num  # O(1)
    return total  # O(1)


def measure_execution_time(func, data: List[int]) -> float:
    """Измеряет время выполнения функции в миллисекундах."""
    start_time: float = timeit.default_timer()
    func(data)
    end_time: float = timeit.default_timer()
    return (end_time - start_time) * 1000


def perform_measurements() -> None:
    """Проводит измерения производительности и строит график."""
    system_info: str = """
Тестовый стенд:
- Процессор: Intel Core i5-10210U @ 1.60GHz
- Память: 8 GB DDR4
- ОС: Windows 11
- Python: 3.13.2
"""
    print(system_info)

    sizes: List[int] = [1000, 5000, 10000, 50000, 100000, 500000]
    execution_times: List[float] = []

    print('Результаты измерений:')
    print('{:>10} {:>12} {:>15}'.format('Размер', 'Время (мс)',
                                        'На элемент (мкс)'))

    for size in sizes:
        test_data: List[int] = [random.randint(1, 1000) for _ in range(size)]
        time_per_run: float = (
            timeit.timeit(lambda: array_sum(test_data), number=10) * 1000 / 10
        )
        execution_times.append(time_per_run)
        per_element_time: float = (
            (time_per_run * 1000) / size if size > 0 else 0
            )

        print(
            '{:>10} {:>12.4f} {:>15.4f}'.format(
                size, time_per_run, per_element_time
            )
        )

    plt.figure(figsize=(10, 6))
    plt.plot(sizes, execution_times, 'bo-', label='Время выполнения')
    plt.xlabel('Размер массива')
    plt.ylabel('Время (мс)')
    plt.title('Производительность алгоритма суммирования\nСложность: O(N)')
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend()
    plt.savefig('performance_plot.png', dpi=300, bbox_inches='tight')
    plt.show()

    print('\nВыводы:')
    print('• Алгоритм демонстрирует линейную сложность O(N)')
    print('• Время выполнения пропорционально размеру массива')
    print(f'• Среднее время на элемент: {per_element_time:.4f} мкс')


if __name__ == '__main__':
    read_and_sum("input.txt")
    perform_measurements()
