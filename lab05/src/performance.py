import timeit
from typing import Callable, Tuple
from hash_table_chaining import HashTableChaining
from hash_table_open_addressing import HashTableOpenAddressing

def measure(table_factory: Callable[[], object], n_ops: int = 1000, load: float = 0.5) -> Tuple[float, float, float]:
    """
    Замер трёх операций:
    - вставка n_ops элементов
    - поиск n_ops элементов
    - удаление n_ops элементов

    table_factory — callable, возвращающий новый экземпляр таблицы (без аргументов).
    Возвращает кортеж (t_insert, t_get, t_remove) в секундах.
    """
    tbl = table_factory()
    # предварительно заполним таблицу до заданного load (приблизительно)
    prefill = int(tbl._capacity * load)
    for i in range(prefill):
        tbl.insert(f"pre{i}", i)

    keys = [f"k{i}" for i in range(n_ops)]

    def inserts():
        for i, k in enumerate(keys):
            tbl.insert(k, i)

    def gets():
        for k in keys:
            tbl.get(k)

    def removes():
        for k in keys:
            tbl.remove(k)

    # усредняем по нескольким запускам
    t_ins = timeit.timeit(inserts, number=3) / 3
    t_get = timeit.timeit(gets, number=3) / 3
    t_rem = timeit.timeit(removes, number=3) / 3
    return t_ins, t_get, t_rem


if __name__ == "__main__":
    factors = [0.1, 0.5, 0.7, 0.9]
    for f in factors:
        print("Chaining load", f, measure(lambda: HashTableChaining(), n_ops=500, load=f))
        print("Open (linear) load", f, measure(lambda: HashTableOpenAddressing(mode="linear"), n_ops=500, load=f))
