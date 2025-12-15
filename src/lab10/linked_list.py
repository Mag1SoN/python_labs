class Node:
    """Узел односвязного списка."""

    def __init__(self, value, next=None):
        """
        value - значение, хранящееся в узле
        next - ссылка на следующий узел или None
        """
        self.value = value
        self.next = next

    def __repr__(self):
        """Удобное представление узла для отладки."""
        return f"Node({self.value})"


class SinglyLinkedList:
    """Односвязный список."""

    def __init__(self):
        """Создаёт пустой список."""
        self.head = None   # первый элемент списка
        self.tail = None   # последний элемент списка
        self._size = 0     # количество элементов

    def append(self, value):
        """Добавить элемент в конец списка."""
        new_node = Node(value)

        # Если список пуст
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            # Привязываем новый узел к текущему хвосту
            self.tail.next = new_node
            self.tail = new_node

        self._size += 1

    def prepend(self, value):
        """Добавить элемент в начало списка."""
        new_node = Node(value, next=self.head)
        self.head = new_node

        # Если список был пуст
        if self.tail is None:
            self.tail = new_node

        self._size += 1

    def insert(self, idx, value):
        """Вставить элемент по индексу idx."""
        if idx < 0 or idx > self._size:
            raise IndexError(f"Index {idx} out of bounds for size {self._size}")

        # Вставка в начало
        if idx == 0:
            self.prepend(value)
            return

        # Вставка в конец
        if idx == self._size:
            self.append(value)
            return

        # Поиск узла перед нужной позицией
        cur = self.head
        for _ in range(idx - 1):
            cur = cur.next

        new_node = Node(value, next=cur.next)
        cur.next = new_node
        self._size += 1

    def remove(self, value):
        """Удалить первый элемент со значением value."""
        if self.head is None:
            raise ValueError(f"{value} not in list")

        # Если удаляем голову
        if self.head.value == value:
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            self._size -= 1
            return

        cur = self.head
        while cur.next is not None:
            if cur.next.value == value:
                # Если удаляем хвост
                if cur.next == self.tail:
                    self.tail = cur

                cur.next = cur.next.next
                self._size -= 1
                return
            cur = cur.next

        raise ValueError(f"{value} not in list")

    def __len__(self):
        """Вернуть количество элементов в списке."""
        return self._size

    def __iter__(self):
        """Итерация по значениям списка от головы к хвосту."""
        cur = self.head
        while cur is not None:
            yield cur.value
            cur = cur.next

    def __repr__(self):
        """Строковое представление списка."""
        values = list(self)
        return f"SinglyLinkedList({values})"



# test SinglyLinkedList
print("test SinglyLinkedList")
print()

sll = SinglyLinkedList()
print(f"1. Пустой список: {sll}")

sll.append(7)
sll.append(14)
print(f"2. Добавление в конец (7, 14): {sll}")

sll.prepend(3)
print(f"3. Добавление в начало (3): {sll}")

sll.insert(1, 10)
print(f"4. Вставка 10 по индексу 1: {sll}")

sll.remove(14)
print(f"5. Удаление 14: {sll}")

print(f"6. Размер: {len(sll)}")
print(f"7. Пуст ли список? {len(sll) == 0}")

