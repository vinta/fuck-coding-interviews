# coding: utf-8
from abc import ABC, abstractmethod


class BaseNode(ABC):
    def __init__(self, value):
        self.value = self.val = value

    @abstractmethod
    def __eq__(self, other):
        ...


class BaseTree(ABC):
    NODE_CLASS = BaseNode

    def __init__(self):
        self.root = None

    @abstractmethod
    def __eq__(self, value):
        ...

    @abstractmethod
    def __len__(self):
        ...

    @abstractmethod
    def __iter__(self):
        ...

    @abstractmethod
    def __contains__(self, value):
        ...

    @abstractmethod
    def is_root(self, node):
        ...

    @abstractmethod
    def is_leaf(self, node):
        ...

    is_external = is_leaf

    def is_internal(self, node):
        return not self.is_external(node)

    @abstractmethod
    def children(self, node):
        ...

    @abstractmethod
    def traverse(self):
        ...

    @abstractmethod
    def height(self, node=None):
        """
        The height of a tree is equal to the maximum level of any node in the tree.

        If node is a leaf, then the height of node is 0.
        Otherwise, the height of node is 1 + the maximum of the heights of node's children.
        """
        ...

    @abstractmethod
    def depth(self, node=None):
        """
        The depth is the number of ancestors of node, excluding node itself.

        If node is the root, then the depth of node is 0.
        Otherwise, the depth of node is 1 + the depth of the parent of node.
        """
        ...

    level = depth
