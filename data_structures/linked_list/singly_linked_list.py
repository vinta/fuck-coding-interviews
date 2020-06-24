# coding: utf-8
import unittest


class ListNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self, head):
        self.head = head

    def node_of_index(self, index):
        # TODO: Support negative indexes
        if index < 0:
            raise IndexError

        current_index = 0
        current_node = self.head
        while current_node:
            if current_index == index:
                return current_node
            else:
                current_node = current_node.next
                current_index += 1

        raise IndexError

    def value_of_index(self, index):
        return self.node_of_index(index).value

    def index_of_value(self, value):
        current_index = 0
        current_node = self.head
        while current_node:
            if current_node.value == value:
                return current_index
            current_node = current_node.next
            current_index += 1

        return None

    def insert_at_index(self, index, value):
        pass

    def delete_at_index(self, index):
        pass


class TestCase(unittest.TestCase):
    def setUp(self):
        self.node_0 = ListNode('once')
        self.node_1 = ListNode('upon')
        self.node_2 = ListNode('a')
        self.node_3 = ListNode('time')
        self.node_0.next = self.node_1
        self.node_1.next = self.node_2
        self.node_2.next = self.node_3

        self.linked_list = LinkedList(self.node_0)

    def test_value_of_index(self):
        self.assertEqual(self.linked_list.value_of_index(0), self.node_0.value)
        self.assertEqual(self.linked_list.value_of_index(1), self.node_1.value)
        self.assertEqual(self.linked_list.value_of_index(2), self.node_2.value)
        self.assertEqual(self.linked_list.value_of_index(3), self.node_3.value)

        with self.assertRaises(IndexError):
            self.linked_list.value_of_index(-1)

        with self.assertRaises(IndexError):
            self.linked_list.value_of_index(4)

        with self.assertRaises(IndexError):
            self.linked_list.value_of_index(100)

    def test_index_of_value(self):
        self.assertEqual(self.linked_list.index_of_value('once'), 0)
        self.assertEqual(self.linked_list.index_of_value('upon'), 1)
        self.assertEqual(self.linked_list.index_of_value('a'), 2)
        self.assertEqual(self.linked_list.index_of_value('time'), 3)
        self.assertEqual(self.linked_list.index_of_value('NOT EXIST'), None)


if __name__ == '__main__':
    unittest.main()
