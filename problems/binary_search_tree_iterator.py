# coding: utf-8
"""
https://leetcode.com/problems/binary-search-tree-iterator/
"""
import itertools


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:
    def __init__(self, root: TreeNode):
        def inorder_traverse(node):
            if not node:
                return

            yield from inorder_traverse(node.left)
            yield node.val
            yield from inorder_traverse(node.right)

        self.generator = inorder_traverse(root)

    def next(self) -> int:
        """
        @return the next smallest number
        """
        try:
            return next(self.generator)
        except StopIteration:
            return

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        used_generator, checked_generator = itertools.tee(self.generator)
        self.generator = used_generator
        try:
            next(checked_generator)
        except StopIteration:
            return False

        return True


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
