# coding: utf-8
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
    def __reversed__(self):
        current_node = self.tail
        while current_node:
            yield current_node.value
            current_node = current_node.previous

    # O(n)
    # O(1) if it inserts before the first or the last item
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

    # O(n)
    # O(1) if it pops the first or the last item
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
