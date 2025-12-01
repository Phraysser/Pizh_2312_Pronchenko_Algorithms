import random
from typing import List


def generate_data(size: int, data_type: str = "random",
                  almost_fraction: float = 0.95) -> List[int]:
    """Генерирует список целых чисел для тестов.

    data_type: 'random', 'sorted', 'reversed', 'almost_sorted'
    almost_fraction: доля упорядоченных элементов для almost_sorted
    """
    if size <= 0:
        return []
    if data_type == "random":
        return [random.randint(0, size * 10) for _ in range(size)]
    base = list(range(size))
    if data_type == "sorted":
        return base
    if data_type == "reversed":
        return base[::-1]
    if data_type == "almost_sorted":
        arr = base.copy()
        # Перемешаем небольшое количество пар
        num_swaps = max(1, int(size * (1 - almost_fraction)))
        for _ in range(num_swaps):
            i = random.randrange(size)
            j = random.randrange(size)
            arr[i], arr[j] = arr[j], arr[i]
        return arr
    raise ValueError(f"Unknown data_type: {data_type}")
