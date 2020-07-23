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

    is_external = is_leaf

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
