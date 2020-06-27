# coding: utf-8
import unittest

from data_structures.linked_lists.singly_linked_list import LinkedList


class DoublyListNode:
    def __init__(self, value, next=None, previous=None):
        self.value = value
        self.next = next
        self.previous = previous


# TODO: Override other methods to support negative indexes
class DoublyLinkedList(LinkedList):
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def __getitem__(self, index):
        if index < 0:
            current_node = self.tail
            current_index = -1
            while current_node:
                if current_index == index:
                    return current_node.value

                current_node = current_node.previous
                current_index = current_index - 1

            raise IndexError
        else:
            return super().__getitem__(index)

    def __reverse__(self):
        current_node = self.tail
        while current_node:
            yield current_node.value
            current_node = current_node.previous

    def append(self, value):
        new_node = DoublyListNode(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            return

        new_node.previous = self.tail
        self.tail.next = new_node
        self.tail = new_node

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

    def test__getitem__(self):
        with self.assertRaises(IndexError):
            print(self.empty_linked_list[-1])

        self.assertEqual(self.linked_list[0], self.node_0.value)
        self.assertEqual(self.linked_list[1], self.node_1.value)
        self.assertEqual(self.linked_list[2], self.node_2.value)
        self.assertEqual(self.linked_list[3], self.node_3.value)

        self.assertEqual(self.linked_list[-1], self.node_3.value)
        self.assertEqual(self.linked_list[-2], self.node_2.value)
        self.assertEqual(self.linked_list[-3], self.node_1.value)
        self.assertEqual(self.linked_list[-4], self.node_0.value)

        with self.assertRaises(IndexError):
            print(self.linked_list[-5])

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

    def test_append(self):
        self.linked_list.append('4')
        expected = [
            self.node_0.value,
            self.node_1.value,
            self.node_2.value,
            self.node_3.value,
            '4',
        ]
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
        self.assertEqual(list(self.linked_list), expected)


if __name__ == '__main__':
    unittest.main()
