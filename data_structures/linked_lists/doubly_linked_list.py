# coding: utf-8
import unittest

from data_structures.linked_lists.singly_linked_list import LinkedList


class DoublyListNode:
    def __init__(self, value=None, next=None, previous=None):
        self.value = value
        self.next = next
        self.previous = previous


class DoublyLinkedList(LinkedList):
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    # O(n)
    def __reverse__(self):
        current_node = self.tail
        while current_node:
            yield current_node.value
            current_node = current_node.previous

    # O(n), O(1) if it inserts before the first or the last item
    def insert_before(self, index, value):
        new_node = DoublyListNode(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            return

        if index >= 0:
            current_node = self.head
            current_index = 0
            index_step = 1
            get_next_node = lambda node: node.next
        else:
            current_node = self.tail
            current_index = -1
            index_step = -1
            get_next_node = lambda node: node.previous

        while current_node:
            if current_index == index:
                new_node.next = current_node
                new_node.previous = current_node.previous
                if current_node.previous:
                    current_node.previous.next = new_node
                else:
                    self.head = new_node
                current_node.previous = new_node
                return

            current_node = get_next_node(current_node)
            current_index += index_step

        raise IndexError

    # O(n), O(1) if it pops the first or the last item
    def pop(self, index):
        if not self.head:
            raise IndexError('pop from empty linked list')

        if index >= 0:
            current_node = self.head
            current_index = 0
            index_step = 1
            get_next_node = lambda node: node.next
        else:
            current_node = self.tail
            current_index = -1
            index_step = -1
            get_next_node = lambda node: node.previous

        while current_node:
            if current_index == index:
                deleted_value = current_node.value
                next_node = current_node.next
                previous_node = current_node.previous

                if next_node:
                    next_node.previous = previous_node
                if previous_node:
                    previous_node.next = next_node

                if current_node == self.head:
                    self.head = next_node
                if current_node == self.tail:
                    self.tail = previous_node

                return deleted_value

            current_node = get_next_node(current_node)
            current_index += index_step

        raise IndexError

    # O(1)
    def append(self, value):
        new_node = DoublyListNode(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            return

        new_node.previous = self.tail
        self.tail.next = new_node
        self.tail = new_node

    # O(n)
    def reverse(self):
        current_node = self.head
        self.head, self.tail = self.tail, self.head
        while current_node:
            next_node = current_node.next
            current_node.next, current_node.previous = current_node.previous, current_node.next
            current_node = next_node


class TestCase(unittest.TestCase):
    def setUp(self):
        self.empty_linked_list = DoublyLinkedList()

        self.node_0 = DoublyListNode('nobody exists on purpose')
        self.node_1 = DoublyListNode('nobody belongs anywhere')
        self.node_2 = DoublyListNode('everybody is gonna die')
        self.node_3 = DoublyListNode('come writing Python')
        self.node_0.next = self.node_1
        self.node_1.next = self.node_2
        self.node_2.next = self.node_3
        self.node_3.next = None
        self.node_0.previous = None
        self.node_1.previous = self.node_0
        self.node_2.previous = self.node_1
        self.node_3.previous = self.node_2
        self.linked_list = DoublyLinkedList(head=self.node_0, tail=self.node_3)

    def test__reversed__(self):
        self.assertEqual(list(reversed(self.empty_linked_list)), [])

        expected = [
            self.node_3.value,
            self.node_2.value,
            self.node_1.value,
            self.node_0.value,
        ]
        self.assertEqual(list(reversed(self.linked_list)), expected)

        expected = [
            self.node_0.value,
            self.node_1.value,
            self.node_2.value,
            self.node_3.value,
        ]
        self.assertEqual(list(self.linked_list), expected)

    def test_insert_before(self):
        self.empty_linked_list.insert_before(0, '0')
        self.assertEqual(self.empty_linked_list.head.value, '0')
        self.assertEqual(self.empty_linked_list.tail.value, '0')
        self.assertEqual(self.empty_linked_list[0], '0')

        self.linked_list.insert_before(0, '0')
        self.linked_list.insert_before(1, '1')
        self.linked_list.insert_before(3, '3')
        self.linked_list.insert_before(6, '6')
        expected = [
            '0',
            '1',
            self.node_0.value,
            '3',
            self.node_1.value,
            self.node_2.value,
            '6',
            self.node_3.value,
        ]
        self.assertEqual(self.linked_list.head.value, '0')
        self.assertEqual(self.linked_list.tail.value, self.node_3.value)
        self.assertEqual(list(self.linked_list), expected)

        with self.assertRaises(IndexError):
            self.linked_list.insert_before(10, '10')

    def test_insert_before_negative(self):
        self.empty_linked_list.insert_before(-1, '0')
        self.assertEqual(self.empty_linked_list.head.value, '0')
        self.assertEqual(self.empty_linked_list.tail.value, '0')
        self.assertEqual(self.empty_linked_list[0], '0')

        self.linked_list.insert_before(-1, '-1')
        self.linked_list.insert_before(-2, '-2')
        self.linked_list.insert_before(-6, '-6')
        expected = [
            '-6',
            self.node_0.value,
            self.node_1.value,
            self.node_2.value,
            '-2',
            '-1',
            self.node_3.value,
        ]
        self.assertEqual(self.linked_list.head.value, '-6')
        self.assertEqual(self.linked_list.tail.value, self.node_3.value)
        self.assertEqual(list(self.linked_list), expected)

        with self.assertRaises(IndexError):
            self.linked_list.insert_before(-8, '-8')

    def test_pop(self):
        with self.assertRaises(IndexError):
            print(self.empty_linked_list.pop(0))

        self.assertEqual(self.linked_list.pop(0), self.node_0.value)
        self.assertEqual(self.linked_list.pop(1), self.node_2.value)
        self.assertEqual(self.linked_list.pop(1), self.node_3.value)

        expected = [
            self.node_1.value,
        ]
        self.assertEqual(self.linked_list.head.value, self.node_1.value)
        self.assertEqual(self.linked_list.tail.value, self.node_1.value)
        self.assertEqual(list(self.linked_list), expected)

        with self.assertRaises(IndexError):
            print(self.linked_list.pop(1))

    def test_pop_negative(self):
        with self.assertRaises(IndexError):
            print(self.empty_linked_list.pop(-1))

        self.assertEqual(self.linked_list.pop(-1), self.node_3.value)
        self.assertEqual(self.linked_list.pop(-1), self.node_2.value)
        self.assertEqual(self.linked_list.pop(-2), self.node_0.value)

        expected = [
            self.node_1.value,
        ]
        self.assertEqual(self.linked_list.head.value, self.node_1.value)
        self.assertEqual(self.linked_list.tail.value, self.node_1.value)
        self.assertEqual(list(self.linked_list), expected)

        with self.assertRaises(IndexError):
            print(self.linked_list.pop(-2))

    def test_append(self):
        self.empty_linked_list.append('0')
        self.assertEqual(self.empty_linked_list.head.value, '0')
        self.assertEqual(self.empty_linked_list.tail.value, '0')
        self.assertEqual(self.empty_linked_list[0], '0')

        self.linked_list.append('4')
        self.linked_list.append('5')
        expected = [
            self.node_0.value,
            self.node_1.value,
            self.node_2.value,
            self.node_3.value,
            '4',
            '5',
        ]
        self.assertEqual(self.linked_list.head.value, self.node_0.value)
        self.assertEqual(self.linked_list.tail.value, '5')
        self.assertEqual(list(self.linked_list), expected)

    def test_reverse(self):
        self.empty_linked_list.reverse()
        self.assertEqual(list(self.empty_linked_list), [])

        self.linked_list.reverse()
        expected = [
            self.node_3.value,
            self.node_2.value,
            self.node_1.value,
            self.node_0.value,
        ]
        self.assertEqual(self.linked_list.head.value, self.node_3.value)
        self.assertEqual(self.linked_list.tail.value, self.node_0.value)
        self.assertEqual(list(self.linked_list), expected)


if __name__ == '__main__':
    unittest.main()
