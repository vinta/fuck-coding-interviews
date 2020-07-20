# coding: utf-8
import heapq
import random
import unittest

from data_structures.trees.array_based_binary_heap import ArrayBasedBinaryHeap


class TestCase(unittest.TestCase):
    def setUp(self):
        self.empty_heap = ArrayBasedBinaryHeap()
        self.heap = ArrayBasedBinaryHeap()
        self.heapq_heap = []

        self.values = [random.randint(-100, 100) for _ in range(random.randint(1, 100))]
        for value in self.values:
            self.heap.push(value)
            heapq.heappush(self.heapq_heap, value)

    def test__len__(self):
        self.assertEqual(len(self.empty_heap), 0)
        self.assertEqual(len(self.heap), len(self.values))

    def test_push(self):
        self.empty_heap.push(42)
        self.assertEqual(len(self.empty_heap), 1)
        self.assertEqual(self.empty_heap.pop_min(), 42)
        self.assertEqual(len(self.empty_heap), 0)

    def test_pop_min(self):
        for _ in range(len(self.values)):
            self.assertEqual(self.heap.pop_min(), heapq.heappop(self.heapq_heap))

        self.assertEqual(len(self.heap), 0)

    def test_peek_min(self):
        with self.assertRaises(ValueError):
            self.empty_heap.peek_min()

        self.assertEqual(self.heap.peek_min(), self.heapq_heap[0])


if __name__ == '__main__':
    unittest.main()
