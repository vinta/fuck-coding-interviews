# coding: utf-8
"""
LIFO: last in, first out
append left, pop left
"""
import unittest


class ListNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


# Also see: https://github.com/vinta/fuck-coding-interviews/blob/master/data_structures/linked_lists/singly_linked_list.py
# This implementation is more simplified, however, with specific modifications
class LinkedList:
    def __init__(self, head=None):
        self.head = None
        self.size = 0

    def __len__(self):
        return self.size

    def __iter__(self):
        node = self.head
        while node:
            yield node.value
            node = node.next

    def append_left(self, value):
        self.size += 1
        new_node = ListNode(value)

        if not self.head:
            self.head = new_node
            return

        new_node.next = self.head
        self.head = new_node

    def pop_left(self):
        if not self.head:
            raise IndexError

        self.size -= 1
        deleted_value = self.head.value
        self.head = self.head.next
        return deleted_value


class LinkedListBasedStack:
    def __init__(self):
        self.linked_list = LinkedList()

    # O(1)
    def __len__(self):
        return len(self.linked_list)

    def __iter__(self):
        for item in self.linked_list:
            yield item

    # O(1)
    def push(self, value):
        self.linked_list.append_left(value)

    # O(1)
    def pop(self):
        try:
            return self.linked_list.pop_left()
        except IndexError:
            raise ValueError('Stack is empty')

    # O(1)
    def peek(self):
        if not self.linked_list.head:
            raise ValueError('Stack is empty')

        return self.linked_list.head.value


class TestCase(unittest.TestCase):
    def setUp(self):
        self.stack = LinkedListBasedStack()

    def test__len__(self):
        self.assertEqual(len(self.stack), 0)

        self.stack.push(0)
        self.assertEqual(len(self.stack), 1)

    def test_push(self):
        self.stack.push(0)
        self.stack.push(1)
        self.stack.push(2)
        self.assertEqual(len(self.stack), 3)
        self.assertEqual(list(self.stack), [2, 1, 0])

    def test_pop(self):
        with self.assertRaises(ValueError):
            print(self.stack.pop())

        self.stack.push(0)
        self.stack.push(1)
        self.stack.push(2)
        self.assertEqual(self.stack.pop(), 2)
        self.assertEqual(self.stack.pop(), 1)
        self.assertEqual(self.stack.pop(), 0)
        self.assertEqual(len(self.stack), 0)
        self.assertEqual(list(self.stack), [])

        with self.assertRaises(ValueError):
            print(self.stack.pop())

    def test_peek(self):
        with self.assertRaises(ValueError):
            print(self.stack.peek())

        self.stack.push(0)
        self.stack.push(1)
        self.stack.push(2)
        self.assertEqual(self.stack.peek(), 2)


if __name__ == '__main__':
    unittest.main()
