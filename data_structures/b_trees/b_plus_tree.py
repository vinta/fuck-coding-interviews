# coding: utf-8
"""
B+ Tree
https://en.wikipedia.org/wiki/B%2B_tree
"""
import bisect
import math


class BPlusTreeNode:
    __slots__ = ['tree', 'parent', 'keys', 'values']

    def __init__(self, tree, parent=None):
        self.tree = tree
        self.parent = parent
        self.keys = []
        self.values = []

    def __repr__(self):
        return f'{self.__class__.__name__}({self.keys})'

    def __str__(self):
        return self.__repr__()

    def is_root(self):
        return self.parent is None

    def is_leaf(self):
        return isinstance(self, BPlusTreeLeafNode)

    def is_overflow(self):
        return len(self.keys) > self.tree.order - 1

    def split(self):
        if self.is_root():
            new_root = BPlusTreeNode(tree=self.tree)
            self.tree.root = new_root
            self.parent = new_root
            self.parent.values = [self, ]

        median_index = self.tree.order // 2
        median_key = self.keys[median_index]

        if self.is_leaf():
            new_right = BPlusTreeLeafNode(tree=self.tree, parent=self.parent)
            new_right.keys = self.keys[median_index:]
            new_right.values = self.values[median_index:]  # values are nodes.
            new_right.next = self.next

            self.keys = self.keys[:median_index]
            self.values = self.values[:median_index]
            self.next = new_right
        else:
            new_right = BPlusTreeNode(tree=self.tree, parent=self.parent)
            new_right.keys = self.keys[median_index + 1:]
            new_right.values = self.values[median_index + 1:]  # values are data.
            for child in new_right.values:
                child.parent = new_right

            self.keys = self.keys[:median_index]
            self.values = self.values[:median_index + 1]  # NOTE: Here is "median_index + 1" instead of "median_index".

        child_index = bisect.bisect_left(self.parent.keys, median_key)
        self.parent.keys.insert(child_index, median_key)
        self.parent.values.insert(child_index + 1, new_right)
        if self.parent.is_overflow():
            self.parent.split()

    def insert(self, key, value):
        index = bisect.bisect_left(self.keys, key)
        self.keys.insert(index, key)
        self.values.insert(index, value)
        if self.is_overflow():
            self.split()

    def check_validation(self):
        if len(self.tree):
            assert self.keys
            assert self.keys == sorted(set(self.keys))

        num_pointers = len(self.pointers)
        assert num_pointers <= self.tree.order, num_pointers

        if not self.is_leaf() and not self.is_root():  # Internal nodes.
            assert num_pointers >= math.ceil(self.tree.order / 2), num_pointers

        if self.is_root() and not self.is_leaf():
            assert num_pointers >= 2, num_pointers

        if self.is_leaf():
            for value in self.values:
                assert not isinstance(value, (BPlusTreeNode, BPlusTreeLeafNode))
        else:
            assert num_pointers - 1 == len(self.keys)

            for child in self.values:
                assert child.parent == self
                child.check_validation()


class BPlusTreeLeafNode(BPlusTreeNode):
    __slots__ = ['tree', 'parent', 'keys', 'values', 'next']

    def __init__(self, tree, parent=None):
        super().__init__(tree, parent=parent)
        self.next = None


class BPlusTree:
    DEFAULT_TO_ROOT = object()

    def __init__(self, order=512):
        if order < 3:
            raise ValueError('order must be greater than or equal to 3')

        self.size = 0
        self.order = order
        self.root = BPlusTreeLeafNode(tree=self)
        self.head = self.root

    def __len__(self):
        return self.size

    def __iter__(self):
        leaf_node = self.head
        while leaf_node:
            yield from leaf_node.keys
            leaf_node = leaf_node.next

    def search_node(self, key, node):
        if isinstance(node, BPlusTreeLeafNode):
            return node

        index = bisect.bisect_right(node.keys, key)
        return self.search_node(key, node.values[index])

    def get(self, key):
        node = self.search_node(key, self.root)
        index = bisect.bisect_left(node.keys, key)
        if index < len(node.keys) and node.keys[index] == key:
            return node.values[index]

        raise KeyError

    def insert(self, key, value):
        node = self.search_node(key, self.root)
        index = bisect.bisect_left(node.keys, key)
        if index < len(node.keys) and node.keys[index] == key:
            raise KeyError('Duplicate key')

        node.insert(key, value)
        self.size += 1
