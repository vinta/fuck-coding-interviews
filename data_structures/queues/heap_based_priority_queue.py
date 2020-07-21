# coding: utf-8
from data_structures.heaps.array_based_binary_heap import ArrayBasedBinaryHeap


class HeapBasedPriorityQueue:
    def __init__(self):
        self.heap = ArrayBasedBinaryHeap()

    def __len__(self):
        return len(self.heap)

    def __iter__(self):
        return self.heap.__iter__()

    def enqueue(self, value):
        self.heap.push(value)

    def dequeue(self):
        try:
            return self.heap.pop_min()
        except ValueError:
            raise ValueError('queue is empty')
