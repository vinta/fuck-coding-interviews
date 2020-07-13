# coding: utf-8
"""
https://en.wikipedia.org/wiki/Binary_search_tree

- Every node has at most two children, left and right.
- All values in left subtree of a node are less than the node's value.
- All values in right subtree of a node are greater than the node's value.
- Each of left and right subtree must also be a Binary Search Tree.
"""
from collections import deque


class TreeNode:
    __slots__ = ['value', 'val', 'left', 'right']

    def __init__(self, value, left=None, right=None):
        self.value = self.val = value
        self.left = left
        self.right = right

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return all((
            self.value == other.value,
            self.left == other.left,
            self.right == other.right,
        ))


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

    def _insert_node(self, node, value):
        if value < node.value:
            if node.left:
                self._insert_node(node.left, value)
            else:
                node.left = self.NODE_CLASS(value)
        elif value > node.value:
            if node.right:
                self._insert_node(node.right, value)
            else:
                node.right = self.NODE_CLASS(value)
        elif value == node.value:
            raise ValueError('value is duplicate')

    def insert(self, value):
        self.size += 1
        if self.root:
            self._insert_node(self.root, value)
        else:
            self.root = self.NODE_CLASS(value)

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

    def is_root(self, node):
        return self.root == node

    def children(self, node):
        if node.left:
            yield node.left
        if node.right:
            yield node.right

    def is_leaf(self, node):
        for _ in self.children(node):
            return False
        return True

    # Inorder: the root is accessed between the left and the right.
    def inorder_traverse(self, node):
        # Inorder traversal of a BST will give you all elements in order.
        if not node:
            return

        # NOTE: self.inorder_traverse(node.left) only creates the generator object,
        # we need to actually run it with a for loop or yield from.
        yield from self.inorder_traverse(node.left)
        yield node
        yield from self.inorder_traverse(node.right)

    # Preorder: the root is accessed before the left and the right.
    def preorder_traverse(self, node):
        if not node:
            return

        yield node
        yield from self.preorder_traverse(node.left)
        yield from self.preorder_traverse(node.right)

    # Postorder: the root is accessed after the left and the right.
    def postorder_traverse(self, node):
        if not node:
            return

        yield from self.postorder_traverse(node.left)
        yield from self.postorder_traverse(node.right)
        yield node

    # Levelorder: visiting nodes level by level, left to right.
    def levelorder_traverse(self, node):
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

    def traverse(self, method='inorder'):
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
