from collections import deque


class Stack:
    """Стек (LIFO) на основе списка."""

    def __init__(self, data: list = []):
        """Создаёт стек.
        data - список, в котором хранятся элементы стека.
        """
        self._data = data

    def push(self, item):
        """Добавить элемент на вершину стека."""
        self._data.append(item)

    def pop(self):
        """Снять и вернуть верхний элемент стека."""
        return self._data.pop()

    def peek(self):
        """Вернуть верхний элемент без удаления."""
        return self._data[-1]

    def is_empty(self):
        """Проверить, пуст ли стек."""
        return len(self._data) == 0

    def __len__(self):
        """Вернуть количество элементов в стеке."""
        return len(self._data)


class Queue:
    """Очередь на основе deque."""

    def __init__(self, data: deque = []):
        """Создаёт очередь.
        data - deque, в котором хранятся элементы очереди.
        """
        self._data = data

    def enqueue(self, item):
        """Добавить элемент в очередь."""
        self._data.append(item)

    def dequeue(self):
        """Удалить и вернуть элемент из очереди.
        Если очередь пуста - выбрасывает IndexError.
        """
        if self._data == []:
            raise IndexError("Queue is empty")
        else:
            return self._data.pop()

    def peek(self):
        """Вернуть элемент очереди без удаления.
        Если очередь пуста - вернуть None.
        """
        if self._data == []:
            return None
        return self._data[-1]

    def is_empty(self):
        """Проверить, пуста ли очередь."""
        if self._data == []:
            return True
        else:
            return False

    def __len__(self):
        """Вернуть количество элементов в очереди."""
        return len(self._data)


# test Stack
print("test Stack\n")
s = Stack([])                  # создание пустого стека
s.push(8)                      # добавляем 8 в стек
s.push(4)                      # добавляем 4 поверх 8
print(s.pop())                 # удаляем и выводим верхний элемент (4)
print(s.peek())                # смотрим верхний элемент (8)
print(s.__len__())             # выводим количество элементов в стеке
print(s.is_empty())            # проверяем, пуст ли стек
s.pop()                        # удаляем последний элемент (8)
print(s.is_empty())            # проверяем, пуст ли стек после удаления

print("-------------")

# test Queue
print("test Queue\n")
q = Queue()                    # создание пустой очереди
q.enqueue(7)                   # добавляем 7 в очередь
q.enqueue(21)                  # добавляем 21 в очередь
print(q.dequeue())             # удаляем и выводим элемент из очереди
print(q.peek())                # смотрим элемент очереди без удаления
print(q.__len__())             # выводим количество элементов в очереди
print(q.is_empty())            # проверяем, пуста ли очередь
q.dequeue()                    # удаляем последний элемент очереди
print(q.is_empty())            # проверяем, пуста ли очередь после удаления
