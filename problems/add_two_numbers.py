# coding: utf-8
"""
https://leetcode.com/problems/add-two-numbers/
"""
import unittest

from problems.utils.leetcode import list_to_listnode
from problems.utils.leetcode import listnode_to_list


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        result_node = ListNode()
        dummy_head_result_node = result_node

        carry = 0
        while l1 or l2:
            # the length of `l1` and `l2` might be different
            if l1:
                value1 = l1.val
                next1 = l1.next
            else:
                value1 = 0
                next1 = None
            if l2:
                value2 = l2.val
                next2 = l2.next
            else:
                value2 = 0
                next2 = None

            val = value1 + value2 + carry
            if val >= 10:
                val = val - 10
                carry = 1
            else:
                carry = 0

            # in the first loop, `result_node` is currently `dummy_head_result_node`
            next_result_node = ListNode(val)
            result_node.next = next_result_node

            # prepare for the next loop
            result_node = next_result_node
            l1 = next1
            l2 = next2

        if carry >= 1:
            result_node.next = ListNode(carry)

        return dummy_head_result_node.next


class TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test(self):
        l1 = list_to_listnode([2, 4, 3])
        l2 = list_to_listnode([5, 6, 4])
        expected_head = self.solution.addTwoNumbers(l1, l2)
        expected = [7, 0, 8]
        self.assertEqual(listnode_to_list(expected_head), expected)

    def test2(self):
        l1 = list_to_listnode([0, 1, 0, 9])
        l2 = list_to_listnode([1, 9, 9])
        expected_head = self.solution.addTwoNumbers(l1, l2)
        expected = [1, 0, 0, 0, 1]
        self.assertEqual(listnode_to_list(expected_head), expected)


if __name__ == '__main__':
    unittest.main()
