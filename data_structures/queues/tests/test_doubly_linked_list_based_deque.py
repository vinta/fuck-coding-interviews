# coding: utf-8
import unittest

from data_structures.queues.doubly_linked_list_based_deque import DoublyLinkedListBasedDeque


class TestCase(unittest.TestCase):
    def setUp(self):
        self.deque = DoublyLinkedListBasedDeque()

    def test_append(self):
        self.deque.append(0)
        self.assertEqual(self.deque.linked_list.head.value, 0)
        self.assertEqual(self.deque.linked_list.head.previous, None)
        self.assertEqual(self.deque.linked_list.tail.value, 0)
        self.assertEqual(self.deque.linked_list.tail.next, None)
        self.deque.append(1)
        self.assertEqual(self.deque.linked_list.head.value, 0)
        self.assertEqual(self.deque.linked_list.head.previous, None)
        self.assertEqual(self.deque.linked_list.tail.value, 1)
        self.assertEqual(self.deque.linked_list.tail.next, None)
        self.deque.append(2)
        self.assertEqual(self.deque.linked_list.head.value, 0)
        self.assertEqual(self.deque.linked_list.head.previous, None)
        self.assertEqual(self.deque.linked_list.tail.value, 2)
        self.assertEqual(self.deque.linked_list.tail.next, None)

        expected = [0, 1, 2]
        self.assertEqual(len(self.deque), 3)
        self.assertEqual(list(self.deque), expected)
        self.assertEqual(list(reversed(self.deque)), list(reversed(expected)))

    def test_append_left(self):
        self.deque.append_left(0)
        self.assertEqual(self.deque.linked_list.head.value, 0)
        self.assertEqual(self.deque.linked_list.head.previous, None)
        self.assertEqual(self.deque.linked_list.tail.value, 0)
        self.assertEqual(self.deque.linked_list.tail.next, None)
        self.deque.append_left(1)
        self.assertEqual(self.deque.linked_list.head.value, 1)
        self.assertEqual(self.deque.linked_list.head.previous, None)
        self.assertEqual(self.deque.linked_list.tail.value, 0)
        self.assertEqual(self.deque.linked_list.tail.next, None)
        self.deque.append_left(2)
        self.assertEqual(self.deque.linked_list.head.value, 2)
        self.assertEqual(self.deque.linked_list.head.previous, None)
        self.assertEqual(self.deque.linked_list.tail.value, 0)
        self.assertEqual(self.deque.linked_list.tail.next, None)

        expected = [2, 1, 0]
        self.assertEqual(len(self.deque), 3)
        self.assertEqual(list(self.deque), expected)
        self.assertEqual(list(reversed(self.deque)), list(reversed(expected)))

    def test_pop(self):
        with self.assertRaises(ValueError):
            print(self.deque.pop())

        self.deque.append(0)
        self.deque.append(1)
        self.deque.append(2)
        self.assertEqual(self.deque.pop(), 2)
        self.assertEqual(self.deque.linked_list.head.previous, None)
        self.assertEqual(self.deque.linked_list.tail.next, None)
        self.assertEqual(self.deque.pop(), 1)
        self.assertEqual(self.deque.linked_list.head.previous, None)
        self.assertEqual(self.deque.linked_list.tail.next, None)
        self.assertEqual(self.deque.pop(), 0)
        self.assertEqual(self.deque.linked_list.head, None)
        self.assertEqual(self.deque.linked_list.tail, None)
        self.assertEqual(len(self.deque), 0)
        self.assertEqual(list(self.deque), [])
        self.assertEqual(list(reversed(self.deque)), [])

        with self.assertRaises(ValueError):
            print(self.deque.pop())

    def test_pop_left(self):
        with self.assertRaises(ValueError):
            print(self.deque.pop_left())

        self.deque.append(0)
        self.deque.append(1)
        self.deque.append(2)
        self.assertEqual(self.deque.pop_left(), 0)
        self.assertEqual(self.deque.linked_list.head.previous, None)
        self.assertEqual(self.deque.linked_list.tail.next, None)
        self.assertEqual(self.deque.pop_left(), 1)
        self.assertEqual(self.deque.linked_list.head.previous, None)
        self.assertEqual(self.deque.linked_list.tail.next, None)
        self.assertEqual(self.deque.pop_left(), 2)
        self.assertEqual(self.deque.linked_list.head, None)
        self.assertEqual(self.deque.linked_list.tail, None)
        self.assertEqual(len(self.deque), 0)
        self.assertEqual(list(self.deque), [])
        self.assertEqual(list(reversed(self.deque)), [])

        with self.assertRaises(ValueError):
            print(self.deque.pop_left())

    def test(self):
        self.deque.append(0)
        self.deque.append(1)
        self.assertEqual(self.deque.pop(), 1)
        self.deque.append(2)
        self.deque.append_left(-1)
        self.assertEqual(self.deque.pop_left(), -1)
        self.deque.append_left(-2)
        self.deque.append_left(-3)

        self.assertEqual(self.deque.linked_list.head.value, -3)
        self.assertEqual(self.deque.linked_list.tail.value, 2)


if __name__ == '__main__':
    unittest.main()
