# coding: utf-8
class ListNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    # O(n)
    def __len__(self):
        length = 0
        current_node = self.head
        while current_node:
            length += 1
            current_node = current_node.next

        return length

    # O(n)
    def __iter__(self):
        current_node = self.head
        while current_node:
            yield current_node.value
            current_node = current_node.next

    # O(n)
    def __getitem__(self, index):
        if index < 0:
            raise ValueError('Negative index is yet not supported')

        current_index = 0
        current_node = self.head
        while current_node:
            if current_index == index:
                return current_node.value
            else:
                current_node = current_node.next
                current_index += 1

        raise IndexError

    # O(n)
    def __setitem__(self, index, value):
        if index < 0:
            raise ValueError('Negative index is yet not supported')

        current_node = self.head
        current_index = 0
        while current_node:
            if current_index == index:
                current_node.value = value
                return
            current_node = current_node.next
            current_index += 1

        raise IndexError

    # O(n)
    # O(1) if it inserts before the first item
    def insert_before(self, index, value):
        if index < 0:
            raise ValueError('Negative index is yet not supported')

        new_node = ListNode(value)
        if not self.head:
            self.head = new_node
            return

        if index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            current_node = self.head
            current_index = 0
            while current_node:
                # We find the node that before the node at the index we are looking for
                if current_index == index - 1:
                    target_node = current_node.next
                    current_node.next = new_node
                    new_node.next = target_node
                    return

                current_node = current_node.next
                current_index += 1

            raise IndexError

    # O(n)
    # O(1) if it pops the first item
    def pop(self, index):
        if index < 0:
            raise ValueError('Negative index is yet not supported')

        if index == 0:
            if not self.head:
                raise IndexError('pop from empty linked list')

            deleted_value = self.head.value
            self.head = self.head.next
            return deleted_value
        else:
            previous_node = self.head
            current_node = self.head.next
            current_index = 1
            while current_node:
                if current_index == index:
                    deleted_value = current_node.value
                    previous_node.next = current_node.next
                    return deleted_value

                previous_node = current_node
                current_node = current_node.next
                current_index += 1

            raise IndexError

    # O(n)
    def index(self, value):
        current_index = 0
        current_node = self.head
        while current_node:
            if current_node.value == value:
                return current_index
            current_node = current_node.next
            current_index += 1

        raise ValueError(f'{value} is not in linked list')

    # O(n)
    def append(self, value):
        new_node = ListNode(value)
        if not self.head:
            self.head = new_node
            return

        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node

    # O(n)
    def reverse(self):
        previous_node = None
        current_node = self.head
        while current_node:
            next_node = current_node.next
            current_node.next = previous_node
            previous_node = current_node
            current_node = next_node

        self.head = previous_node
