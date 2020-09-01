# coding: utf-8
"""
B+ Tree
https://en.wikipedia.org/wiki/B%2B_tree
"""
import bisect
import math


class Node:
    __slots__ = ['tree', 'parent', 'keys', 'values']

    def __init__(self, tree, parent=None):
        self.tree = tree
        self.parent = parent
        self.keys = []
        self.values = []

    def __repr__(self):
        return f'{self.__class__.__name__}({self.keys})'

    def __str__(self):
        return self.__repr__()

    def is_root(self):
        return self.parent is None

    def is_leaf(self):
        return isinstance(self, LeafNode)

    def is_overflow(self):
        return len(self.keys) > self.tree.order - 1

    def is_underflow(self):
        if self.is_root():
            if self.is_leaf():
                return False
            else:
                return len(self.keys) < 2 - 1

        return len(self.keys) < math.ceil(self.tree.order / 2) - 1

    def create_new_root(self):
        new_root = Node(tree=self.tree)
        self.tree.root = new_root
        self.parent = new_root
        self.parent.values = [self, ]

    def add_child(self, new_key, new_child):
        child_index = bisect.bisect_left(self.keys, new_key)
        self.keys.insert(child_index, new_key)
        self.values.insert(child_index + 1, new_child)
        if self.is_overflow():
            self.split()

    def split(self):
        if self.is_root():
            self.create_new_root()

        median_index = self.tree.order // 2
        median_key = self.keys[median_index]

        new_right = Node(tree=self.tree, parent=self.parent)
        new_right.keys = self.keys[median_index + 1:]
        new_right.values = self.values[median_index + 1:]  # values here are child nodes.
        for child in new_right.values:
            child.parent = new_right

        self.keys = self.keys[:median_index]
        self.values = self.values[:median_index + 1]  # NOTE: Here is "median_index + 1" instead of "median_index".

        self.parent.add_child(median_key, new_right)

    def immediate_siblings(self):
        if self.is_root():
            return None, None

        my_index = self.parent.values.index(self)
        if my_index == 0:
            left_sibling = None
        else:
            left_sibling = self.parent.values[my_index - 1]
        if my_index == len(self.parent.values) - 1:
            right_sibling = None
        else:
            right_sibling = self.parent.values[my_index + 1]

        return left_sibling, right_sibling

    def borrow_left(self, left_sibling, my_index):
        borrowed_key = left_sibling.keys.pop(-1)
        borrowed_value = left_sibling.values.pop(-1)

        if self.is_leaf():
            self.keys.insert(0, borrowed_key)
            self.values.insert(0, borrowed_value)

            # Update separator keys in the parent.
            for i, child in enumerate(self.parent.values[1:]):
                self.parent.keys[i] = child.keys[0]
        else:
            # This procedure is the same as B-Tree's.
            borrowed_value.parent = self

            separator_index = my_index - 1  # The separator key between the left sibling and the current node.
            separator = self.parent.keys[separator_index]
            self.parent.keys[separator_index] = borrowed_key

            self.keys.insert(0, separator)
            self.values.insert(0, borrowed_value)

        return True

    def borrow_right(self, right_sibling, my_index):
        borrowed_key = right_sibling.keys.pop(0)
        borrowed_value = right_sibling.values.pop(0)

        if self.is_leaf():
            self.keys.append(borrowed_key)
            self.values.append(borrowed_value)

            # Update separator keys in the parent.
            for i, child in enumerate(self.parent.values[1:]):
                self.parent.keys[i] = child.keys[0]
        else:
            # This procedure is the same as B-Tree's.
            borrowed_value.parent = self

            separator_index = my_index  # The separator key between the current node and the right sibling.
            separator = self.parent.keys[separator_index]
            self.parent.keys[separator_index] = borrowed_key

            self.keys.append(separator)
            self.values.append(borrowed_value)

        return True

    def merge(self, left_node, right_node):  # Merge the right node into the left node.
        index = left_node.parent.values.index(right_node)

        # Drop the current node from the parent,
        # also drop the the separator key since the parent lose a child.
        left_node.parent.values.pop(index)
        parent_separator_key = left_node.parent.keys.pop(index - 1)

        if left_node.is_leaf():
            left_node.next = right_node.next
        else:
            # Drag the separator key into the merged node.
            left_node.keys.append(parent_separator_key)
            for child in right_node.values:
                child.parent = left_node

        left_node.keys.extend(right_node.keys)
        left_node.values.extend(right_node.values)

        if left_node.parent.is_underflow():
            left_node.parent.rebalance()

    def rebalance(self):
        if self.is_root():
            # If we land here, the root node has no keys but one child node.
            # So we promote the only child as the new root.
            new_root = self.values[0]
            new_root.parent = None
            self.tree.root = new_root
            return True

        my_index = self.parent.values.index(self)
        left_sibling, right_sibling = self.immediate_siblings()

        # We can only merge a sibling which has exactly the minimum number of keys.
        if left_sibling and (len(left_sibling.keys) > math.ceil(self.tree.order / 2) - 1):
            self.borrow_left(left_sibling, my_index)
        elif right_sibling and (len(right_sibling.keys) > math.ceil(self.tree.order / 2) - 1):
            self.borrow_right(right_sibling, my_index)
        elif left_sibling and len(left_sibling.keys) == math.ceil(self.tree.order / 2) - 1:
            self.merge(left_sibling, self)
        elif right_sibling and len(right_sibling.keys) == math.ceil(self.tree.order / 2) - 1:
            self.merge(self, right_sibling)

    def check_validation(self):
        if len(self.tree):
            # assert self.keys
            assert self.keys == sorted(set(self.keys)), self.keys

        num_values = len(self.values)
        assert num_values <= self.tree.order, num_values

        if self.is_leaf():
            for value in self.values:
                assert not isinstance(value, (Node, LeafNode))
        else:
            # Internal nodes.
            if self.is_root():
                assert num_values >= 2, num_values
            else:
                assert num_values >= math.ceil(self.tree.order / 2), num_values

            assert num_values - 1 == len(self.keys)

            for child in self.values:
                assert isinstance(child, (Node, LeafNode))
                assert child.parent == self
                child.check_validation()


