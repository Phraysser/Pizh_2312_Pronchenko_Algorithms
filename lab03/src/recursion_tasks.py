import os
from typing import List, Optional, Tuple


def binary_search_recursive(
    sorted_list: List[int],
    target_value: int,
    left_index: int,
    right_index: int
) -> Optional[int]:
    """Рекурсивный бинарный поиск в отсортированном массиве
    sorted_list[left_index:right_index+1].

    Временная сложность: O(log n)
    Пространственная сложность (стек): O(log n)
    """
    if left_index > right_index:  # O(1) — базовый случай, элемент не найден
        return None
    middle_index = (left_index + right_index) // 2  # O(1)
    if sorted_list[middle_index] == target_value:
        return middle_index
    if sorted_list[middle_index] < target_value:
        return binary_search_recursive(sorted_list, target_value,
                                       middle_index + 1, right_index)
    return binary_search_recursive(sorted_list, target_value, left_index,
                                   middle_index - 1)


def solve_hanoi_towers(
    disks_count: int,
    source: str,
    auxiliary: str,
    destination: str,
    moves_list: Optional[List[Tuple[str, str]]] = None
) -> List[Tuple[str, str]]:
    """Генерирует последовательность перемещений для задачи Ханойских башен.

    Возвращает список кортежей (откуда, куда).

    Временная сложность: O(2^n) (количество перемещений = 2^n - 1).
    Пространственная сложность: O(n) (глубина рекурсии).
    """
    if moves_list is None:
        moves_list = []
    if disks_count <= 0:
        return moves_list
    if disks_count == 1:
        moves_list.append((source, destination))
        return moves_list
    # Переместить n-1 дисков source -> auxiliary
    solve_hanoi_towers(disks_count - 1, source, destination,
                       auxiliary, moves_list)
    # Переместить самый большой диск source -> destination
    moves_list.append((source, destination))
    # Переместить n-1 дисков auxiliary -> destination
    solve_hanoi_towers(disks_count - 1, auxiliary, source,
                       destination, moves_list)
    return moves_list


def traverse_directory(
    directory_path: str,
    current_depth: int = 0,
    maximum_depth: Optional[int] = None
) -> List[str]:
    """Рекурсивный обход директории: возвращает список строк с отступами,
    представляющими дерево.

    current_depth: текущий уровень (используется для отступов).
    maximum_depth: если задан, ограничивает глубину обхода.

    Временная сложность: O(number_of_files + number_of_dirs)
    Пространственная сложность: O(depth)
    """
    result_entries: List[str] = []
    try:
        with os.scandir(directory_path) as directory_entries:
            for entry in directory_entries:
                result_entries.append("  " * current_depth + entry.name)
                if entry.is_dir(follow_symlinks=False):
                    if (maximum_depth is None or
                            current_depth + 1 <= maximum_depth):
                        result_entries.extend(
                            traverse_directory(entry.path, current_depth + 1,
                                               maximum_depth)
                        )
    except PermissionError:
        result_entries.append("  " * current_depth + "[PermissionError]")
    except FileNotFoundError:
        result_entries.append("  " * current_depth + "[NotFound]")
    return result_entries


def calculate_max_depth(directory_path: str) -> int:
    """Измеряет максимальную глубину вложенности в файловой системе начиная с
    directory_path.

    Возвращает максимальное значение depth.
    """
    max_depth = 0
    try:
        with os.scandir(directory_path) as directory_entries:
            for entry in directory_entries:
                if entry.is_dir(follow_symlinks=False):
                    child_depth = calculate_max_depth(entry.path)
                    if child_depth + 1 > max_depth:
                        max_depth = child_depth + 1
    except PermissionError:
        return 0
    except FileNotFoundError:
        return 0
    return max_depth


# Примеры работы
if __name__ == "__main__":
    # Рекурсивный бинарный поиск
    sample_array = list(range(0, 100, 2))
    result_index = binary_search_recursive(sample_array, 42, 0,
                                           len(sample_array) - 1)
    print("Index of 42 in even array:", result_index)

    # Ханойские башни (пример disks_count=3)
    hanoi_moves = solve_hanoi_towers(3, "A", "B", "C")
    print("Hanoi moves for disks_count=3:")
    for move in hanoi_moves:
        print(f"{move[0]} -> {move[1]}")

    # Обход текущей директории
    directory_tree = traverse_directory(".", maximum_depth=2)
    print("Directory tree (depth <=2):")
    for line in directory_tree[:50]:
        print(line)

    # Максимальная глубина текущей папки
    print("Max directory depth (this dir):", calculate_max_depth("."))
