# coding: utf-8
"""
Binary Search Tree
https://en.wikipedia.org/wiki/Binary_search_tree

A binary search tree is a special binary tree which satisfies following properties:
- Every node has at most two children, left and right.
- Elements in left subtree of a node are less than the node.
- Elements in right subtree of a node are greater than the node.
- Each of left and right subtree must also be a binary search tree.
"""
from collections import deque
import sys

from data_structures.trees.base_tree import BaseNode
from data_structures.trees.base_tree import BaseTree


class TreeNode(BaseNode):
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
class BinarySearchTree(BaseTree):
    NODE_CLASS = TreeNode
    DEFAULT_TO_ROOT = object()

    def __init__(self):
        self.root = None
        self.size = 0

    def __eq__(self, other):
        return self.root == other.root  # It runs self.root's __eq__() resursively

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.levelorder_traverse()

    def __contains__(self, value):
        return self.search(value)

    def is_valid(self):
        # The inorder traversal of a binary search tree results in an ascending sorted array.
        def inorder(node):
            if not node:
                return None

            yield from inorder(node.left)
            yield node.value
            yield from inorder(node.right)

        previous_value = -sys.maxsize
        for value in inorder(self.root):
            if previous_value >= value:
                return False
            previous_value = value

        return True

    def is_full(self):
        """
        A full binary tree is a binary tree where each node has exactly 0 or 2 children.
        """
        queue = deque([self.root, ])
        while queue:
            node = queue.popleft()
            if node:
                if not ((not node.left and not node.right) or (node.left and node.right)):
                    return False
                queue.extend((node.left, node.right))

        return True

    def is_complate(self):
        """
        When we fill out a complete binary tree, we go top to bottom, left to right.

        Also, in the levelorder traversal, if we find any concrete node after an empty node (a None node),
        then the tree is not complete.
        """
        queue = deque([self.root, ])
        found_none_node = False
        while queue:
            node = queue.popleft()
            if node:
                if found_none_node:
                    return False
                queue.extend((node.left, node.right))
            else:
                found_none_node = True

        return True

    def is_balanced(self):
        """
        A balanced binary tree is a binary tree in which
        the left and right subtrees of every node differ in height by no more than 1.
        """
        # NOTE: If you use something like _is_balanced = True, it won't work.
        # When you run _is_balanced = False inside the _height() function,
        # you simply create a new local variable, _is_balanced, in the function.
        tree = {'is_balanced': True}

        def _height(node):
            # Trigger the short circuit if we already found the tree unbalanced
            if not tree['is_balanced']:
                return 0

            if not node:
                return -1
            if (not node.left) and (not node.right):
                return 0

            left_height = _height(node.left)
            right_height = _height(node.right)
            if abs(left_height - right_height) > 1:
                tree['is_balanced'] = False

            return 1 + max(left_height, right_height)

        _height(self.root)
        return tree['is_balanced']

    def is_perfect(self):
        """
        A perfect binary tree is a binary tree in which
        every non-leaf node has exactly 2 children.

        Also, a perfect binary tree of height h has (2 ** (h + 1)) – 1 nodes.
        """
        tree = {'node_count': 0}

        def _height(node):
            if not node:
                return -1

            tree['node_count'] += 1

            if not node.left and not node.right:
                return 0

            return 1 + max(_height(node.left), _height(node.right))

        height = _height(self.root)
        return tree['node_count'] == (2 ** (height + 1)) - 1

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
        if node:
            if node.left:
                return False
            if node.right:
                return False
        return True

    def height(self, node=DEFAULT_TO_ROOT):
        """
        The height of a node is the number of edges between the node and its deepest leaf.

        If node is a leaf, then the height of node is 0.
        Otherwise, the height of node is 1 + the maximum of heights of node's children.
        """
        if node is self.DEFAULT_TO_ROOT:
            node = self.root

        if not node:
            return -1
        if (not node.left) and (not node.right):
            return 0

        return 1 + max(self.height(node.left), self.height(node.right))

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

    def insert(self, value):
        """
        Insertion of a binary search tree follows the basic logic of binary search.
        """
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

    def get_min_node(self, node=DEFAULT_TO_ROOT):
        """
        The minimum node is the leftmost node in subtrees of node.
        """
        if node is self.DEFAULT_TO_ROOT:
            node = self.root

        current_node = node
        while current_node:
            if current_node.left:
                current_node = current_node.left
            else:
                return current_node

    def get_max_node(self, node=DEFAULT_TO_ROOT):
        """
        The maximum node is the rightmost node in subtrees of node.
        """
        if node is self.DEFAULT_TO_ROOT:
            node = self.root

        current_node = node
        while current_node:
            if current_node.right:
                current_node = current_node.right
            else:
                return current_node

    def _delete_node(self, node, value):
        if not node:
            raise ValueError('value is not found')

        if value == node.value:
            if self.num_children(node) == 0:
                self.size -= 1
                node = None
            elif self.num_children(node) == 1:
                self.size -= 1
                if node.left:
                    node = node.left
                elif node.right:
                    node = node.right
            elif self.num_children(node) == 2:
                inorder_successor = self.get_min_node(node.right)
                node.value = inorder_successor.value
                node.right = self._delete_node(node.right, inorder_successor.value)
        elif value < node.value:
            node.left = self._delete_node(node.left, value)
        elif value > node.value:
            node.right = self._delete_node(node.right, value)

        # NOTE: Python function's parameters are "passed by assignment".
        # If you re-assign a parameter, you lose the parameter's reference to the original object.
        # https://docs.python.org/3/faq/programming.html#how-do-i-write-a-function-with-output-parameters-call-by-reference
        return node

    def delete(self, value):
        """
        If the node to be deleted:
            - Is a leaf:
                - Simply remove the node from the tree.
            - Has 1 child:
                - Copy the child to the node and delete the child.
            - Has 2 children:
                - Find the leftmost node in the node's right subtree, the inorder successor.
                - Copy the value of the inorder successor to the node.
                - Delete the inorder successor.
        """
        self.root = self._delete_node(self.root, value)

    def inorder_traverse(self, node=DEFAULT_TO_ROOT):
        """
        Inorder: the root is accessed between the left and the right.
        """
        if node is self.DEFAULT_TO_ROOT:
            node = self.root

        # Inorder traversal of a BST will give you all elements in order.
        if not node:
            return

        # NOTE: self.inorder_traverse(node.left) only creates the generator object,
        # we need to actually run it with a for loop or yield from.
        yield from self.inorder_traverse(node.left)
        yield node.value
        yield from self.inorder_traverse(node.right)

    def preorder_traverse(self, node=DEFAULT_TO_ROOT):
        """
        Preorder: the root is accessed before the left and the right.
        """
        if node is self.DEFAULT_TO_ROOT:
            node = self.root

        if not node:
            return

        yield node.value
        yield from self.preorder_traverse(node.left)
        yield from self.preorder_traverse(node.right)

    def postorder_traverse(self, node=DEFAULT_TO_ROOT):
        """
        Postorder: the root is accessed after the left and the right.
        """
        if node is self.DEFAULT_TO_ROOT:
            node = self.root

        if not node:
            return

        yield from self.postorder_traverse(node.left)
        yield from self.postorder_traverse(node.right)
        yield node.value

    def levelorder_traverse(self, node=DEFAULT_TO_ROOT):
        """
        Levelorder: visiting nodes level by level, left to right.
        """
        if node is self.DEFAULT_TO_ROOT:
            node = self.root

        if not node:
            return

        queue = deque([node, ])
        while queue:
            node = queue.popleft()
            yield node.value
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

    def invert(self):
        # Traverse nodes by levelorder
        queue = deque([self.root, ])
        while queue:
            node = queue.popleft()
            if node:
                queue.extend((node.left, node.right))
                node.left, node.right = node.right, node.left

    def to_array_representation(self):
        """
        Return the "Array Representation" of the tree.
        https://en.wikipedia.org/wiki/Binary_tree#Arrays
        """
        array = []
        current_level = [self.root, ]
        next_level = []
        while any(current_level):
            for node in current_level:
                # We append values to array for current_level,
                # and put their child nodes to next_level.
                if node:
                    array.append(node.value)
                    next_level.extend([node.left, node.right])
                else:
                    array.append(None)
                    next_level.extend([None, None])

            current_level = next_level
            next_level = []

        while array and (array[-1] is None):
            array.pop()

        return array

    @classmethod
    def from_array_representation(cls, array):
        """
        The index of parent node of array[i] is math.floor((i - 1) / 2).
        Also, every odd index indicates a left node, and every even index indicates a right node.
        https://learning.oreilly.com/library/view/data-structures-and/9781118290279/13_chap08.html#ch008-sec022
        """
        bst = cls()

        if not array:
            return bst

        nodes = [value if value is None else cls.NODE_CLASS(value) for value in array]
        for i in range(1, len(nodes)):
            node = nodes[i]
            parent_index = (i - 1) // 2
            parent_node = nodes[parent_index]
            if (node is None) and (parent_node is None):
                continue
            if i % 2 == 0:
                parent_node.right = nodes[i]
            else:
                parent_node.left = nodes[i]

        bst.root = nodes[0]
        return bst
