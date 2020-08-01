# coding: utf-8
"""
https://leetcode.com/problems/maximum-depth-of-binary-tree/
"""


class TreeNode:  # pragma: no cover
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        max_depth = 0
        current_level = [root, ]
        while current_level:
            next_level = []
            for node in current_level:
                if node:
                    next_level.extend([node.left, node.right])

            if next_level:
                max_depth += 1

            current_level = next_level

        return max_depth


class Solution2:
    def maxDepth(self, root: TreeNode) -> int:
        # LeetCode's definition:
        # The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
        if not root:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
