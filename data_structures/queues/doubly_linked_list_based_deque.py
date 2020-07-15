# coding: utf-8
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
        self.size = 0

    def __len__(self):
        return self.size

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
        self.size += 1
        new_node = DoublyListNode(value)

        if not self.head:
            self.head = new_node
            self.tail = new_node
            return

        new_node.previous = self.tail
        self.tail.next = new_node
        self.tail = new_node

    def append_left(self, value):
        self.size += 1
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

        self.size -= 1
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

    # O(1)
    def __len__(self):
        return len(self.linked_list)

    # O(n)
    def __iter__(self):
        return self.linked_list.__iter__()

    # O(n)
    def __reversed__(self):
        return self.linked_list.__reversed__()

    # O(1)
    def append(self, value):
        self.linked_list.append(value)

    # O(1)
    def append_left(self, value):
        self.linked_list.append_left(value)

    # O(1)
    def pop(self):
        return self.linked_list.pop()

    # O(1)
    def pop_left(self):
        return self.linked_list.pop_left()
