# coding: utf-8
import unittest


from data_structures.queues.circular_array_based_queue import CircularArrayBasedQueue


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
