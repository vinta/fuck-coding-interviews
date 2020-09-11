# coding: utf-8
"""
https://leetcode.com/problems/merge-k-sorted-lists/
"""
from typing import List
import heapq


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        def gen_nodes(node):
            while node:
                yield node
                node = node.next

        linked_lists = [gen_nodes(head) for head in lists]
        sorted_nodes = heapq.merge(*linked_lists, key=lambda node: node.val)
        dummy_head = last_node = ListNode()
        for node in sorted_nodes:
            last_node.next = node
            last_node = node

        return dummy_head.next
