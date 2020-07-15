# coding: utf-8
"""
https://learning.oreilly.com/library/view/Data+Structures+and+Algorithms+in+Python/9781118290279/11_chap06.html#ch006-sec014
"""


class CircularArray:
    def __init__(self, capacity=10):
        self._capacity = capacity
        self._array = [None, ] * self._capacity
        self._size = 0
        self._front = 0

    # O(1)
    def __len__(self):
        return self._size

    def _positive_index(self, index):
        if index >= 0:
            if index >= self._size:
                raise IndexError
            positive_index = index
        else:
            if abs(index) > self._size:
                raise IndexError
            positive_index = self._size + index

        return positive_index

    # O(1)
    def __getitem__(self, index):
        positive_index = self._positive_index(index)
        actual_index = (self._front + positive_index) % self._capacity
        return self._array[actual_index]

    # O(1)
    def __setitem__(self, index, value):
        positive_index = self._positive_index(index)
        actual_index = (self._front + positive_index) % self._capacity
        self._array[actual_index] = value

    # O(n)
    def __iter__(self):
        for i in range(self._size):
            actual_index = (self._front + i) % self._capacity
            yield self._array[actual_index]

    # O(n)
    def _resize(self, new_capacity):
        new_array = [None, ] * new_capacity
        for i in range(self._size):
            old_index = (self._front + i) % self._capacity
            new_array[i] = self._array[old_index]

        self._array = new_array
        self._capacity = new_capacity
        self._front = 0

    @property
    def _rear(self):
        if self._size == 0:
            raise ValueError
        return (self._front + self._size - 1) % self._capacity

    # O(1)
    # O(n) if it triggers resize
    def append(self, value):
        if self._size == self._capacity:
            self._resize(self._capacity * 2)

        append_index = (self._front + self._size) % self._capacity
        self._array[append_index] = value
        self._size += 1

    # O(n)
    # O(1) if it pops the first or the last item and doesn't trigger resize
    def pop(self, index=-1):
        if self._size == 0:
            raise IndexError

        positive_index = self._positive_index(index)
        actual_index = (self._front + positive_index) % self._capacity
        pop_value = self._array[actual_index]

        if actual_index == self._front:  # the first item
            self._array[actual_index] = None
            self._size -= 1
            self._front = (self._front + 1) % self._capacity
        elif actual_index == self._rear:  # the last item
            self._array[actual_index] = None
            self._size -= 1
        else:
            for i in range(positive_index, self._size - 1):
                actual_i = (self._front + i) % self._capacity
                self._array[actual_i] = self._array[actual_i + 1]

            self._array[self._rear] = None
            self._size -= 1

        # Reduce the array to half of its current size,
        # whenever the number of elements stored in it falls below one fourth of its capacity
        if 0 < self._size < (self._capacity * (1 / 4)):
            self._resize(self._capacity // 2)

        return pop_value
