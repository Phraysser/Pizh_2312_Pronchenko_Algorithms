from typing import Any, Optional, Tuple, List
from hash_functions import HashFn, djb2, poly_hash, simple_hash

PC_INFO: str = "HashTableOpenAddressing — open addressing implementation."

_TOMBSTONE = object()
Slot = Optional[Tuple[str, Any]]

class HashTableOpenAddressing:
    """
    Параметры:
        capacity: начальный размер таблицы (>= 8)
        hash_fn: первичная хеш-функция
        second_hash_fn: вторичная функция для double hashing
        mode: 'linear' или 'double'

    Особенности:
        - Ресайз при (size+1)/capacity > 0.6
        - Используется tombstone для удалений
    Временная сложность (ожидаемая):
        insert/get/remove: O(1) при умеренном load factor, иначе может быстро деградировать
    """
    def __init__(
        self,
        capacity: int = 8,
        hash_fn: HashFn = djb2,
        second_hash_fn: HashFn = poly_hash,
        mode: str = "linear"
    ):
        assert mode in ("linear", "double")
        self._capacity = max(8, capacity)
        self._table: List[Slot] = [None] * self._capacity
        self._size = 0
        self._hash_fn = hash_fn
        self._second_hash_fn = second_hash_fn
        self._mode = mode

    def _idx(self, key: str, i: int) -> int:
        """Вычисление индекса с учётом i-й попытки (probe)."""
        h1 = self._hash_fn(key, self._capacity)
        if self._mode == "linear":
            return (h1 + i) % self._capacity
        else:
            # для второй функции берем мод (capacity - 1) чтобы шаг был в [0, capacity-2], затем +1
            step = (self._second_hash_fn(key, self._capacity - 1) % (self._capacity - 1)) + 1
            return (h1 + i * step) % self._capacity

    def insert(self, key: str, value: Any) -> None:
        """
        Вставка/обновление. При достижении порога ресайзится (умножение на 2).
        Сложность: ожидаемая O(1), худшая O(n) (при полном заполнении).
        """
        if (self._size + 1) / self._capacity > 0.6:
            self._resize(self._capacity * 2)

        first_tomb = None
        for i in range(self._capacity):
            idx = self._idx(key, i)
            slot = self._table[idx]
            if slot is None:
                # если нашли пустой слот — используем либо первый tomb, либо текущий
                if first_tomb is not None:
                    self._table[first_tomb] = (key, value)
                else:
                    self._table[idx] = (key, value)
                self._size += 1
                return
            if slot is _TOMBSTONE:
                if first_tomb is None:
                    first_tomb = idx
                continue
            k, _ = slot
            if k == key:
                # обновление значения
                self._table[idx] = (key, value)
                return
        # если дошли до конца — таблица полна (обычно этого не происходит из-за ресайза)
        raise RuntimeError("HashTable is full")

    def get(self, key: str) -> Optional[Any]:
        """
        Поиск по ключу. Возвращает значение или None.
        Сложность: O(1) ожидаемо, может расти при большом load factor.
        """
        for i in range(self._capacity):
            idx = self._idx(key, i)
            slot = self._table[idx]
            if slot is None:
                return None
            if slot is _TOMBSTONE:
                continue
            k, v = slot
            if k == key:
                return v
        return None

    def remove(self, key: str) -> bool:
        """
        Удаление ключа — помечает слот как tombstone.
        Возвращает True, если удаление произошло.
        """
        for i in range(self._capacity):
            idx = self._idx(key, i)
            slot = self._table[idx]
            if slot is None:
                return False
            if slot is _TOMBSTONE:
                continue
            k, _ = slot
            if k == key:
                self._table[idx] = _TOMBSTONE
                self._size -= 1
                return True
        return False

    def contains(self, key: str) -> bool:
        return self.get(key) is not None

    def _resize(self, new_capacity: int) -> None:
        """
        Перехеширование всех существующих (не-tombstone) слотов в новую таблицу.
        Сложность: O(n).
        """
        old_items: List[Tuple[str, Any]] = []
        for slot in self._table:
            if slot is not None and slot is not _TOMBSTONE:
                old_items.append(slot)
        self._capacity = max(8, new_capacity)
        self._table = [None] * self._capacity
        self._size = 0
        for k, v in old_items:
            self.insert(k, v)

    def __len__(self) -> int:
        return self._size


if __name__ == "__main__":
    ht = HashTableOpenAddressing(mode="double", second_hash_fn=simple_hash)
    ht.insert("a", 1)
    ht.insert("b", 2)
    print("a ->", ht.get("a"))
    ht.remove("a")
    print("contains a?", ht.contains("a"))
