# coding: utf-8
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def listnode_to_list(head):
    array = []
    next_node = head
    while next_node:
        array.append(next_node.val)
        next_node = next_node.next
    return array


def list_to_listnode(array):
    dummy_head_node = ListNode()
    current_node = dummy_head_node
    for val in array:
        current_node.next = ListNode(val)
        current_node = current_node.next
    return dummy_head_node.next
