
SYSTEM_INFO: str = (
    "Характеристики системы для тестирования:\n"
    "- Процессор: (заполните)\n"
    "- Оперативная память: (заполните)\n"
    "- Операционная система: (заполните)\n"
    "- Версия Python: (заполните)\n"
)


def compute_factorial(number: int) -> int:
    """Вычисляет факториал number рекурсивно.

    Базовый случай: compute_factorial(0) == 1.
    Временная сложность: O(n) — выполняется n рекурсивных вызовов.
    Пространственная сложность (стек): O(n) — глубина рекурсии n.
    """
    if number < 0:
        raise ValueError("Число должно быть неотрицательным")
    if number == 0:  # O(1) — базовый случай
        return 1  # O(1)
    return number * compute_factorial(number - 1)  # O(1) * O(n-1) => O(n)


def fibonacci_recursive(n: int) -> int:
    """Наивный рекурсивный расчёт n-го числа Фибоначчи.

    Определение:
        fibonacci_recursive(0) = 0, fibonacci_recursive(1) = 1
        fibonacci_recursive(n) = fibonacci_recursive(n-1) +
        fibonacci_recursive(n-2) для n >= 2

    Временная сложность: O(phi^n) — экспоненциальная (примерно O(1.618^n)).
    Пространственная сложность (стек): O(n) — глубина рекурсии равна n.
    """
    if n < 0:
        raise ValueError("n должно быть неотрицательным")
    if n < 2:  # O(1) — базовый случай
        return n  # O(1)
    # два рекурсивных вызова
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def fast_exponentiation(base: float, exponent: int) -> float:
    """Быстрое возведение base в степень exponent (exponentiation by squaring).

    Временная сложность: O(log n) — число рекурсивных вызовов ~ log2(n).
    Пространственная сложность: O(log n) — глубина стека рекурсии.
    """
    if exponent < 0:
        return 1.0 / fast_exponentiation(base, -exponent)
    if exponent == 0:
        return 1.0
    if exponent % 2 == 0:
        half_power = fast_exponentiation(base, exponent // 2)
        return half_power * half_power
    # exponent нечетное
    return base * fast_exponentiation(base, exponent - 1)


if __name__ == "__main__":
    print(SYSTEM_INFO)
    print("compute_factorial(5) =", compute_factorial(5))  # 120
    print("fibonacci_recursive(10) =", fibonacci_recursive(10))  # 55
    print("fast_exponentiation(2, 10) =", fast_exponentiation(2, 10))  # 1024
