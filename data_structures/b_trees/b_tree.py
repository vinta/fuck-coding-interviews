# coding: utf-8
"""
B-tree
https://en.wikipedia.org/wiki/B-tree

A B-tree of order m is an m-way search tree that either is empty or satisfies the following properties:
- All nodes have ceil(m / 2) <= k <= m children, except for:
    - The root node which has 2 <= k <= m children.
    - Leaf nodes which have no children.
- All leaf nodes are in the same level and carry no information.
- All non-leaf nodes with k children contain k − 1 keys.
- All keys within a node are in increasing order.
"""
import bisect


class BTreeNode:
    def __init__(self, tree, parent=None):
        self.tree = tree
        self.parent = parent
        self.keys = []
        self._children = []

    @property
    def children(self):
        return self._children

    @children.setter
    def children(self, new_children):
        self._children = []
        for child in new_children:
            child.parent = self
            self._children.append(child)

    def __repr__(self):
        return f'BTreeNode({self.keys})'

    def __str__(self):
        return self.__repr__()

    def is_root(self):
        return self.parent is None

    def is_leaf(self):
        return not self.children

    def is_full(self):
        return len(self.keys) > (self.tree.order - 1)

    def split(self):
        if self.is_root():
            new_root = self.__class__(tree=self.tree, parent=None)
            self.tree.root = new_root
            self.parent = new_root
            self.parent.children = [self, ]

        median_index = (0 + len(self.keys) - 1) // 2
        median = self.keys[median_index]

        new_right = self.__class__(tree=self.tree, parent=self.parent)
        new_right.keys = self.keys[median_index + 1:]
        new_right.children = self.children[median_index + 1:]

        self.keys = self.keys[:median_index]
        self.children = self.children[:median_index + 1]  # NOTE

        child_index = self.parent.children.index(self)
        self.parent.children.insert(child_index + 1, new_right)
        self.parent.insert(key=median, value=median)

    def insert(self, key, value):
        index = bisect.bisect_left(self.keys, key)
        self.keys.insert(index, key)
        if self.is_full():
            self.split()


class BTree:
    NODE_CLASS = BTreeNode

    def __init__(self, order=512):
        if order <= 1:
            raise ValueError('order must be greater than 1')

        self._size = 0
        self._height = 0
        self.order = order
        self.root = self.NODE_CLASS(tree=self)

    def __len__(self):
        return self._size

    def __iter__(self):
        for node in self.inorder_traverse(self.root):
            yield from node.keys

    def inorder_traverse(self, node):
        for child_node in node.children[:len(node.children) - 1]:
            yield from self.inorder_traverse(child_node)

        yield node

        if node.children:
            yield from self.inorder_traverse(node.children[-1])

    def levelorder_traverse(self, node):
        yield node
        for child in node.children:
            yield from self.levelorder_traverse()

    def _binary_search(self, arr, target, low, high):
        if low > high:
            return -1

        mid_index = (low + high) // 2
        mid = arr[mid_index]
        if target == mid:
            return mid_index
        elif target < mid:
            return self._binary_search(arr, target, low, mid_index - 1)
        elif target > mid:
            return self._binary_search(arr, target, mid_index + 1, high)

    def _search_node(self, node, key):
        if node.is_leaf():
            index = self._binary_search(node.keys, key, 0, len(node.keys) - 1)
            return node, index
        else:
            index = bisect.bisect_left(node.keys, key)
            child_node = node.children[index]
            return self._search_node(child_node, key)

    def search(self, key):
        node, index = self._search_node(self.root, key)
        if index == -1:
            raise ValueError
        return node.values[index]

    def insert(self, key, value):
        # TODO: duplicate key?
        node, index = self._search_node(self.root, key)
        node.insert(key, value)
        self._size += 1
