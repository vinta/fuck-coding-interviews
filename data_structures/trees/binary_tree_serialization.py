# coding: utf-8
from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# This format is the same as how LeetCode serializes a binary tree
# https://support.leetcode.com/hc/en-us/articles/360011883654-What-does-1-null-2-3-mean-in-binary-tree-representation
class LevelorderCodec:
    def serialize(self, root):
        if not root:
            return '[]'

        # Levelorder traversal: visting node level by level, left to right
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

        return f"[{','.join(str(v) for v in values)}]"

    def deserialize(self, data):
        if not data or data == '[]':
            return None

        # Retrieve values from the serialized string, and convert them to proper types
        values = data.strip('[]').split(',')
        values = [None if v == 'null' else int(v) for v in values]
        value_queue = deque(values)

        root = TreeNode(value_queue.popleft())
        node_queue = deque([root, ])

        while node_queue and value_queue:
            node = node_queue.popleft()

            left_value = value_queue.popleft()
            if left_value is not None:  # Check the value explicitly since the value might be falsy value, for instance, 0
                node.left = TreeNode(left_value)
                node_queue.append(node.left)

            try:
                right_value = value_queue.popleft()
            except IndexError:
                continue
            if right_value is not None:
                node.right = TreeNode(right_value)
                node_queue.append(node.right)

        return root
