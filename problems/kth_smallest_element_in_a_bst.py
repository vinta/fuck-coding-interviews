# coding: utf-8
"""
https://leetcode.com/problems/kth-smallest-element-in-a-bst/
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        def inorder_traverse(node):
            if not node:
                return

            yield from inorder_traverse(node.left)
            yield node.val
            yield from inorder_traverse(node.right)

        count = 1
        for value in inorder_traverse(root):
            if count == k:
                return value

            count += 1
