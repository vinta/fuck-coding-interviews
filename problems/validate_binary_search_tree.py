# coding: utf-8
"""
https://leetcode.com/problems/validate-binary-search-tree/
"""
import sys


class TreeNode:  # pragma: no cover
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def inorder(node):
            if not node:
                return

            yield from inorder(node.left)
            yield node.val
            yield from inorder(node.right)

        values = list(inorder(root))
        sorted_values = sorted(values)
        dedup_values = set(values)

        return (values == sorted_values) and (len(values) == len(dedup_values))


class Solution2:
    def isValidBST(self, root: TreeNode) -> bool:
        def inorder(node):
            if not node:
                return None

            yield from inorder(node.left)
            yield node.val
            yield from inorder(node.right)

        # last_val = float('-inf')
        last_val = -sys.maxsize
        for val in inorder(root):
            if last_val >= val:
                return False
            last_val = val

        return True
