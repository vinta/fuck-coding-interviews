# coding: utf-8
import unittest

from singly_linked_list import LinkedList


class DoublyListNode:
    def __init__(self, value, next=None, previous=None):
        self.value = value
        self.next = next
        self.previous = previous


class DoublyLinkedList(LinkedList):
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def insert_at_end(self, value):
        new_node = DoublyListNode(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.previous = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def remove_from_front(self):
        pass


class TestCase(unittest.TestCase):
    def setUp(self):
        self.empty_doubly_linked_list = DoublyLinkedList()

        self.node_0 = DoublyListNode('nobody exists on purpose')
        self.node_1 = DoublyListNode('nobody belongs anywhere')
        self.node_2 = DoublyListNode('everybody is gonna die')
        self.node_3 = DoublyListNode('come writing Python')
        self.node_0.next = self.node_1
        self.node_1.next = self.node_2
        self.node_2.next = self.node_3
        self.node_1.previous = self.node_0
        self.node_2.previous = self.node_1
        self.node_3.previous = self.node_2
        self.doubly_linked_list = DoublyLinkedList(head=self.node_0, tail=self.node_3)

    def test(self):
        pass


if __name__ == '__main__':
    unittest.main()
