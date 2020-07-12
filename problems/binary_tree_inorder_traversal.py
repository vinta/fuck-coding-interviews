# coding: utf-8
"""
https://leetcode.com/problems/binary-tree-inorder-traversal/
"""
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        def inorder_traverse(node):
            if not node:
                return

            yield from inorder_traverse(node.left)
            yield node.val
            yield from inorder_traverse(node.right)

        return inorder_traverse(root)
