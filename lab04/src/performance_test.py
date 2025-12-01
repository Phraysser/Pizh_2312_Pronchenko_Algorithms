import timeit
import copy
import csv
from typing import List, Tuple

from sorts import SORT_FUNCTIONS, is_sorted, PC_INFO
from generate_data import generate_data


def measure_sort_time(func, data: List[int], runs: int = 3) -> float:
    """Возвращает среднее время в миллисекундах для func(copy(data))."""
    stmt = lambda: func(copy.deepcopy(data))
    total = timeit.timeit(stmt, number=runs)
    return (total / runs) * 1000.0


def run_experiments(
    sizes: List[int],
    data_types: List[str],
    runs: int = 3,
    csv_file: str = "lab04_results.csv"
) -> List[Tuple[str, int, str, float]]:
    """Запускает эксперименты и сохраняет результаты в CSV."""
    results: List[Tuple[str, int, str, float]] = []
    print(PC_INFO)

    for data_type in data_types:
        for n in sizes:
            data = generate_data(n, data_type)
            for name, func in SORT_FUNCTIONS.items():
                # Пропускаем квадратичные для больших n
                if (
                    n > 10000
                    and name in ("bubble_sort", "selection_sort",
                                 "insertion_sort")
                ):
                    print(f"Skipping {name} for n={n} (practical limit)")
                    continue

                t = measure_sort_time(func, data, runs=runs)
                # проверка корректности
                out = func(data.copy())
                assert is_sorted(out), (
                    f"{name} failed correctness for n={n}, type={data_type}"
                )
                results.append((name, n, data_type, t))
                print(
                    f"{name:15} | type={data_type:12} | "
                    f"n={n:6} -> {t:8.3f} ms"
                )

    # Сохраняем CSV
    with open(csv_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["algorithm", "size", "data_type", "time_ms"])
        for row in results:
            writer.writerow([row[0], row[1], row[2], f"{row[3]:.6f}"])

    print(f"Saved results to {csv_file}")
    return results


if __name__ == "__main__":
    sizes = [100, 500, 1000, 5000, 10000]
    data_types = ["random", "sorted", "reversed", "almost_sorted"]
    run_experiments(sizes, data_types, runs=3)
