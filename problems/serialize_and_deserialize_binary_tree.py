# coding: utf-8
"""
https://leetcode.com/problems/serialize-and-deserialize-binary-tree/
"""
from collections import deque


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Also see https://github.com/vinta/fuck-coding-interviews/blob/master/data_structures/trees/binary_tree_serialization.py
class Codec:
    def serialize(self, root):
        if not root:
            return ''

        values = []
        node_queue = deque([root, ])

        while node_queue:
            node = node_queue.popleft()
            if node:
                values.append(node.val)
                node_queue.append(node.left)
                node_queue.append(node.right)
            else:
                values.append('#')

        while values and (values[-1] == '#'):
            values.pop()

        return ','.join(str(v) for v in values)

    def deserialize(self, data):
        if not data:
            return None

        value_queue = deque(None if v == '#' else int(v) for v in data.split(','))

        root = TreeNode(value_queue.popleft())
        node_queue = deque([root, ])

        while node_queue and value_queue:
            node = node_queue.popleft()

            left_value = value_queue.popleft()
            if left_value is not None:
                node.left = TreeNode(left_value)
                node_queue.append(node.left)

            try:
                right_value = value_queue.popleft()
            except IndexError:
                return root
            if right_value is not None:
                node.right = TreeNode(right_value)
                node_queue.append(node.right)

        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
