# coding: utf-8
"""
https://leetcode.com/problems/sort-list/
"""
import heapq


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


def split(head):
    middle = next_two = head
    middle_previous = None
    while next_two and next_two.next:
        middle_previous = middle
        middle = middle.next
        next_two = next_two.next.next

    middle_previous.next = None
    return head, middle


def merge(head1, head2):
    dummy_head = tail = ListNode()
    while head1 and head2:
        if head1.val <= head2.val:
            tail.next = head1
            head1 = head1.next
        else:
            tail.next = head2
            head2 = head2.next
        tail = tail.next

    if head1:
        tail.next = head1
    else:
        tail.next = head2
    return dummy_head.next


def mergesort(head):
    # The linked list is empty or there is only one node.
    if (not head) or (not head.next):
        return head

    head1, head2 = split(head)
    sorted_head1 = mergesort(head1)
    sorted_head2 = mergesort(head2)
    return merge(sorted_head1, sorted_head2)


class Solution2:
    def sortList(self, head: ListNode) -> ListNode:
        return mergesort(head)


class Solution3:
    def sortList(self, head: ListNode) -> ListNode:
        min_heap = []

        # Traverse the linked list and build the heap.
        while head:
            heapq.heappush(min_heap, head.val)
            head = head.next

        # Rebuild the linked list from the heap.
        node = dummy_head = ListNode()
        while min_heap:
            val = heapq.heappop(min_heap)
            node.next = ListNode(val)
            node = node.next

        return dummy_head.next
