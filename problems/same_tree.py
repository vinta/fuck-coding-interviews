# coding: utf-8
"""
https://leetcode.com/problems/same-tree/
"""


class TreeNode:  # pragma: no cover
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        def is_same_node(p, q):
            if not p and not q:
                return True
            if p and q:
                return (p.val == q.val) and is_same_node(p.left, q.left) and is_same_node(p.right, q.right)

            return False

        return is_same_node(p, q)
