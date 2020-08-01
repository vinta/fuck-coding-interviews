# coding: utf-8
"""
https://leetcode.com/problems/maximum-depth-of-binary-tree/
"""
from collections import deque


class TreeNode:  # pragma: no cover
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        queue = deque([(root, 1), ])
        while queue:
            node, depth = queue.popleft()
            if node:
                if (not node.left) and (not node.right):  # The node is a leaf.
                    # Since we do level traversal,
                    # the depth of the first leaf node we found is the minimum depth.
                    return depth

                if node.left:
                    queue.append((node.left, depth + 1))
                if node.right:
                    queue.append((node.right, depth + 1))

        return 0
