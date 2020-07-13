# coding: utf-8
"""
https://leetcode.com/problems/binary-tree-preorder-traversal/
"""
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        def preorder_traverse(node):
            if not node:
                return

            yield node.val
            yield from preorder_traverse(node.left)
            yield from preorder_traverse(node.right)

        return preorder_traverse(root)
