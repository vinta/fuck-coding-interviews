# coding: utf-8
"""
Heap
https://en.wikipedia.org/wiki/Heap_(data_structure)
"""


class ArrayBasedHeap:
    def __init__(self):
        self._array = []

    def __len__(self):
        return len(self._array)

    def _parent(self, index):
        return (index - 1) // 2

    def _left(self, index):
        return (2 * index) + 1

    def _right(self, index):
        return (2 * index) + 2

    def _is_leaf(self, index):
        length = len(self._array)
        if (self._left(index) < length) or (self._right(index) < length):
            return False

        return True

    def _swap(self, index_a, index_b):
        self._array[index_a], self._array[index_b] = self._array[index_b], self._array[index_a]

    def _min_child(self, index):
        length = len(self._array)
        left_index = self._left(index)
        right_index = self._right(index)
        left = self._array[left_index] if left_index < length else None
        right = self._array[right_index] if right_index < length else None
        if (left is not None) and (right is not None):
            if left < right:
                return left_index
            else:
                return right_index
        elif left is not None:
            return left_index
        elif right is not None:
            return right_index

    def _heapify(self, index):
        if not self._is_leaf(index):
            parent = self._array[index]
            min_child_index = self._min_child(index)
            min_child = self._array[min_child_index]
            if parent > min_child:
                self._swap(index, min_child_index)
                self._heapify(min_child_index)

    def push(self, value):
        self._array.append(value)

        index = len(self._array) - 1
        while index >= 1:
            parent_index = self._parent(index)
            if self._array[index] < self._array[parent_index]:
                self._swap(index, parent_index)
            index = parent_index

    def pop_min(self):
        try:
            popped = self._array[0]
        except IndexError:
            raise ValueError('heap is empty')

        self._swap(0, len(self._array) - 1)
        self._array.pop()
        self._heapify(0)

        return popped

    def peek_min(self):
        try:
            return self._array[0]
        except IndexError:
            raise ValueError('heap is empty')
