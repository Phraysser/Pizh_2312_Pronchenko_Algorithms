"""Реализация односвязного списка (ЛР-02)."""
from __future__ import annotations
from typing import Any, Optional


class ListNode:
    """Узел связного списка."""

    def __init__(self, value: Any) -> None:
        self.value: Any = value
        self.next_ptr: Optional[ListNode] = None


class SingleLinkedList:
    """Односвязный список."""

    def __init__(self) -> None:
        self.first: Optional[ListNode] = None
        self.last: Optional[ListNode] = None  # Для O(1) вставки в конец

    def add_to_beginning(self, value: Any) -> None:
        """Вставка элемента в начало. Сложность O(1)."""
        new_elem = ListNode(value)  # O(1)
        new_elem.next_ptr = self.first  # O(1)
        self.first = new_elem  # O(1)
        if self.last is None:  # O(1)
            self.last = new_elem  # O(1)

    def add_to_end(self, value: Any) -> None:
        """Вставка элемента в конец. Сложность O(1) при наличии last."""
        new_elem = ListNode(value)  # O(1)
        if self.last:  # O(1)
            self.last.next_ptr = new_elem  # O(1)
            self.last = new_elem  # O(1)
        else:
            self.first = self.last = new_elem  # O(1)

    def remove_from_beginning(self) -> Optional[Any]:
        """Удаление элемента из начала. Сложность O(1)."""
        if self.first is None:  # O(1)
            return None
        deleted_value = self.first.value  # O(1)
        self.first = self.first.next_ptr  # O(1)
        if self.first is None:  # O(1)
            self.last = None  # O(1)
        return deleted_value  # O(1)

    def get_all_elements(self) -> list[Any]:
        """Возвращает список элементов. Сложность O(n)."""
        result: list[Any] = []  # O(1)
        current_elem = self.first  # O(1)
        while current_elem:  # O(n)
            result.append(current_elem.value)  # O(1)
            current_elem = current_elem.next_ptr  # O(1)
        return result  # O(1)
