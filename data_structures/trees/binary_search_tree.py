# coding: utf-8
"""
Binary Search Ttree
https://en.wikipedia.org/wiki/Binary_search_tree

- Every node has at most two children, left and right.
- Elements in left subtree of a node are less than the node.
- Elements in right subtree of a node are greater than the node.
- Each of left and right subtree must also be a Binary Search Tree.
"""
from collections import deque


class TreeNode:
    __slots__ = ['value', 'val', 'left', 'right']

    def __init__(self, value, left=None, right=None):
        self.value = self.val = value
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


# This implementation cannot properly handle duplicates.
class BinarySearchTree:
    NODE_CLASS = TreeNode

    def __init__(self):
        self.root = None
        self.size = 0

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return self.root == other.root  # It runs self.root's __eq__() resursively

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.levelorder_traverse(self.root)

    def __contains__(self, value):
        return self.search(value)

    def is_root(self, node):
        # TODO: What should we do if this is an empty tree?
        return self.root == node

    def children(self, node):
        if not node:
            return
        if node.left:
            yield node.left
        if node.right:
            yield node.right

    def num_children(self, node):
        return len(list(self.children(node)))

    def is_leaf(self, node):
        for _ in self.children(node):
            return False
        return True

    def height(self, node):
        """
        The height of a node is the number of edges on the longest path between the node and a descendant leaf.

        If node is a leaf, then the height of node is 0.
        Otherwise, the height of node is 1 + the maximum of heights of node's children.
        """
        if self.is_leaf(node):
            return 0
        return 1 + max(self.height(child) for child in self.children(node))

    def depth(self, node):
        """
        The depth of a node is the number of edges between the node and the root.

        If node is the root, then the depth of node is 0.
        Otherwise, the depth of node is 1 + the depth of node's parent.
        """
        if self.is_root(node):
            return 0

        depth = 0
        current_node = self.root
        while current_node:
            if node.value == current_node.value:
                break
            elif node.value < current_node.value:
                current_node = current_node.left
            elif node.value > current_node.value:
                current_node = current_node.right
            depth += 1

        return depth

    def level(self, node):
        """
        The level of a node is 1 + the depth of the node.
        """
        return 1 + self.depth(node)

    def num_edges(self):
        """
        If there are n nodes, then there are n - 1 edges.

        The 1 indicates the root node which has no edge points to it.
        """
        return self.size - 1 if self.size else 0

    def _insert_node(self, node, value):
        if not self.root:
            self.size += 1
            self.root = self.NODE_CLASS(value)
            return

        if value < node.value:
            if node.left:
                self._insert_node(node.left, value)
            else:
                self.size += 1
                node.left = self.NODE_CLASS(value)
        elif value > node.value:
            if node.right:
                self._insert_node(node.right, value)
            else:
                self.size += 1
                node.right = self.NODE_CLASS(value)
        elif value == node.value:
            raise ValueError('value is duplicate')
        else:
            raise RuntimeError

    def insert(self, value):
        self._insert_node(self.root, value)

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

    def inorder_traverse(self, node):
        """
        Inorder: the root is accessed between the left and the right.
        """
        # Inorder traversal of a BST will give you all elements in order.
        if not node:
            return

        # NOTE: self.inorder_traverse(node.left) only creates the generator object,
        # we need to actually run it with a for loop or yield from.
        yield from self.inorder_traverse(node.left)
        yield node
        yield from self.inorder_traverse(node.right)

    def preorder_traverse(self, node):
        """
        Preorder: the root is accessed before the left and the right.
        """
        if not node:
            return

        yield node
        yield from self.preorder_traverse(node.left)
        yield from self.preorder_traverse(node.right)

    def postorder_traverse(self, node):
        """
        Postorder: the root is accessed after the left and the right.
        """
        if not node:
            return

        yield from self.postorder_traverse(node.left)
        yield from self.postorder_traverse(node.right)
        yield node

    def levelorder_traverse(self, node):
        """
        Levelorder: visiting nodes level by level, left to right.
        """
        if not node:
            return

        queue = deque([node, ])
        while queue:
            node = queue.popleft()
            yield node
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    def traverse(self, method):
        method_to_func = {
            # Depth-First Search (DFS)
            'inorder': self.inorder_traverse,
            'preorder': self.preorder_traverse,
            'postorder': self.postorder_traverse,
            # Breadth-First Search (BFS)
            'levelorder': self.levelorder_traverse,
        }
        try:
            traverse_func = method_to_func[method]
        except KeyError:
            raise ValueError(f'invalid method {method}')

        return traverse_func(self.root)
