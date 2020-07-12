# coding: utf-8
"""
https://en.wikipedia.org/wiki/Tree_%28data_structure%29#Terminology_used_in_trees
http://typeocaml.com/2014/11/26/height-depth-and-level-of-a-tree/
"""
from abc import ABC
from abc import abstractmethod


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
    def parent(self, node):
        ...

    @abstractmethod
    def children(self, node):
        ...

    @abstractmethod
    def traverse(self):
        ...

    @abstractmethod
    def height(self, node):
        """
        The height of a node is the number of edges on the longest path between the node and a descendant leaf.

        If node is a leaf, then the height of node is 0.
        Otherwise, the height of node is 1 + the maximum of heights of node's children.
        """
        if self.is_leaf(node):
            return 0
        return 1 + max(self.height(child) for child in self.children(node))

    @abstractmethod
    def depth(self, node):
        """
        The depth of a node is the number of edges between the node and the root.

        If node is the root, then the depth of node is 0.
        Otherwise, the depth of node is 1 + the depth of node's parent.
        """
        if self.is_root(node):
            return 0
        return 1 + self.depth(self.parent(node))

    @abstractmethod
    def level(self, node):
        """
        The level of a node is 1 + the depth of the node.
        """
        return 1 + self.depth(node)
