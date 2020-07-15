# coding: utf-8
"""
https://leetcode.com/problems/reverse-linked-list/
"""


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
