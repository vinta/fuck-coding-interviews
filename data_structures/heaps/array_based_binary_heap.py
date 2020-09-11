# coding: utf-8
"""
Binary Heap
https://en.wikipedia.org/wiki/Binary_heap
https://en.wikipedia.org/wiki/Heap_(data_structure)

A binary heap is a special binary tree which satisfies following properties:
- The tree is complete.
- The parent's value is less than or equal to children's values.
- The root's value would be the minimum of the tree.

A binary heap is typically represented as a compact array since it's a complete binary search tree:
- array[0] is the root node.
- array[floor((i - 1) / 2)] is the parent node of array[i].
- array[(i * 2) + 1] is the left child node of array[i].
- array[(i * 2) + 2] is the right child node of array[i].

Applications:
- K-way merges (merging k sorted arrays into a single sorted array).
- Priority queues.
"""


# This is a min heap.
class ArrayBasedBinaryHeap:
    def __init__(self):
        self._array = []

    def __len__(self):
        return len(self._array)

    def __iter__(self):
        for value in sorted(self._array):
            yield value

    def _parent(self, index):
        if index == 0:
            raise IndexError('The root node has no parent.')
        return (index - 1) // 2

    def _left(self, index):
        return (index * 2) + 1

    def _right(self, index):
        return (index * 2) + 2

    def _swap(self, index_a, index_b):
        self._array[index_a], self._array[index_b] = self._array[index_b], self._array[index_a]

    def _up_heap(self, index):
        # Compare the current item with its parent;
        # if they're not in the correct order, swap them.
        while index >= 1:
            parent_index = self._parent(index)
            if self._array[parent_index] > self._array[index]:
                self._swap(parent_index, index)
            else:
                return
            index = parent_index

    # O(1)
    # O(log n) if it triggers up-heap
    def push(self, value):
        self._array.append(value)  # Add the element to the bottom level at the leftmost open space.
        self._up_heap(len(self._array) - 1)

    def _min_child_index(self, index):
        left_index = self._left(index)
        right_index = self._right(index)
        left = self._array[left_index] if left_index < len(self._array) else None
        right = self._array[right_index] if right_index < len(self._array) else None

        # Determine the smaller child.
        if (left is not None) and (right is not None):  # There're both left and right children.
            return left_index if left < right else right_index
        elif left is not None:  # There's only left child.
            return left_index
        elif right is not None:  # There's only right child.
            return right_index

        return None  # There's no child.

    def _down_heap(self, index):
        # Compare the current item with its smaller child;
        # if they're not in the correct order, swap with its smaller child.
        min_child_index = self._min_child_index(index)
        if min_child_index:
            current = self._array[index]
            min_child = self._array[min_child_index]
            if current > min_child:
                self._swap(index, min_child_index)
                self._down_heap(min_child_index)

    # O(log n)
    def pop_min(self):
        if not self._array:
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
