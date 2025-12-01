"""
tests.py

Набор простых unit-тестов (не использует pytest, можно запускать напрямую).
Каждый тест возвращает True при успехе, в конце — сообщение.
"""

from hash_table_chaining import HashTableChaining
from hash_table_open_addressing import HashTableOpenAddressing

def test_chaining_basic() -> bool:
    ht = HashTableChaining()
    ht.insert("one", 1)
    ht.insert("two", 2)
    assert ht.get("one") == 1
    assert ht.get("two") == 2
    assert ht.get("three") is None
    assert ht.contains("one")
    ht.remove("one")
    assert not ht.contains("one")
    return True

def test_open_addressing_basic() -> bool:
    ht = HashTableOpenAddressing(mode="linear")
    ht.insert("x", "X")
    ht.insert("y", "Y")
    assert ht.get("x") == "X"
    assert ht.get("y") == "Y"
    assert ht.contains("y")
    ht.remove("x")
    assert not ht.contains("x")
    return True

def test_collision_and_resize() -> bool:
    # проверяем, что после большого числа вставок — все элементы доступны
    ht = HashTableChaining(capacity=4)
    for i in range(50):
        ht.insert(f"k{i}", i)
    for i in range(50):
        assert ht.get(f"k{i}") == i
    return True

if __name__ == "__main__":
    tests = [
        ("chaining_basic", test_chaining_basic),
        ("open_basic", test_open_addressing_basic),
        ("collision_resize", test_collision_and_resize)
    ]
    for name, fn in tests:
        try:
            ok = fn()
            print(f"{name}: OK" if ok else f"{name}: FAIL")
        except AssertionError as e:
            print(f"{name}: ASSERTION FAILED ->", e)
    print("Тесты завершены")