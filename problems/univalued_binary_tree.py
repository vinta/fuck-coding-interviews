# coding: utf-8
"""
https://leetcode.com/problems/univalued-binary-tree/
"""
from collections import deque


class TreeNode:  # pragma: no cover
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        if not root:
            return True

        value = root.val
        queue = deque([root, ])
        while queue:
            node = queue.popleft()
            if node:
                if node.val != value:
                    return False

                queue.extend([node.left, node.right])

        return True
