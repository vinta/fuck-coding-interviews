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
        def inorder_traverse(node):
            if not node:
                return

            yield from inorder_traverse(node.left)
            yield node.val
            yield from inorder_traverse(node.right)

        values = list(inorder_traverse(root))
        sorted_values = sorted(values)
        dedup_values = set(values)

        return (values == sorted_values) and (len(values) == len(dedup_values))


class Solution2:
    def isValidBST(self, root: TreeNode) -> bool:
        def inorder_traverse(node):
            if not node:
                return None

            yield from inorder_traverse(node.left)
            yield node.val
            yield from inorder_traverse(node.right)

        # last_val = float('-inf')
        last_val = -sys.maxsize
        for val in inorder_traverse(root):
            if last_val >= val:
                return False
            last_val = val

        # The following solution doesn't work since you cannot just check a single node at a time.
        # There might be a binary tree like this which is not BST:
        #    5
        #  /   \
        # 1     6
        #      / \
        #     4   7

        # def inorder_traverse(node):
        #     if not node:
        #         return

        #     yield from inorder_traverse(node.left)
        #     yield node
        #     yield from inorder_traverse(node.right)

        # for node in inorder_traverse(root):
        #     if node.left:
        #         if node.val <= node.left.val:
        #             return False

        #     if node.right:
        #         if node.val >= node.right.val:
        #             return False

        return True
