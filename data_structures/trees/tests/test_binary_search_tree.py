# coding: utf-8
import unittest
import random

from binarytree import Node
import binarytree
import pythonds3

from data_structures.trees.binary_search_tree import BinarySearchTree
from data_structures.trees.binary_search_tree import TreeNode


class TreeNodeTest(unittest.TestCase):
    def setUp(self):
        self.node = TreeNode(2)

    def test__repr__(self):
        self.assertTrue(repr(self.node))

    def test__str__(self):
        self.assertTrue(str(self.node))

    def test__eq__(self):
        other_node = TreeNode(2)
        self.assertEqual(self.node, other_node)

        node_a = TreeNode(2, left=TreeNode(1), right=TreeNode(3))
        node_b = TreeNode(2, left=TreeNode(1), right=TreeNode(3))
        self.assertEqual(node_a, node_b)

        other_node = TreeNode(22)
        self.assertNotEqual(self.node, other_node)


class BinarySearchTreeTest(unittest.TestCase):
    def setUp(self):
        self.empty_bst = BinarySearchTree()

        self.one_node_bst = BinarySearchTree()
        self.one_node_bst.insert(1)

        #     ______8
        #    /       \
        #   3__       10___
        #  /   \           \
        # 1     6          _14
        #      / \        /
        #     4   7      13
        self.insert_items = [8, 3, 10, 1, 6, 14, 4, 7, 13]
        self.bst = BinarySearchTree()
        for i in self.insert_items:
            self.bst.insert(i)

        root = Node(8)
        root.left = Node(3)
        root.right = Node(10)
        root.left.left = Node(1)
        root.left.right = Node(6)
        root.right.right = Node(14)
        root.left.right.left = Node(4)
        root.left.right.right = Node(7)
        root.right.right.left = Node(13)
        self.binarytree = root

    def test__eq__(self):
        tree_1 = BinarySearchTree()
        for i in self.insert_items:
            tree_1.insert(i)
        self.assertEqual(self.bst, tree_1)

        tree_2 = BinarySearchTree()
        for i in [1, 2, 3]:
            tree_2.insert(i)
        self.assertNotEqual(self.bst, tree_2)

        self.assertNotEqual(self.bst, self.empty_bst)

    def test__len__(self):
        self.assertEqual(len(self.empty_bst), 0)
        self.assertEqual(len(self.bst), len(self.insert_items))

    def test__iter__(self):
        items = list(self.bst)
        expected = [8, 3, 10, 1, 6, 14, 4, 7, 13]
        self.assertEqual(items, expected)

    def test__contains__(self):
        self.assertIn(random.choice(self.insert_items), self.bst)
        self.assertNotIn(100, self.bst)

    def test_is_valid(self):
        self.assertEqual(self.empty_bst.is_valid(), True)
        self.assertEqual(self.bst.is_valid(), True)

    def test_is_full(self):
        self.assertEqual(self.bst.is_full(), False)

    def test_is_complate(self):
        self.assertEqual(self.bst.is_complate(), False)

    def test_is_balanced(self):
        self.assertEqual(self.empty_bst.is_balanced(), True)
        self.assertEqual(self.one_node_bst.is_balanced(), True)
        self.assertEqual(self.bst.is_balanced(), False)

    def test_is_root(self):
        self.assertEqual(self.bst.is_root(self.bst.root), True)
        self.assertEqual(self.bst.is_root(self.bst.root.left), False)
        self.assertEqual(self.bst.is_root(self.bst.root.right), False)

    def test_children(self):
        self.assertEqual(list(self.bst.children(self.bst.root)), [self.bst.root.left, self.bst.root.right])
        self.assertEqual(list(self.bst.children(self.bst.root.left)), [self.bst.root.left.left, self.bst.root.left.right])
        self.assertEqual(list(self.bst.children(self.bst.root.right)), [self.bst.root.right.right, ])
        self.assertEqual(list(self.bst.children(self.bst.root.left.left)), [])

    def test_num_children(self):
        self.assertEqual(self.bst.num_children(self.bst.root), 2)
        self.assertEqual(self.bst.num_children(self.bst.root.left), 2)
        self.assertEqual(self.bst.num_children(self.bst.root.right), 1)
        self.assertEqual(self.bst.num_children(self.bst.root.left.left), 0)

    def test_is_leaf(self):
        self.assertEqual(self.bst.is_leaf(self.bst.root.left.left), True)
        self.assertEqual(self.bst.is_leaf(self.bst.root.left.right.left), True)
        self.assertEqual(self.bst.is_leaf(self.bst.root.left.right.right), True)
        self.assertEqual(self.bst.is_leaf(self.bst.root.right.right.left), True)
        self.assertEqual(self.bst.is_leaf(self.bst.root), False)
        self.assertEqual(self.bst.is_leaf(self.bst.root.left), False)
        self.assertEqual(self.bst.is_leaf(self.bst.root.right), False)

    def test_height(self):
        self.assertEqual(self.empty_bst.height(), -1)
        self.assertEqual(self.one_node_bst.height(), 0)
        self.assertEqual(self.bst.height(), 3)
        self.assertEqual(self.bst.height(self.bst.root.left.left), 0)
        self.assertEqual(self.bst.height(self.bst.root.left.right), 1)
        self.assertEqual(self.bst.height(self.bst.root.right), 2)

        self.bst.insert(15)
        self.bst.insert(30)
        self.assertEqual(self.bst.height(), 4)

    def test_depth(self):
        self.assertEqual(self.bst.depth(self.bst.root), 0)
        self.assertEqual(self.bst.depth(self.bst.root.right), 1)
        self.assertEqual(self.bst.depth(self.bst.root.right.right), 2)
        self.assertEqual(self.bst.depth(self.bst.root.left.right.left), 3)

        self.bst.insert(15)
        self.bst.insert(30)
        self.assertEqual(self.bst.depth(self.bst.root.right.right.right.right), 4)

    def test_level(self):
        self.assertEqual(self.bst.level(self.bst.root), 1)
        self.assertEqual(self.bst.level(self.bst.root.right), 2)
        self.assertEqual(self.bst.level(self.bst.root.right.right), 3)
        self.assertEqual(self.bst.level(self.bst.root.left.right.left), 4)

        self.bst.insert(15)
        self.bst.insert(30)
        self.assertEqual(self.bst.level(self.bst.root.right.right.right.right), 5)

    def test_num_edges(self):
        self.assertEqual(self.empty_bst.num_edges(), 0)
        self.assertEqual(self.bst.num_edges(), len(self.bst) - 1)

    def test_search(self):
        self.assertEqual(self.bst.search(8), self.bst.root)
        self.assertEqual(self.bst.search(1), self.bst.root.left.left)
        self.assertEqual(self.bst.search(13), self.bst.root.right.right.left)
        self.assertEqual(self.bst.search(100), None)

    def test_get_min_node(self):
        self.assertEqual(self.bst.get_min_node().value, min(self.insert_items))

    def test_get_max_node(self):
        self.assertEqual(self.bst.get_max_node().value, max(self.insert_items))

    def test_delete(self):
        with self.assertRaises(ValueError):
            self.bst.delete(100)

        bst2 = pythonds3.BinarySearchTree()
        for i in self.insert_items:
            bst2.put(key=i, value=i)

        #   ______8
        #  /       \
        # 3__       10___
        #    \           \
        #     6          _14
        #    / \        /
        #   4   7      13
        self.bst.delete(1)
        bst2.delete(1)
        self.assertEqual(len(self.bst), len(bst2))
        self.assertEqual(list(self.bst.traverse()), list(bst2))
        self.assertEqual(self.bst.is_valid(), True)

        #   ______10___
        #  /           \
        # 3__          _14
        #    \        /
        #     6      13
        #    / \
        #   4   7
        self.bst.delete(8)
        bst2.delete(8)
        self.assertEqual(len(self.bst), len(bst2))
        self.assertEqual(list(self.bst.traverse()), list(bst2))
        self.assertEqual(self.bst.is_valid(), True)

        #   ____10___
        #  /         \
        # 3__        _14
        #    \      /
        #     7    13
        #    /
        #   4
        self.bst.delete(6)
        bst2.delete(6)
        self.assertEqual(len(self.bst), len(bst2))
        self.assertEqual(list(self.bst.traverse()), list(bst2))
        self.assertEqual(self.bst.is_valid(), True)

        self.bst.delete(10)
        self.bst.delete(4)
        self.bst.delete(7)
        self.bst.delete(14)
        self.bst.delete(3)
        self.bst.delete(13)
        self.assertEqual(len(self.bst), 0)
        self.assertFalse(self.bst)
        self.assertEqual(self.bst.is_valid(), True)

    def test_inorder_traverse(self):
        items = list(self.bst.inorder_traverse())
        expected = [1, 3, 4, 6, 7, 8, 10, 13, 14]
        self.assertEqual(items, expected)

        items = list(self.bst.inorder_traverse(self.bst.root.right.left))
        expected = []
        self.assertEqual(items, expected)

    def test_preorder_traverse(self):
        items = list(self.bst.preorder_traverse())
        expected = [8, 3, 1, 6, 4, 7, 10, 14, 13]
        self.assertEqual(items, expected)

    def test_postorder_traverse(self):
        items = list(self.bst.postorder_traverse())
        expected = [1, 4, 7, 6, 3, 13, 14, 10, 8]
        self.assertEqual(items, expected)

    def test_levelorder_traverse(self):
        items = list(self.bst.levelorder_traverse())
        expected = [8, 3, 10, 1, 6, 14, 4, 7, 13]
        self.assertEqual(items, expected)

    def test_traverse(self):
        with self.assertRaises(ValueError):
            self.bst.traverse('NOT EXIST')

    def test_invert(self):
        self.empty_bst.invert()

        self.bst.invert()
        items = list(self.bst.levelorder_traverse())
        expected = [8, 10, 3, 14, 6, 1, 13, 7, 4]
        self.assertEqual(items, expected)
        self.assertEqual(self.bst.is_valid(), False)

    def test_to_array_representation(self):
        array = self.empty_bst.to_array_representation()
        self.assertEqual(array, [])

        array = self.bst.to_array_representation()
        root = binarytree.build(array)
        self.assertEqual(array, root.values)

    def test_from_array_representation(self):
        array = binarytree.bst(height=random.randint(0, 9), is_perfect=random.choice([True, False])).values
        bst = BinarySearchTree.from_array_representation(array)
        self.assertEqual(array, bst.to_array_representation())


if __name__ == '__main__':
    unittest.main()
