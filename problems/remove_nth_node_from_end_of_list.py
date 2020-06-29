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


if __name__ == '__main__':
    unittest.main()
