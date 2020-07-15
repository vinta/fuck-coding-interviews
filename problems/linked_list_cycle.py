# coding: utf-8
"""
https://leetcode.com/problems/linked-list-cycle/
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        visted_ids = set()

        node = head
        while node:
            node_id = id(node)
            if node_id in visted_ids:
                return True
            else:
                visted_ids.add(node_id)

            node = node.next

        return False
