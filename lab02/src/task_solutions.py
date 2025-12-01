"""Практические задачи из ЛР-02."""
from collections import deque


def check_bracket_balance(expression: str) -> bool:
    """Проверка сбалансированности скобок. Сложность O(n)."""
    stack: list[str] = []  # O(1)
    bracket_pairs = {')': '(', ']': '[', '}': '{'}

    for character in expression:  # O(n)
        if character in bracket_pairs.values():
            stack.append(character)  # O(1)
        elif character in bracket_pairs:  # O(1)
            if not stack or stack.pop() != bracket_pairs[character]:  # O(1)
                return False
    return not stack  # O(1)


def simulate_print_queue(print_jobs: list[str]) -> None:
    """Симуляция обработки очереди печати. Сложность O(n)."""
    print_queue = deque(print_jobs)  # O(n)
    while print_queue:  # O(n)
        current_job = print_queue.popleft()  # O(1)
        print(f"Печатается: {current_job}")  # O(1)


def check_palindrome(sequence: str) -> bool:
    """Проверка палиндрома через deque. Сложность O(n)."""
    char_deque = deque(sequence.lower())  # O(n)
    while len(char_deque) > 1:  # O(n/2)
        if char_deque.popleft() != char_deque.pop():  # O(1)
            return False
    return True


if __name__ == "__main__":
    print("=== Проверка сбалансированных скобок ===")
    test_expressions = ["(a + b) * [c - d]", "([)]", "{[()()]}", "(()", ""]
    for expr in test_expressions:
        print(f"{expr!r} -> {check_bracket_balance(expr)}")

    print("\n=== Симуляция очереди печати ===")
    job_list = ["Документ1", "Фото2", "Отчет3"]
    simulate_print_queue(job_list)

    print("\n=== Проверка палиндромов ===")
    test_words = ["level", "Racecar", "python", "А роза упала на лапу Азора"]
    for word in test_words:
        cleaned_word = "".join(char for char in word if char.isalpha())
        print(f"{word!r} -> {check_palindrome(cleaned_word)}")
