# coding: utf-8
"""
https://leetcode.com/problems/middle-of-the-linked-list/
"""


class ListNode:  # pragma: no cover
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        def to_list(node):
            arr = []
            while node:
                arr.append(node.val)
                node = node.next
            return arr

        def to_node(arr):
            node = dummy_head = ListNode()
            for val in arr:
                node.next = ListNode(val)
                node = node.next
            return dummy_head.next

        arr = to_list(head)
        middle_index = len(arr) // 2
        return to_node(arr[middle_index:])


# The Two-Pointers way.
class Solution2:
    def middleNode(self, head: ListNode) -> ListNode:
        slow = fast = head
        # `slow` traverses one node at a time, and `fast` traverses two nodes at a time.
        # When `fast` reaches the end, `slow` would be in the middle.
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow
