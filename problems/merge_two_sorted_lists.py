# coding: utf-8
"""
https://leetcode.com/problems/merge-two-sorted-lists/
"""
import heapq
import itertools


class ListNode:  # pragma: no cover
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        def gen_values(node):
            while node:
                yield node.val
                node = node.next

        # sorted_values = sorted(list(gen_values(l1)) + list(gen_values(l2)))
        sorted_values = sorted(itertools.chain(gen_values(l1), gen_values(l2)))

        # Build the linked list.
        dummy_head = last_node = ListNode()
        for value in sorted_values:
            new_node = ListNode(value)
            last_node.next = new_node
            last_node = new_node

        return dummy_head.next


# heapq.merge() is exactly suitable for k-way merges.
class Solution2:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        def gen_nodes(node):
            while node:
                yield node
                node = node.next

        sorted_nodes = heapq.merge(gen_nodes(l1), gen_nodes(l2), key=lambda node: node.val)
        dummy_head = last_node = ListNode()
        for node in sorted_nodes:
            last_node.next = node
            last_node = node

        return dummy_head.next


class Solution3:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        def gen_nodes(node):
            while node:
                yield node
                node = node.next

        l1_gen = gen_nodes(l1)
        l2_gen = gen_nodes(l2)

        dummy_head = last_node = ListNode()
        while True:
            n1 = next(l1_gen, None)
            n2 = next(l2_gen, None)
            if n1 and n2:
                if n1.val <= n2.val:
                    last_node.next = n1
                    last_node = n1
                    # Since we pop a node from l1, the node from l2 should remain.
                    # So reset l2 generator by creating a new one starts from the node.
                    l2_gen = gen_nodes(n2)
                else:
                    last_node.next = n2
                    last_node = n2
                    l1_gen = gen_nodes(n1)
            elif n1:
                last_node.next = n1
                last_node = n1
            elif n2:
                last_node.next = n2
                last_node = n2
            else:
                break

        return dummy_head.next
