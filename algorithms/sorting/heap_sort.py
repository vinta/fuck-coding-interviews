# coding: utf-8
import heapq


class Heap:
    def __init__(self):
        self._array = []

    def _parent(self, index):
        return (index - 1) // 2

    def _left(self, index):
        return (2 * index) + 1

    def _right(self, index):
        return (2 * index) + 2

    def _swap(self, a, b):
        self._array[a], self._array[b] = self._array[b], self._array[a]

    def _up_heap(self, index):
        while index >= 1:
            parent_index = self._parent(index)
            parent = self._array[parent_index]
            current = self._array[index]
            if parent > current:
                self._swap(parent_index, index)
            else:
                return
            index = parent_index

    def push(self, value):
        self._array.append(value)
        self._up_heap(len(self._array) - 1)

    def _min_child_index(self, index):
        left_index = self._left(index)
        right_index = self._right(index)
        left = self._array[left_index] if left_index < len(self._array) else None
        right = self._array[right_index] if right_index < len(self._array) else None
        if (left is not None) and (right is not None):
            if left < right:
                return left_index
            else:
                return right_index
        if left is not None:
            return left_index
        if right is not None:
            return right_index

    def _down_heap(self, index):
        min_child_index = self._min_child_index(index)
        if min_child_index:
            current = self._array[index]
            min_child = self._array[min_child_index]
            if current > min_child:
                self._swap(index, min_child_index)
                self._down_heap(min_child_index)

    def pop_min(self):
        if not self._array:
            raise ValueError('heap is empty')

        self._swap(0, len(self._array) - 1)
        popped = self._array.pop()
        self._down_heap(0)

        return popped


def heap_sort(arr):
    heap = Heap()
    for item in arr:
        heap.push(item)
    return [heap.pop_min() for _ in range(len(arr))]


def heap_sort_heapq(arr):
    heapq.heapify(arr)
    return [heapq.heappop(arr) for _ in range(len(arr))]
