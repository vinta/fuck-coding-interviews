# coding: utf-8
"""
https://leetcode.com/problems/binary-tree-postorder-traversal/
"""
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        def postorder_traverse(node):
            if not node:
                return

            yield from postorder_traverse(node.left)
            yield from postorder_traverse(node.right)
            yield node.val

        return postorder_traverse(root)
