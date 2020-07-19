# coding: utf-8
import random
import unittest

from data_structures.trees.array_based_heap import ArrayBasedHeap


class TestCase(unittest.TestCase):
    def setUp(self):
        self.empty_heap = ArrayBasedHeap()
        self.heap = ArrayBasedHeap()

        self.values = [random.randint(-100, 100) for _ in range(random.randint(1, 100))]
        for value in self.values:
            self.heap.push(value)

    def test__len__(self):
        self.assertEqual(len(self.empty_heap), 0)
        self.assertEqual(len(self.heap), len(self.values))

    def test_push(self):
        self.empty_heap.push(42)
        self.assertEqual(len(self.empty_heap), 1)

    def test_pop_min(self):
        self.empty_heap.push(42)
        self.empty_heap.push(8)
        self.empty_heap.push(27)
        self.empty_heap.push(99)
        self.assertEqual(self.empty_heap.pop_min(), 8)
        self.assertEqual(self.empty_heap.pop_min(), 27)
        self.assertEqual(self.empty_heap.pop_min(), 42)
        self.assertEqual(self.empty_heap.pop_min(), 99)
        self.assertEqual(len(self.empty_heap), 0)

    def test_peek_min(self):
        with self.assertRaises(ValueError):
            self.empty_heap.peek_min()

        self.assertEqual(self.heap.peek_min(), min(self.values))


if __name__ == '__main__':
    unittest.main()
