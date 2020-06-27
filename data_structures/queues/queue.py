# coding: utf-8
import unittest

from data_structures.linked_lists.singly_linked_list import LinkedList


class ArrayBasedQueue:
    def __init__(self):
        self.array = []

    def __len__(self):
        return len(self.array)

    def __bool__(self):
        return bool(self.array)

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


class LinkedListBasedQueue:
    def __init__(self):
        self.linked_list = LinkedList()

    def __len__(self):
        return len(self.linked_list)

    def __bool__(self):
        return bool(self.linked_list)

    def __iter__(self):
        for item in self.linked_list:
            yield item

    def enqueue(self, value):
        self.linked_list.append(value)

    def dequeue(self):
        try:
            return self.linked_list.pop(0)
        except IndexError:
            raise ValueError('Queue is empty')


class TestCase(unittest.TestCase):
    def setUp(self):
        self.queue = ArrayBasedQueue()

    def test__len__(self):
        self.assertEqual(len(self.queue), 0)

        self.queue.enqueue(0)
        self.assertEqual(len(self.queue), 1)

    def test__bool__(self):
        self.assertFalse(self.queue)

        self.queue.enqueue(0)
        self.assertTrue(self.queue)

    def test_enqueue(self):
        self.queue.enqueue(0)
        self.queue.enqueue(1)
        self.queue.enqueue(2)
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


class TestCase2(unittest.TestCase):
    def setUp(self):
        self.queue = LinkedListBasedQueue()

    def test__len__(self):
        self.assertEqual(len(self.queue), 0)

        self.queue.enqueue(0)
        self.assertEqual(len(self.queue), 1)

    def test__bool__(self):
        self.assertFalse(self.queue)

        self.queue.enqueue(0)
        self.assertTrue(self.queue)

    def test_enqueue(self):
        self.queue.enqueue(0)
        self.queue.enqueue(1)
        self.queue.enqueue(2)
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


if __name__ == '__main__':
    unittest.main()
