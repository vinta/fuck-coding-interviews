# coding: utf-8
class Node:
    def __init__(self, value):
        self.value = self.val = value

    def __eq__(self, other):
        raise NotImplementedError

    def __ne__(self, other):
        return not self == other


class Tree:
    NODE_CLASS = Node

    def __init__(self):
        self.root = None
        self.size = 0

    def __len__(self):
        return self.size

    def __iter__(self):
        raise NotImplementedError

    def _validate_node(self, node):
        if not isinstance(node, self.NODE_CLASS):
            raise TypeError(f'node must be a {self.NODE_CLASS.__name__} instance')
        return node

    def is_root(self, node):
        node = self._validate_node(node)
        return node == self.root

    def is_leaf(self, node):
        node = self._validate_node(node)
        return self.num_children(node) == 0

    def parent(self, node):
        raise NotImplementedError

    def num_children(self, node):
        raise NotImplementedError

    def children(self, node):
        raise NotImplementedError

    def siblings(self, node):
        raise NotImplementedError

    def subtree(self, node):
        raise NotImplementedError

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

    def external_nodes(self):
        raise NotImplementedError

    def internal_nodes(self):
        raise NotImplementedError
