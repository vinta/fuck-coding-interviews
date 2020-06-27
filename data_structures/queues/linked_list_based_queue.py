# coding: utf-8
import unittest


class ListNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


# Also see: https://github.com/vinta/fuck-coding-interviews/blob/master/data_structures/linked_lists/singly_linked_list.py
# This implementation is more simplified, however, with some modifications
class LinkedList:
    def __init__(self, head=None, tail=None):
        self.head = None
        self.tail = None
        self.size = 0

    def __len__(self):
        return self.size

    def __bool__(self):
        return bool(self.size)

    def __iter__(self):
        node = self.head
        while node:
            yield node.value
            node = node.next

    def new_node(self, value):
        return ListNode(value)

    def append(self, value):
        new_node = self.new_node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            self.size += 1
            return

        self.tail.next = new_node
        self.tail = new_node
        self.size += 1

    def pop_head(self):
        if not self.head:
            raise IndexError

        deleted_value = self.head.value
        self.head = self.head.next
        self.size -= 1
        return deleted_value


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
            return self.linked_list.pop_head()
        except IndexError:
            raise ValueError('Queue is empty')


class TestCase(unittest.TestCase):
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

        with self.assertRaises(ValueError):
            print(self.queue.dequeue())


if __name__ == '__main__':
    unittest.main()
