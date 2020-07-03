# coding: utf-8
import unittest


class ArrayBasedQueue:
    def __init__(self):
        self.array = []

    def __len__(self):
        return len(self.array)

    def __iter__(self):
        for item in self.array:
            yield item

    def enqueue(self, value):
        self.array.append(value)

    def dequeue(self):
        try:
            return self.array.pop(0)
        except IndexError:
            raise ValueError('Queue is empty')


class TestCase(unittest.TestCase):
    def setUp(self):
        self.queue = ArrayBasedQueue()

    def test_enqueue(self):
        self.queue.enqueue(0)
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.assertEqual(len(self.queue), 3)
        self.assertEqual(list(self.queue), [0, 1, 2])

    def test_dequeue(self):
        with self.assertRaises(ValueError):
            print(self.queue.dequeue())

        self.queue.enqueue(0)
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.assertEqual(self.queue.dequeue(), 0)
        self.assertEqual(self.queue.dequeue(), 1)
        self.assertEqual(self.queue.dequeue(), 2)
        self.assertEqual(len(self.queue), 0)
        self.assertEqual(list(self.queue), [])

        with self.assertRaises(ValueError):
            print(self.queue.dequeue())


if __name__ == '__main__':
    unittest.main()