class LeafNode(Node):
    __slots__ = ['tree', 'parent', 'keys', 'values', 'previous', 'next']

    def __init__(self, tree, parent=None):
        super().__init__(tree, parent=parent)
        self.previous = None
        self.next = None

    def split(self):
        if self.is_root():
            self.create_new_root()

        median_index = self.tree.order // 2
        median_key = self.keys[median_index]

        new_right = LeafNode(tree=self.tree, parent=self.parent)
        new_right.keys = self.keys[median_index:]
        new_right.values = self.values[median_index:]  # values are nodes.
        new_right.previous = self
        new_right.next = self.next

        self.keys = self.keys[:median_index]
        self.values = self.values[:median_index]
        self.next = new_right

        self.parent.add_child(median_key, new_right)

    def insert(self, key, value):
        index = bisect.bisect_left(self.keys, key)
        self.keys.insert(index, key)
        self.values.insert(index, value)
        if self.is_overflow():
            self.split()

    def update_parent_separator(self, deleted_key):
        def next_smallest_key():
            key = None
            if len(self.keys) > 0:
                key = self.keys[0]
            else:
                if self.next:
                    key = self.next.keys[0]
            return key

        parent = self.parent
        while parent:
            for i, key in enumerate(parent.keys):
                if key == deleted_key:
                    parent.keys[i] = next_smallest_key()
                    return
            parent = parent.parent

    def delete(self, key):
        index = bisect.bisect_left(self.keys, key)
        self.keys.pop(index)
        self.values.pop(index)

        # NOTE: If we remove the smallest element in a leaf node,
        # we must replace the separator key in the parent or grandparent
        # with the next smallest element.
        if index == 0 and self.parent:
            self.update_parent_separator(key)

        if self.is_underflow():
            self.rebalance()


class BPlusTree:
    DEFAULT_TO_ROOT = object()

    def __init__(self, order=512):
        if order < 3:
            raise ValueError('order must be greater than or equal to 3')

        self.size = 0
        self.order = order
        self.root = LeafNode(tree=self)
        self.head = self.root

    def __len__(self):
        return self.size

    def __iter__(self):
        leaf_node = self.head
        while leaf_node:
            yield from leaf_node.keys
            leaf_node = leaf_node.next

    def search_node(self, key, node):
        if isinstance(node, LeafNode):
            return node

        child_index = bisect.bisect_right(node.keys, key)
        return self.search_node(key, node.values[child_index])

    def get(self, key):
        node = self.search_node(key, self.root)
        index = bisect.bisect_left(node.keys, key)
        if index < len(node.keys) and node.keys[index] == key:
            return node.values[index]

        raise KeyError('Not found')

    def insert(self, key, value):
        node = self.search_node(key, self.root)
        index = bisect.bisect_left(node.keys, key)
        if index < len(node.keys) and node.keys[index] == key:
            raise KeyError('Duplicate key')

        node.insert(key, value)
        self.size += 1

    def delete(self, key):
        node = self.search_node(key, self.root)
        index = bisect.bisect_left(node.keys, key)
        if index < len(node.keys) and node.keys[index] != key:
            raise KeyError('Not found')

        node.delete(key)
        self.size -= 1

    def min(self):
        try:
            return {'key': self.head.keys[0], 'value': self.head.values[0]}
        except IndexError:
            raise KeyError('Tree is empty')

    def max(self):
        last_leaf = self.head
        while last_leaf.next:
            last_leaf = last_leaf.next

        try:
            return {'key': last_leaf.keys[-1], 'value': last_leaf.values[-1]}
        except IndexError:
            raise KeyError('Tree is empty')

    def levelorder_traverse_nodes(self, node=DEFAULT_TO_ROOT):
        if node == self.DEFAULT_TO_ROOT:
            node = self.root

        current_level = [self.root, ]
        while current_level:
            next_level = []
            for node in current_level:
                yield node
                if not isinstance(node, LeafNode):
                    next_level.extend(node.values)

            current_level = next_level
