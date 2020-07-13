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

    items = []
    queue = deque([root, ])
    while queue:
        node = queue.popleft()

        if node:
            items.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            items.append('null')

    # Remove tail nulls
    while items and (items[-1] == 'null'):
        items.pop()

    return f"[{','.join(str(i) for i in items)}]"


def deserialize_tree_str(data):
    if data == '[]':
        return None

    value_queue = data.strip('[]').split(',')
    for i in range(len(value_queue)):
        if value_queue[i] == 'null':
            value_queue[i] = None
        else:
            value_queue[i] = int(value_queue[i])

    root_val = value_queue.pop(0)
    root = TreeNode(root_val)
    tree_queue = deque([root, ])

    while (tree_queue and value_queue):
        node = tree_queue.popleft()

        if value_queue:
            val = value_queue.pop(0)
            if val:
                node.left = TreeNode(val)
                tree_queue.append(node.left)

        if value_queue:
            val = value_queue.pop(0)
            if val:
                node.right = TreeNode(val)
                tree_queue.append(node.right)

    return root
