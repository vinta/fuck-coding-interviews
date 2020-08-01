# coding: utf-8
"""
https://leetcode.com/problems/binary-tree-level-order-traversal/
"""
from typing import List


class TreeNode:  # pragma: no cover
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        current_level = [root, ]
        output = []
        while current_level:
            level = []
            next_level = []
            for node in current_level:
                if node:
                    level.append(node.val)
                    next_level.extend([node.left, node.right])

            if level:
                output.append(level)

            current_level = next_level

        return output
