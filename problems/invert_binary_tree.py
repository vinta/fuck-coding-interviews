# coding: utf-8
"""
https://leetcode.com/problems/invert-binary-tree/
"""
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        queue = deque([root, ])
        while queue:
            node = queue.popleft()
            if node:
                queue.extend((node.left, node.right))
                node.left, node.right = node.right, node.left

        return root
