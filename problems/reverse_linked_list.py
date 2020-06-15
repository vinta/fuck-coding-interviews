# coding: utf-8

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
