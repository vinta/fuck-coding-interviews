# coding: utf-8
"""
https://leetcode.com/problems/binary-tree-maximum-path-sum/
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.max_sum = float('-inf')

        def max_path_sum(node):
            if not node:
                return 0

            val = node.val

            # If the branch's sum is negative, ignore it.
            left_sum = max(max_path_sum(node.left), 0)
            right_sum = max(max_path_sum(node.right), 0)

            # Check whether this is the possible root node.
            current_sum = max(val, val + left_sum + right_sum)
            if current_sum > self.max_sum:
                self.max_sum = current_sum

            # You can only choose 1 branch, go left or go right.
            return max(val + left_sum, val + right_sum)

        max_path_sum(root)

        return self.max_sum
