# coding: utf-8
"""
Binary Heap
https://en.wikipedia.org/wiki/Binary_heap

A binary heap is a special binary tree which satisfies following properties:
- The tree is complete.
- The parent's value is less than or equal to children's values.
- The root's value would be the minimum of the tree.
"""


# This is a min heap.
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

    def _swap(self, index_a, index_b):
        self._array[index_a], self._array[index_b] = self._array[index_b], self._array[index_a]

    def _up_heap(self, index):
        # Compare the current item with its parent;
        # if they're not in the correct order, swap them.
        while index >= 1:
            parent_index = self._parent(index)
            if self._array[parent_index] > self._array[index]:
                self._swap(index, parent_index)
            else:
                return
            index = parent_index

    # O(log n)
    def push(self, value):
        self._array.append(value)
        self._up_heap(len(self._array) - 1)

    def _down_heap(self, index):
        # Compare the current item with its children;
        # if they're not in the correct order, swap with its smaller child.
        length = len(self._array)
        left_index = self._left(index)
        right_index = self._right(index)
        left = self._array[left_index] if left_index < length else None
        right = self._array[right_index] if right_index < length else None
        if (left is not None) or (right is not None):
            # determine the smaller child
            if (left is not None) and (right is not None):
                if left < right:
                    min_child_index = left_index
                else:
                    min_child_index = right_index
            elif left is not None:
                min_child_index = left_index
            elif right is not None:
                min_child_index = right_index

            parent = self._array[index]
            min_child = self._array[min_child_index]
            if parent > min_child:
                self._swap(index, min_child_index)
                self._down_heap(min_child_index)

    # O(log n)
    def pop_min(self):
        if not self:
            raise ValueError('heap is empty')

        # Replace the root with the last element on the last level, and drop the old root.
        self._swap(0, len(self._array) - 1)
        popped = self._array.pop()
        self._down_heap(0)

        return popped

    # O(1)
    def peek_min(self):
        try:
            return self._array[0]
        except IndexError:
            raise ValueError('heap is empty')
