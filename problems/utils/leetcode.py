# coding: utf-8
from collections import deque


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


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def list_to_compact_str(array):
    return f"[{','.join(str(i) for i in array)}]"


def serialize_treenode(root):
    if not root:
        return '[]'

    values = []
    node_queue = deque([root, ])

    while node_queue:
        node = node_queue.popleft()
        if node:
            values.append(node.val)
            node_queue.append(node.left)
            node_queue.append(node.right)
        else:
            values.append('null')

    # Remove tail nulls
    while values and (values[-1] == 'null'):
        values.pop()

    return f"[{','.join(str(i) for i in values)}]"


def deserialize_tree_str(data):
    if data == '[]':
        return None

    values = data.strip('[]').split(',')
    for i in range(len(values)):
        if values[i] == 'null':
            values[i] = None
        else:
            values[i] = int(values[i])
    value_queue = deque(values)

    root = TreeNode(value_queue.popleft())
    node_queue = deque([root, ])

    while node_queue and value_queue:
        node = node_queue.popleft()

        val = value_queue.popleft()
        if val:
            node.left = TreeNode(val)
            node_queue.append(node.left)

        try:
            val = value_queue.popleft()
        except IndexError:
            continue
        if val:
            node.right = TreeNode(val)
            node_queue.append(node.right)

    return root
