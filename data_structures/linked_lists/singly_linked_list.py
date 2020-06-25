# coding: utf-8
import unittest


class ListNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def __repr__(self):
        pass

    def __str__(self):
        pass

    def __bool__(self):
        pass

    def __len__(self):
        length = 0
        current_node = self.head
        while current_node:
            length += 1
            current_node = current_node.next

        return length

    def __iter__(self):
        current_node = self.head
        while current_node:
            # TODO: Should we yield the node itself?
            yield current_node.value
            current_node = current_node.next

    def reverse(self):
        node = None
        current_node = self.head
        while current_node:
            next_node = current_node.next
            current_node.next = node
            node = current_node
            current_node = next_node

        # TODO:
        # We can cache the reversed version as self._reversed,
        # but we need to invalidate cache when the LinkedList changes
        return LinkedList(node)

    def __reversed__(self):
        reversed_linked_list = self.reverse()
        current_node = reversed_linked_list.head
        while current_node:
            yield current_node.value
            current_node = current_node.next

    def __getitem__(self, index):
        pass

    def __setitem__(self, index, value):
        pass

    # TODO
    def append(self, value):
        pass

    def prepend(self, value):
        pass

    def insert(self, index, value):
        pass

    def pop(self, index):
        pass

    def index(self, value):
        pass

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
        # TODO: Support negative indexes
        if index < 0:
            raise IndexError

        new_node = ListNode(value)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            current_node = self.head
            current_index = 0
            while current_node:
                # We find the node that before the node at the index we are looking for
                if current_index == index - 1:
                    next_node = current_node.next
                    current_node.next = new_node
                    new_node.next = next_node
                    return

                current_node = current_node.next
                current_index += 1

            raise IndexError

    def delete_at_index(self, index):
        if index == 0:
            if not self.head:
                raise IndexError

            self.head = self.head.next
        else:
            current_node = self.head
            current_index = 0
            while current_node:
                # We find the node that before the node at the index we are looking for
                if current_index == index - 1:
                    deleted_node = current_node.next
                    if not deleted_node:
                        raise IndexError

                    next_node = deleted_node.next
                    current_node.next = next_node
                    return

                current_node = current_node.next
                current_index += 1

            raise IndexError


class TestCase(unittest.TestCase):
    def setUp(self):
        self.empty_linked_list = LinkedList()

        self.node_0 = ListNode('nobody exists on purpose')
        self.node_1 = ListNode('nobody belongs anywhere')
        self.node_2 = ListNode('everybody is gonna die')
        self.node_3 = ListNode('come writing Python')
        self.node_0.next = self.node_1
        self.node_1.next = self.node_2
        self.node_2.next = self.node_3
        self.linked_list = LinkedList(self.node_0)

    def test__len__(self):
        self.assertEqual(len(self.empty_linked_list), 0)
        self.assertEqual(len(self.linked_list), 4)

    def test__iter__(self):
        self.assertEqual(list(self.empty_linked_list), [])
        self.assertEqual(list(self.linked_list), [self.node_0.value, self.node_1.value, self.node_2.value, self.node_3.value])

    def test_reverse(self):
        reversed_linked_list = self.linked_list.reverse()
        self.assertEqual(list(reversed_linked_list), [self.node_3.value, self.node_2.value, self.node_1.value, self.node_0.value])

    def test__reversed__(self):
        self.assertEqual(list(reversed(self.linked_list)), [self.node_3.value, self.node_2.value, self.node_1.value, self.node_0.value])

    def test_value_of_index(self):
        with self.assertRaises(IndexError):
            self.empty_linked_list.value_of_index(0)

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
        self.assertEqual(self.empty_linked_list.index_of_value('NOT EXIST'), None)

        self.assertEqual(self.linked_list.index_of_value(self.node_0.value), 0)
        self.assertEqual(self.linked_list.index_of_value(self.node_1.value), 1)
        self.assertEqual(self.linked_list.index_of_value(self.node_2.value), 2)
        self.assertEqual(self.linked_list.index_of_value(self.node_3.value), 3)

        self.assertEqual(self.linked_list.index_of_value('NOT EXIST'), None)

    def test_insert_at_index(self):
        self.empty_linked_list.insert_at_index(0, '0')
        self.assertEqual(self.empty_linked_list.value_of_index(0), '0')

        self.linked_list.insert_at_index(0, '0')
        self.assertEqual(self.linked_list.value_of_index(0), '0')
        self.assertEqual(self.linked_list.value_of_index(1), self.node_0.value)
        self.assertEqual(self.linked_list.value_of_index(2), self.node_1.value)
        self.assertEqual(self.linked_list.value_of_index(3), self.node_2.value)
        self.assertEqual(self.linked_list.value_of_index(4), self.node_3.value)

        self.linked_list.insert_at_index(2, '2')
        self.assertEqual(self.linked_list.value_of_index(0), '0')
        self.assertEqual(self.linked_list.value_of_index(1), self.node_0.value)
        self.assertEqual(self.linked_list.value_of_index(2), '2')
        self.assertEqual(self.linked_list.value_of_index(3), self.node_1.value)
        self.assertEqual(self.linked_list.value_of_index(4), self.node_2.value)
        self.assertEqual(self.linked_list.value_of_index(5), self.node_3.value)

        self.linked_list.insert_at_index(5, '5')
        self.assertEqual(self.linked_list.value_of_index(5), '5')
        self.assertEqual(self.linked_list.value_of_index(6), self.node_3.value)

        self.linked_list.insert_at_index(7, '7')
        self.assertEqual(self.linked_list.value_of_index(7), '7')

        self.assertEqual(len(self.linked_list), 8)

        with self.assertRaises(IndexError):
            self.linked_list.insert_at_index(9, '9')

        with self.assertRaises(IndexError):
            self.linked_list.insert_at_index(100, '100')

        with self.assertRaises(IndexError):
            self.linked_list.insert_at_index(-1, '-1')

    def test_delete_at_index(self):
        with self.assertRaises(IndexError):
            self.empty_linked_list.delete_at_index(0)

        self.linked_list.delete_at_index(0)
        self.assertEqual(self.linked_list.value_of_index(0), self.node_1.value)
        self.assertEqual(self.linked_list.value_of_index(1), self.node_2.value)
        self.assertEqual(self.linked_list.value_of_index(2), self.node_3.value)

        self.linked_list.delete_at_index(1)
        self.assertEqual(self.linked_list.value_of_index(0), self.node_1.value)
        self.assertEqual(self.linked_list.value_of_index(1), self.node_3.value)

        self.assertEqual(len(self.linked_list), 2)

        self.linked_list.delete_at_index(1)
        self.linked_list.delete_at_index(0)

        self.assertEqual(len(self.linked_list), 0)

        with self.assertRaises(IndexError):
            self.linked_list.delete_at_index(2)

        with self.assertRaises(IndexError):
            self.linked_list.delete_at_index(100)

        with self.assertRaises(IndexError):
            self.linked_list.delete_at_index(-1)


if __name__ == '__main__':
    unittest.main()
