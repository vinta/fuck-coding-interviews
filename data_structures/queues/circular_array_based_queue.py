# coding: utf-8
"""
FIFO: first in, first out
append, pop left
"""


# Also see: https://github.com/vinta/fuck-coding-interviews/blob/master/data_structures/arrays/circular_array.py
# This implementation is more simplified, however, with specific modifications
class CircularArray:
    def __init__(self, capacity=10):
        self._capacity = capacity
        self._array = [None, ] * self._capacity
        self._size = 0
        self._front = 0

    def __len__(self):
        return self._size

    def __iter__(self):
        for i in range(self._size):
            index = (self._front + i) % self._capacity
            yield self._array[index]

    def _resize(self, new_capacity):
        new_array = [None, ] * new_capacity
        for i in range(self._size):
            old_index = (self._front + i) % self._capacity
            new_array[i] = self._array[old_index]

        self._array = new_array
        self._capacity = new_capacity
        self._front = 0

    def append(self, value):
        if self._size == self._capacity:
            self._resize(self._capacity * 2)

        append_index = (self._front + self._size) % self._capacity
        self._array[append_index] = value
        self._size += 1

    def pop_left(self):
        if self._size == 0:
            raise ValueError

        pop_value = self._array[self._front]
        self._array[self._front] = None
        self._size -= 1
        self._front = (self._front + 1) % self._capacity

        return pop_value


class CircularArrayBasedQueue:
    def __init__(self, capacity=None):
        self._array = CircularArray(capacity=capacity) if capacity else CircularArray()

    # O(1)
    def __len__(self):
        return len(self._array)

    # O(n)
    def __iter__(self):
        return self._array.__iter__()

    # O(1)
    # O(n) if it triggers resizing
    def enqueue(self, value):
        self._array.append(value)

    # O(1)
    def dequeue(self):
        try:
            return self._array.pop_left()
        except ValueError:
            raise ValueError('queue is empty')
