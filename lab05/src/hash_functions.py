from typing import Callable

PC_INFO: str = (
    """
Характеристики ПК для тестирования:
- Процессор: Intel Core i5-10110U @ 2.60GHz
- Оперативная память: 8 GB DDR4
- ОС: Windows 11
- Python: 3.13.2
"""
)


def simple_hash(s: str, mod: int) -> int:
    """
    Простая сумма кодов символов.
    Сложность: O(n) по времени, O(1) по памяти.
    Преимущества: очень простая, быстрая.
    Недостатки: плохое распределение (анализ анаграмм, короткие строки).
    """
    total = 0
    for ch in s:
        total += ord(ch)
    return total % mod


def poly_hash(s: str, mod: int, p: int = 31) -> int:
    """
    Полиномиальная (rolling) хеш-функция:
    h = sum( (code(ch) * p^i) ) mod M

    p — основание (например, 31 или 53).
    Сложность: O(n) по времени, O(1) по памяти (с аккуратным взятием mod).
    Примечание: для общих строк используют ord(ch) напрямую; при работе
    с буквами часто маппят 'a'->1 и т.п.
    """
    h = 0
    power = 1
    for ch in s:
        # можно использовать (ord(ch) - ord('a') + 1) для алфавита, но берём ord напрямую
        h = (h + (ord(ch) * power)) % mod
        power = (power * p) % mod
    return h % mod


def djb2(s: str, mod: int) -> int:
    """
    DJB2 — эмпирически хорошая простая хеш-функция.
    Инициализация: h = 5381
    Для каждого символа: h = h * 33 + ord(ch)

    Сложность: O(n) по времени, O(1) по памяти.
    Часто показывает хорошее распределение для строк.
    """
    h = 5381
    for ch in s:
        h = ((h << 5) + h) + ord(ch)
    return h % mod


# Тип для передачи хеш-функции: Callable[[str, int], int]
HashFn = Callable[[str, int], int]

if __name__ == "__main__":
    M = 1024
    print("PC_INFO:", PC_INFO)
    print("simple_hash('hello') =", simple_hash("hello", M))
    print("poly_hash('hello') =", poly_hash("hello", M))
    print("djb2('hello') =", djb2("hello", M))
