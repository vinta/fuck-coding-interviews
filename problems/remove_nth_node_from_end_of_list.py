# coding: utf-8
"""
https://leetcode.com/problems/remove-nth-node-from-end-of-list/
"""
import unittest

from problems.utils.leetcode import listnode_to_list
from problems.utils.leetcode import list_to_listnode


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        array = []
        node = head
        while node:
            array.append(node)
            node = node.next

        removed_node = array[-n]

        # If a node has no previous, it means the node is the head
        try:
            previous_node = array[-(n + 1)]
        except IndexError:
            head = removed_node.next
        else:
            previous_node.next = removed_node.next

        return head


class Solution2:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # Calculate the length of the LinkedList in a full while loop
        length = 0
        node = head
        while node:
            length += 1
            node = node.next

        if length <= 1:
            return None

        # Convert the negative index to the 0-based index
        deleted_index = length - n

        if deleted_index == 0:
            head = head.next
            return head

        # Start from the head, and find the previous node of the node we're going to delete
        index = 0
        node = head
        while node:
            if index == deleted_index - 1:
                previous_node = node
                deleted_node = node.next
                previous_node.next = deleted_node.next
                return head

            index += 1
            node = node.next

        return head


class TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test(self):
        head = list_to_listnode([1, 2, 3, 4, 5])
        n = 2
        expected_head = self.solution.removeNthFromEnd(head, n)
        expected = [1, 2, 3, 5]
        self.assertEqual(listnode_to_list(expected_head), expected)

    def test2(self):
        head = list_to_listnode([1, 2, 3, 4, 5])
        n = 1
        expected_head = self.solution.removeNthFromEnd(head, n)
        expected = [1, 2, 3, 4]
        self.assertEqual(listnode_to_list(expected_head), expected)

    def test3(self):
        head = list_to_listnode([1, 2])
        n = 2
        expected_head = self.solution.removeNthFromEnd(head, n)
        expected = [2]
        self.assertEqual(listnode_to_list(expected_head), expected)

    def test4(self):
        head = list_to_listnode([1])
        n = 1
        expected_head = self.solution.removeNthFromEnd(head, n)
        expected = []
        self.assertEqual(listnode_to_list(expected_head), expected)


class TestCase2(unittest.TestCase):
    def setUp(self):
        self.solution = Solution2()

    def test(self):
        head = list_to_listnode([1, 2, 3, 4, 5])
        n = 2
        expected_head = self.solution.removeNthFromEnd(head, n)
        expected = [1, 2, 3, 5]
        self.assertEqual(listnode_to_list(expected_head), expected)

    def test2(self):
        head = list_to_listnode([1, 2, 3, 4, 5])
        n = 1
        expected_head = self.solution.removeNthFromEnd(head, n)
        expected = [1, 2, 3, 4]
        self.assertEqual(listnode_to_list(expected_head), expected)

    def test3(self):
        head = list_to_listnode([1, 2])
        n = 2
        expected_head = self.solution.removeNthFromEnd(head, n)
        expected = [2]
        self.assertEqual(listnode_to_list(expected_head), expected)

    def test4(self):
        head = list_to_listnode([1])
        n = 1
        expected_head = self.solution.removeNthFromEnd(head, n)
        expected = []
        self.assertEqual(listnode_to_list(expected_head), expected)


if __name__ == '__main__':
    unittest.main()
