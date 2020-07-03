# coding: utf-8
"""
FIFO: first in, first out
append, pop left
"""
import unittest


class ListNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


# Also see: https://github.com/vinta/fuck-coding-interviews/blob/master/data_structures/linked_lists/singly_linked_list.py
# This implementation is more simplified, however, with specific modifications
class LinkedList:
    def __init__(self, head=None, tail=None):
        self.head = None
        self.tail = None
        self.size = 0

    def __len__(self):
        return self.size

    def __iter__(self):
        node = self.head
        while node:
            yield node.value
            node = node.next

    def append(self, value):
        self.size += 1
        new_node = ListNode(value)

        if not self.head:
            self.head = new_node
            self.tail = new_node
            return

        self.tail.next = new_node
        self.tail = new_node

    def pop_left(self):
        if not self.head:
            raise IndexError

        self.size -= 1
        deleted_value = self.head.value
        self.head = self.head.next
        if not self.head:
            self.tail = None

        return deleted_value


class LinkedListBasedQueue:
    def __init__(self):
        self.linked_list = LinkedList()

    # O(1)
    def __len__(self):
        return len(self.linked_list)

    # O(n)
    def __iter__(self):
        return self.linked_list.__iter__()

    # O(1)
    def enqueue(self, value):
        self.linked_list.append(value)

    # O(1)
    def dequeue(self):
        try:
            return self.linked_list.pop_left()
        except IndexError:
            raise ValueError('Queue is empty')


class TestCase(unittest.TestCase):
    def setUp(self):
        self.queue = LinkedListBasedQueue()

    def test_enqueue(self):
        self.queue.enqueue(0)
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.assertEqual(self.queue.linked_list.head.value, 0)
        self.assertEqual(self.queue.linked_list.tail.value, 2)
        self.assertEqual(len(self.queue), 3)
        self.assertEqual(list(self.queue), [0, 1, 2])

    def test_dequeue(self):
        with self.assertRaises(ValueError):
            print(self.queue.dequeue())

        self.queue.enqueue(0)
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.assertEqual(self.queue.dequeue(), 0)
        self.assertEqual(self.queue.linked_list.head.value, 1)
        self.assertEqual(self.queue.linked_list.tail.value, 2)
        self.assertEqual(self.queue.dequeue(), 1)
        self.assertEqual(self.queue.linked_list.head.value, 2)
        self.assertEqual(self.queue.linked_list.tail.value, 2)
        self.assertEqual(self.queue.dequeue(), 2)
        self.assertEqual(self.queue.linked_list.head, None)
        self.assertEqual(self.queue.linked_list.tail, None)
        self.assertEqual(len(self.queue), 0)
        self.assertEqual(list(self.queue), [])

        with self.assertRaises(ValueError):
            print(self.queue.dequeue())


if __name__ == '__main__':
    unittest.main()
