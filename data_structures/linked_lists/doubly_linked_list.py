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

    def insert_at_index(self, index, value):
        new_node = DoublyListNode(value)

        if index == 0:
            new_node.next = self.head
            self.head.previous = new_node
            self.head = new_node

        elif index > 0:
            current_node = self.head
            current_index = 0
            while current_node:
                if current_index == index:
                    new_node.previous = current_node.previous
                    new_node.next = current_node
                    current_node.previous = new_node
                    return

                current_node = current_node.next
                current_index += 1

            raise IndexError

        elif index < 0:
            current_node = self.tail
            current_index = -1
            while current_node:

                current_node = current_node.previous

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
        self.node_3.next = None
        self.node_0.previous = None
        self.node_1.previous = self.node_0
        self.node_2.previous = self.node_1
        self.node_3.previous = self.node_2
        self.doubly_linked_list = DoublyLinkedList(head=self.node_0, tail=self.node_3)

    def test(self):
        pass


if __name__ == '__main__':
    unittest.main()
