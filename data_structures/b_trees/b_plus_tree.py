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
        new_right.values = self.values[median_index + 1:]  # values are data.
        for child in new_right.values:
            child.parent = new_right

        self.keys = self.keys[:median_index]
        self.values = self.values[:median_index + 1]  # NOTE: Here is "median_index + 1" instead of "median_index".

        self.parent.add_child(median_key, new_right)

    def borrow_left(self, my_index):
        if my_index == 0:  # There is no left sibling.
            return False

        left_sibling = self.parent.values[my_index - 1]
        if len(left_sibling.keys) <= math.ceil(self.tree.order / 2) - 1:
            return False

        node = self
        sibling = left_sibling
        if self.is_leaf():
            borrowed_key = left_sibling.keys.pop(-1)
            borrowed_value = left_sibling.values.pop(-1)
            self.keys.insert(0, borrowed_key)
            self.values.insert(0, borrowed_value)

            # Update separator keys in the parent.
            for i, child in enumerate(self.parent.values[1:]):
                self.parent.keys[i] = child.keys[0]
        else:
            parent_key = node.parent.keys.pop(-1)
            sibling_key = sibling.keys.pop(-1)
            data = sibling.values.pop(-1)
            data.parent = node

            node.parent.keys.insert(0, sibling_key)
            node.keys.insert(0, parent_key)
            node.values.insert(0, data)

        return True

    def borrow_right(self, my_index):
        if my_index == len(self.parent.values) - 1:  # There is no right sibling.
            return False

        right_sibling = self.parent.values[my_index + 1]
        if len(right_sibling.keys) <= math.ceil(self.tree.order / 2) - 1:
            return False

        node = self
        sibling = right_sibling
        if self.is_leaf():
            borrowed_key = right_sibling.keys.pop(0)
            borrowed_value = right_sibling.values.pop(0)
            self.keys.append(borrowed_key)
            self.values.append(borrowed_value)

            # Update separator keys in the parent.
            for i, child in enumerate(self.parent.values[1:]):
                self.parent.keys[i] = child.keys[0]
        else:
            parent_key = node.parent.keys.pop(0)
            sibling_key = sibling.keys.pop(0)
            data = sibling.values.pop(0)
            data.parent = node

            node.parent.keys.append(sibling_key)
            node.keys.append(parent_key)
            node.values.append(data)

        return True

    def update_separator(self, deleted_key):
        def next_smallest_key():
            key = ''
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

    def merge_left(self, my_index):  # Merge the current node into the left sibling.
        if my_index == 0:
            return False

        left_sibling_index = my_index - 1
        left_sibling = self.parent.values[left_sibling_index]
        if len(left_sibling.keys) != math.ceil(self.tree.order / 2) - 1:  # We can only merge a sibling which has exactly the minimum number of keys.
            return False

        # Drop the current node from the parent,
        # also drop the the separator key since the parent lose a child.
        separator_index = left_sibling_index
        parent_separator_key = self.parent.keys.pop(separator_index)
        left_sibling.parent.values.pop(my_index)

        if left_sibling.is_leaf():
            left_sibling.next = self.next
        else:
            # Drag the separator key into the merged node.
            left_sibling.keys.append(parent_separator_key)
            for child in self.values:
                child.parent = left_sibling

        left_sibling.keys.extend(self.keys)
        left_sibling.values.extend(self.values)

        if left_sibling.parent.is_underflow():
            left_sibling.parent.rebalance()

        return True

    def merge_right(self, my_index):  # Merge the right sibling into the current node.
        if my_index == len(self.parent.values) - 1:
            return False

        right_sibling_index = my_index + 1
        right_sibling = self.parent.values[right_sibling_index]
        if len(right_sibling.keys) != math.ceil(self.tree.order / 2) - 1:  # We can only merge a sibling which has exactly the minimum number of keys.
            return False

        # Drop the right sibling from the parent,
        # also drop the the separator key since the parent lose a child.
        separator_index = my_index
        parent_separator_key = self.parent.keys.pop(separator_index)
        self.parent.values.pop(right_sibling_index)

        if self.is_leaf():
            self.next = right_sibling.next
        else:
            # Drag the separator key into the merged node.
            self.keys.append(parent_separator_key)
            for child in right_sibling.values:
                child.parent = self

        self.keys.extend(right_sibling.keys)
        self.values.extend(right_sibling.values)

        if self.parent.is_underflow():
            self.parent.rebalance()

        return True

    def rebalance(self):
        if self.is_root():
            # If we land here, the root node has no keys but one child node.
            # So we promote the only child as the new root.
            new_root = self.values[0]
            new_root.parent = None
            self.tree.root = new_root
            return True

        my_index = self.parent.values.index(self)
        assert \
            self.borrow_left(my_index) or self.borrow_right(my_index) or \
            self.merge_left(my_index) or self.merge_right(my_index)


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

    def delete(self, key):
        index = bisect.bisect_left(self.keys, key)
        self.keys.pop(index)
        self.values.pop(index)

        # If we remove the smallest element in a leaf,
        # then find the *next* smallest element,
        # go up our parent stack,
        # and fix index keys.
        if index == 0 and self.parent:
            self.update_separator(key)

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

    @staticmethod
    def _find(node: Node, key):
        for i, item in enumerate(node.keys):
            if key < item:
                return node.values[i], i
            elif i + 1 == len(node.keys):
                return node.values[i + 1], i + 1  # return right-most node/pointer.

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
