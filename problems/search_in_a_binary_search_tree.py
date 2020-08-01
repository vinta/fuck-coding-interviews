# coding: utf-8
"""
https://leetcode.com/problems/search-in-a-binary-search-tree/
"""


class TreeNode:  # pragma: no cover
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return root

        def search_node(node, value):
            node_val = node.val
            if value == node_val:
                return node
            elif value < node_val:
                if node.left:
                    return search_node(node.left, value)
            elif value > node_val:
                if node.right:
                    return search_node(node.right, value)
            return None

        return search_node(root, val)


class Solution2:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        def search_node(node, value):
            if not node:
                return None
            node_val = node.val
            if value == node_val:
                return node
            elif value < node_val:
                return search_node(node.left, value)
            elif value > node_val:
                return search_node(node.right, value)

        return search_node(root, val)
