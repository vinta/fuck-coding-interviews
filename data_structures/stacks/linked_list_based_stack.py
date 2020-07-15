# coding: utf-8
"""
LIFO: last in, first out
append left, pop left
"""


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

    # O(n)
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
