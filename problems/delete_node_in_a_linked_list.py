# coding: utf-8
"""
https://leetcode.com/problems/delete-node-in-a-linked-list/
"""


class ListNode:  # pragma: no cover
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """

        # It is guaranteed that the node to be deleted is not a tail node in the list.
        node.val = node.next.val
        node.next = node.next.next
