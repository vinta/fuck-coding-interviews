# coding: utf-8
import unittest


class DoublyListNode:
    def __init__(self, value, next=None, previous=None):
        self.value = value
        self.next = next
        self.previous = previous


# Also see: https://github.com/vinta/fuck-coding-interviews/blob/master/data_structures/linked_lists/doubly_linked_list.py
# This implementation is more simplified, however, with some modifications
class DoublyLinkedList:
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail
        self.size = 0

    def __len__(self):
        return self.size

    def __bool__(self):
        return bool(self.size)

    def __reversed__(self):
        node = self.tail
        while node:
            yield node.value
            node = node.previous

    def new_node(self, value):
        return DoublyListNode(value)

    def append(self, value):
        new_node = self.new_node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            self.size += 1
            return

        new_node.previous = self.tail
        self.tail.next = new_node
        self.tail = new_node
        self.size += 1

    def pop(self):
        if not self.head:
            raise IndexError

        deleted_value = self.tail.value
        previous_node = self.tail.previous
        if previous_node:
            previous_node.next = None
            self.tail = previous_node
        else:
            self.head = None
            self.tail = None
        self.size -= 1
        return deleted_value


class DoublyLinkedListBasedStack:
    def __init__(self):
        self.linked_list = DoublyLinkedList()

    def __len__(self):
        return len(self.linked_list)

    def __bool__(self):
        return bool(self.linked_list)

    def __iter__(self):
        for item in reversed(self.linked_list):
            yield item

    def push(self, value):
        self.linked_list.append(value)

    def pop(self):
        try:
            return self.linked_list.pop()
        except IndexError:
            raise ValueError('Stack is empty')

    def peek(self):
        tail = self.linked_list.tail
        if tail:
            return tail.value
        raise ValueError('Stack is empty')


class TestCase(unittest.TestCase):
    def setUp(self):
        self.stack = DoublyLinkedListBasedStack()

    def test__len__(self):
        self.assertEqual(len(self.stack), 0)

        self.stack.push(0)
        self.assertEqual(len(self.stack), 1)

    def test__bool__(self):
        self.assertFalse(self.stack)

        self.stack.push(0)
        self.assertTrue(self.stack)

    def test_push(self):
        self.stack.push(0)
        self.stack.push(1)
        self.stack.push(2)
        self.assertEqual(list(self.stack), [2, 1, 0])
        self.assertEqual(len(self.stack), 3)

    def test_pop(self):
        with self.assertRaises(ValueError):
            print(self.stack.pop())

        self.stack.push(0)
        self.stack.push(1)
        self.stack.push(2)
        self.assertEqual(self.stack.pop(), 2)
        self.assertEqual(self.stack.pop(), 1)
        self.assertEqual(self.stack.pop(), 0)
        self.assertEqual(list(self.stack), [])
        self.assertEqual(len(self.stack), 0)

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
