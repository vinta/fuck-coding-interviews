# coding: utf-8
"""
Treap
https://en.wikipedia.org/wiki/Treap

Treap is a self-balancing binary search tree which satisfies some extra properties:
- Each node has a random priority.
- Each random priority satisfies the properties of a heap.
    - The parent's priority is less than or equal to children's priorities.
    - The root's priority would be the minimum of the tree.
    - Each of left and right subtree is also a heap.
"""
import random


class TreeNode:
    __slots__ = ['_priority', 'value', 'left', 'right']

    def __init__(self, value, left=None, right=None):
        self._priority = random.random()  # Read-only.
        self.value = value
        self.left = left
        self.right = right

    @property
    def priority(self):
        return self._priority

    def right_rotate(self):
        #        root                  pivot
        #       /    \                /     \
        #    pivot   gamma    =>    alpha   root
        #    /   \                          /  \
        # alpha  beta                   beta  gamma
        # https://en.wikipedia.org/wiki/Tree_rotation
        root = self
        pivot = root.left
        root.left = pivot.right
        pivot.right = root
        return pivot

    def left_rotate(self):
        root = self
        pivot = root.right
        root.right = pivot.left
        pivot.left = root
        return pivot

    def check_validation(self):
        if self.left:
            assert self.priority <= self.left.priority
            self.left.check_validation()
        if self.right:
            assert self.priority <= self.right.priority
            self.right.check_validation()


class Treap:
    DEFAULT_TO_ROOT = object()
    NODE_CLASS = TreeNode

    def __init__(self):
        self.root = None
        self.size = 0

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.inorder_traverse(self.root)

    def _search_node(self, node, value):
        if not node:
            return None

        if value == node.value:
            return node
        elif value < node.value:
            return self._search_node(node.left, value)
        elif value > node.value:
            return self._search_node(node.right, value)

    def search(self, value):
        return self._search_node(self.root, value)

    def _insert_node(self, node, value):
        if not node:
            self.size += 1
            node = self.NODE_CLASS(value=value)
            return node

        if value <= node.value:
            node.left = self._insert_node(node.left, value)
            if node.left.priority < node.priority:
                node = node.right_rotate()
        elif value > node.value:
            node.right = self._insert_node(node.right, value)
            if node.right.priority < node.priority:
                node = node.left_rotate()

        return node

    def insert(self, value):
        self.root = self._insert_node(self.root, value)

    def _delete_node(self, node, value):
        if not node:
            raise ValueError('Not found')

        if value == node.value:
            if (node.left is None) and (node.right is None):  # Leaf nodes can be simply deleted.
                self.size -= 1
                return None
            elif node.left is None:
                self.size -= 1
                return node.right
            elif node.right is None:
                self.size -= 1
                return node.left
            elif node.left and node.right:
                if node.left.priority < node.right.priority:
                    node = node.right_rotate()
                    node.right = self._delete_node(node.right, value)
                else:
                    node = node.left_rotate()
                    node.left = self._delete_node(node.left, value)
        elif value < node.value:
            node.left = self._delete_node(node.left, value)
        elif value > node.value:
            node.right = self._delete_node(node.right, value)

        return node

    def delete(self, value):
        self.root = self._delete_node(self.root, value)

    def inorder_traverse(self, node):
        if not node:
            return

        yield from self.inorder_traverse(node.left)
        yield node.value
        yield from self.inorder_traverse(node.right)

    def levelorder_traverse_nodes(self, node=DEFAULT_TO_ROOT):
        if node == self.DEFAULT_TO_ROOT:
            node = self.root

        current_level = [node, ]
        while current_level:
            next_level = []
            for node in current_level:
                if node:
                    yield node
                    next_level.extend([node.left, node.right])
            current_level = next_level
