# coding: utf-8
import unittest


class DoublyListNode:
    def __init__(self, value, next=None, previous=None):
        self.value = value
        self.next = next
        self.previous = previous


# Also see: https://github.com/vinta/fuck-coding-interviews/blob/master/data_structures/linked_lists/doubly_linked_list.py
# This implementation is more simplified, however, with specific modifications
class DoublyLinkedList:
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def __iter__(self):
        node = self.head
        while node:
            yield node.value
            node = node.next

    def __reversed__(self):
        node = self.tail
        while node:
            yield node.value
            node = node.previous

    def append(self, value):
        new_node = DoublyListNode(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            return

        new_node.previous = self.tail
        self.tail.next = new_node
        self.tail = new_node

    def append_left(self, value):
        new_node = DoublyListNode(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            return

        new_node.next = self.head
        self.head.previous = new_node
        self.head = new_node

    def delete_node(self, node):
        if not self.tail:
            raise ValueError

        deleted_value = node.value

        if node.next:
            node.next.previous = node.previous
        else:
            if node.previous:
                self.tail = node.previous
            else:
                self.tail = None

        if node.previous:
            node.previous.next = node.next
        else:
            if node.next:
                self.head = node.next
            else:
                self.head = None

        return deleted_value

    def pop(self):
        return self.delete_node(self.tail)

    def pop_left(self):
        return self.delete_node(self.head)


# Double-ended queue
class DoublyLinkedListBasedDeque:
    def __init__(self):
        self.linked_list = DoublyLinkedList()

    def __iter__(self):
        return self.linked_list.__iter__()

    def __reversed__(self):
        return self.linked_list.__reversed__()

    def append(self, value):
        self.linked_list.append(value)

    def append_left(self, value):
        self.linked_list.append_left(value)

    def pop(self):
        return self.linked_list.pop()

    def pop_left(self):
        return self.linked_list.pop_left()


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
