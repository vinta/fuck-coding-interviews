# coding: utf-8
from abc import ABC, abstractmethod


class BaseNode(ABC):
    def __init__(self, value):
        self.value = self.val = value

    @abstractmethod
    def __eq__(self, other):
        ...

    def __ne__(self, other):
        return not self == other


class BaseTree(ABC):
    NODE_CLASS = BaseNode

    def __init__(self):
        self.root = None
        self.size = 0

    def __len__(self):
        return self.size

    @abstractmethod
    def __iter__(self):
        ...

    def _validate_node(self, node):
        if not isinstance(node, self.NODE_CLASS):
            raise TypeError(f'node must be a {self.NODE_CLASS.__name__} instance')
        return node

    def is_root(self, node):
        node = self._validate_node(node)
        return node == self.root

    def is_leaf(self, node):
        node = self._validate_node(node)
        return len(self.children(node)) == 0

    is_external = is_leaf

    def is_internal(self, node):
        return not self.is_external(node)

    @abstractmethod
    def parent(self, node):
        ...

    @abstractmethod
    def children(self, node):
        ...

    @abstractmethod
    def siblings(self, node):
        ...

    @abstractmethod
    def subtree(self, node):
        ...

    @abstractmethod
    def traverse(self, node=None):
        ...

    def height(self, node=None):
        """
        The height of a tree is equal to the maximum level of any node in the tree.

        If node is a leaf, then the height of node is 0.
        Otherwise, the height of node is 1 + the maximum of the heights of node's children.
        """
        if not node:
            node = self.root
        if self.is_leaf(node):
            return 0
        return 1 + max(self.height(n) for n in self.children(node))

    def depth(self, node):
        """
        The depth is the number of ancestors of node, excluding node itself.

        If node is the root, then the depth of node is 0.
        Otherwise, the depth of node is 1 + the depth of the parent of node.
        """
        if node == self.root:
            return 0
        return 1 + self.depth(self.parent(node))

    level = depth
