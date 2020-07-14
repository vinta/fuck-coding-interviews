# coding: utf-8
from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class BaseCodec:
    def __init__(self, delimiter=',', terminator='null', brackets='[]'):
        self.delimiter = delimiter
        self.terminator = terminator

        len_brackets = len(brackets)
        if len_brackets not in (0, 2):
            raise ValueError('brackets must be 0 or 2 characters')

        self.brackets = brackets
        self.open_bracket = brackets[0] if len_brackets == 2 else ''
        self.close_bracket = brackets[1] if len_brackets == 2 else ''


# This format is the same as how LeetCode serializes a binary tree
# https://support.leetcode.com/hc/en-us/articles/360011883654-What-does-1-null-2-3-mean-in-binary-tree-representation
class LevelorderCodec(BaseCodec):
    def serialize(self, root):
        if not root:
            return self.brackets

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
                values.append(self.terminator)

        # Remove tail nulls
        while values and (values[-1] == self.terminator):
            values.pop()

        return f"{self.open_bracket}{f'{self.delimiter}'.join(str(v) for v in values)}{self.close_bracket}"

    def deserialize(self, data):
        if not data or data == self.brackets:
            return None

        # Retrieve values from the serialized string, and convert them to proper types
        values = data.strip(self.brackets).split(self.delimiter)
        values = [None if v == self.terminator else int(v) for v in values]
        value_queue = deque(values)

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
                continue
            if right_value is not None:
                node.right = TreeNode(right_value)
                node_queue.append(node.right)

        return root
