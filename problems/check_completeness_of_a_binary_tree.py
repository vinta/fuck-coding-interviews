# coding: utf-8
"""
https://leetcode.com/problems/check-completeness-of-a-binary-tree/
"""
from collections import deque


class TreeNode:  # pragma: no cover
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        queue = deque([root, ])
        has_none = False
        while queue:
            node = queue.popleft()
            if node:
                if has_none:
                    return False
                queue.extend([node.left, node.right])
            else:
                has_none = True

        return True
