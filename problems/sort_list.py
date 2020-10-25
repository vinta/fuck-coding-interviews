# coding: utf-8
"""
https://leetcode.com/problems/sort-list/
"""


class ListNode:  # pragma: no cover
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        def to_list(node):
            arr = []
            while node:
                arr.append(node.val)
                node = node.next
            return arr

        def to_node(arr):
            node = dummy_head = ListNode()
            for item in arr:
                node.next = ListNode(item)
                node = node.next
            return dummy_head.next

        arr = to_list(head)
        sorted_arr = sorted(arr)
        return to_node(sorted_arr)
