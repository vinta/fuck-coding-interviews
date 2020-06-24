# coding: utf-8
"""
https://leetcode.com/problems/reverse-linked-list/
"""
import unittest

from utils.leetcode import list_to_listnode
from utils.leetcode import listnode_to_list


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        node = head
        previous_node = None
        while node:
            next_node = node.next
            node.next = previous_node
            previous_node = node
            node = next_node

        return previous_node


class Solution2:
    def reverseList(self, head: ListNode) -> ListNode:
        def reverse(node, previous_node):
            if not node:
                return previous_node
            next_node = node.next
            node.next = previous_node
            return reverse(next_node, node)

        return reverse(head, previous_node=None)


class TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test(self):
        head = list_to_listnode([1, 2, 3, 4, 5])
        expected_head = self.solution.reverseList(head)
        expected = [5, 4, 3, 2, 1]
        self.assertEqual(listnode_to_list(expected_head), expected)


if __name__ == '__main__':
    unittest.main()
