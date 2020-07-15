# coding: utf-8
import unittest

from data_structures.linked_lists.doubly_linked_list import DoublyLinkedList
from data_structures.linked_lists.doubly_linked_list import DoublyListNode


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
