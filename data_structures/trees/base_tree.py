# coding: utf-8
"""
https://en.wikipedia.org/wiki/Tree_%28data_structure%29#Terminology_used_in_trees
http://typeocaml.com/2014/11/26/height-depth-and-level-of-a-tree/
"""
from abc import ABC
from abc import abstractmethod


class BaseNode(ABC):
    @abstractmethod
    def __init__(self):
        ...

    @abstractmethod
    def __eq__(self, other):
        ...


class TreeNode(BaseNode):
    __slots__ = ['value', 'left', 'right']

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return f'TreeNode({self.value})'

    def __str__(self):
        return str(self.value)

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return all((
            self.value == other.value,
            self.left == other.left,
            self.right == other.right,
        ))


class BaseTree(ABC):
    NODE_CLASS = BaseNode

    @abstractmethod
    def __init__(self):
        ...

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

    def is_external(self, node):
        return self.is_leaf(node)

    def is_internal(self, node):
        return not self.is_external(node)

    @abstractmethod
    def traverse(self):
        ...

    @abstractmethod
    def height(self, node):
        ...

    @abstractmethod
    def depth(self, node):
        ...

    @abstractmethod
    def level(self, node):
        ...
