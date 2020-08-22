# coding: utf-8
"""
B+ Tree
https://en.wikipedia.org/wiki/B%2B_tree
"""
import bisect


class Node:
    __slots__ = ['tree', 'parent', 'keys', 'pointers']

    def __init__(self, tree, parent=None):
        self.tree = tree
        self.parent = parent
        self.keys = []
        self.pointers = []

    def __repr__(self):
        return f'{self.__class__.__name__}({self.keys})'

    def __str__(self):
        return self.__repr__()

    def is_root(self):
        return self.parent is None

    def is_overflow(self):
        return len(self.keys) > self.tree.order - 1

    def split(self):
        if self.is_root():
            new_root = Node(tree=self.tree)
            self.tree.root = new_root
            self.parent = new_root
            self.parent.pointers = [self, ]

        median_index = (0 + len(self.keys) - 1) // 2
        median_key = self.keys[median_index]

        new_right = Node(tree=self.tree, parent=self.parent)
        new_right.keys = self.keys[median_index + 1:]
        new_right.pointers = self.pointers[median_index + 1:]
        for child in new_right.pointers:
            child.parent = new_right

        self.keys = self.keys[:median_index]
        self.pointers = self.pointers[:median_index + 1]  # NOTE: Here is "median_index + 1" instead of "median_index".

        child_index = bisect.bisect_left(self.parent.keys, median_key)
        self.parent.keys.insert(child_index, median_key)
        self.parent.pointers.insert(child_index + 1, new_right)
        if self.parent.is_overflow():
            self.parent.split()

    def insert(self, key, value):
        index = bisect.bisect_left(self.keys, key)
        self.keys.insert(index, key)
        self.pointers.insert(index, value)
        if self.is_overflow():
            self.split()


class LeafNode(Node):
    __slots__ = ['tree', 'parent', 'keys', 'pointers', 'next']

    def __init__(self, tree, parent=None):
        super().__init__(tree, parent=parent)
        self.next = None

    def split(self):
        if self.is_root():
            new_root = Node(tree=self.tree)
            self.tree.root = new_root
            self.parent = new_root
            self.parent.pointers = [self, ]

        median_index = (0 + len(self.keys) - 1) // 2
        median_key = self.keys[median_index]

        new_right = LeafNode(tree=self.tree, parent=self.parent)
        new_right.keys = self.keys[median_index:]
        new_right.pointers = self.pointers[median_index:]
        new_right.next = self.next

        self.keys = self.keys[:median_index]
        self.pointers = self.pointers[:median_index]
        self.next = new_right

        child_index = bisect.bisect_left(self.parent.keys, median_key)
        self.parent.keys.insert(child_index, median_key)
        self.parent.pointers.insert(child_index + 1, new_right)
        if self.parent.is_overflow():
            self.parent.split()


class BPlusTree:
    DEFAULT_TO_ROOT = object()

    def __init__(self, order=512):
        if order < 3:
            raise ValueError('order must be greater than or equal to 3')

        self._size = 0
        self.order = order
        self.root = LeafNode(tree=self)
        self.head = self.root

    def __len__(self):
        return self._size

    def __iter__(self):
        leaf_node = self.head
        while leaf_node:
            yield from leaf_node.keys
            leaf_node = leaf_node.next

    def _search_node(self, key, node):
        if isinstance(node, LeafNode):
            index = bisect.bisect_left(node.keys, key)
            if index < len(node.keys) and node.keys[index] == key:
                return node, index
            return node, -1

        if key < node.keys[0]:
            return self._search_node(key, node.pointers[0])
        elif key >= node.keys[-1]:
            return self._search_node(key, node.pointers[-1])
        else:
            index = bisect.bisect_right(node.keys, key)
            return self._search_node(key, node.pointers[index])

    def insert(self, key, value):
        node, index = self._search_node(key, self.root)
        if index != -1:
            raise KeyError('Duplicate key')

        node.insert(key, value)
        self._size += 1
