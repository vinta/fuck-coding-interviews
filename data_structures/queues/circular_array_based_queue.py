# coding: utf-8
"""
FIFO: first in, first out
append, pop left
"""
import unittest


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

    def _expand(self, new_capacity):
        new_array = [None, ] * new_capacity
        for i in range(self._size):
            old_index = (self._front + i) % self._capacity
            new_array[i] = self._array[old_index]

        self._array = new_array
        self._capacity = new_capacity
        self._front = 0

    def append(self, value):
        if self._size == self._capacity:
            self._expand(self._capacity * 2)

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
    def enqueue(self, value):
        self._array.append(value)

    # O(1)
    def dequeue(self):
        try:
            return self._array.pop_left()
        except ValueError:
            raise ValueError('Queue is empty')


class TestCase(unittest.TestCase):
    def setUp(self):
        self.queue = CircularArrayBasedQueue(capacity=4)

    def test_enqueue(self):
        self.queue.enqueue(0)
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.queue.enqueue(3)
        self.queue.enqueue(4)
        self.assertEqual(len(self.queue), 5)
        self.assertEqual(list(self.queue), [0, 1, 2, 3, 4])

    def test_dequeue(self):
        with self.assertRaises(ValueError):
            print(self.queue.dequeue())

        self.queue.enqueue(0)
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.assertEqual(self.queue.dequeue(), 0)
        self.assertEqual(self.queue.dequeue(), 1)
        self.queue.enqueue(3)
        self.queue.enqueue(4)
        self.queue.enqueue(5)
        self.assertEqual(self.queue.dequeue(), 2)
        self.assertEqual(len(self.queue), 3)
        self.assertEqual(list(self.queue), [3, 4, 5])
        self.assertEqual(self.queue.dequeue(), 3)
        self.assertEqual(self.queue.dequeue(), 4)
        self.assertEqual(self.queue.dequeue(), 5)
        self.assertEqual(len(self.queue), 0)
        self.assertEqual(list(self.queue), [])

        with self.assertRaises(ValueError):
            print(self.queue.dequeue())


if __name__ == '__main__':
    unittest.main()
