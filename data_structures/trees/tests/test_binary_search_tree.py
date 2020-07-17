# coding: utf-8
import unittest
import random

import binarytree
import pythonds3

from data_structures.trees.binary_search_tree import BinarySearchTree
from data_structures.trees.binary_search_tree import TreeNode


class TreeNodeTest(unittest.TestCase):
    def setUp(self):
        self.node = TreeNode(2)

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

    def test_is_root(self):
        self.assertTrue(self.bst.is_root(self.bst.root))
        self.assertFalse(self.bst.is_root(self.bst.root.left))
        self.assertFalse(self.bst.is_root(self.bst.root.right))

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
        self.assertTrue(self.bst.is_leaf(self.bst.root.left.left))
        self.assertTrue(self.bst.is_leaf(self.bst.root.left.right.left))
        self.assertTrue(self.bst.is_leaf(self.bst.root.left.right.right))
        self.assertTrue(self.bst.is_leaf(self.bst.root.right.right.left))

        self.assertFalse(self.bst.is_leaf(self.bst.root))
        self.assertFalse(self.bst.is_leaf(self.bst.root.left))
        self.assertFalse(self.bst.is_leaf(self.bst.root.right))

    def test_height(self):
        self.assertEqual(self.empty_bst.height(self.empty_bst.root), 0)
        self.assertEqual(self.bst.height(self.bst.root), 3)
        self.assertEqual(self.bst.height(self.bst.root.left.left), 0)
        self.assertEqual(self.bst.height(self.bst.root.left.right), 1)
        self.assertEqual(self.bst.height(self.bst.root.right), 2)

        self.bst.insert(15)
        self.bst.insert(30)
        self.assertEqual(self.bst.height(self.bst.root), 4)

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
        self.assertEqual(self.bst.get_min_node(self.bst.root).value, min(self.insert_items))

    def test_get_max_node(self):
        self.assertEqual(self.bst.get_max_node(self.bst.root).value, max(self.insert_items))

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

        self.bst.delete(10)
        self.bst.delete(4)
        self.bst.delete(7)
        self.bst.delete(14)
        self.bst.delete(3)
        self.bst.delete(13)
        self.assertEqual(len(self.bst), 0)
        self.assertFalse(self.bst)

    def test_inorder_traverse(self):
        items = list(self.bst.inorder_traverse(self.bst.root))
        expected = [1, 3, 4, 6, 7, 8, 10, 13, 14]
        self.assertEqual(items, expected)

        items = list(self.bst.inorder_traverse(self.bst.root.right.left))
        expected = []
        self.assertEqual(items, expected)

    def test_preorder_traverse(self):
        items = list(self.bst.preorder_traverse(self.bst.root))
        expected = [8, 3, 1, 6, 4, 7, 10, 14, 13]
        self.assertEqual(items, expected)

    def test_postorder_traverse(self):
        items = list(self.bst.postorder_traverse(self.bst.root))
        expected = [1, 4, 7, 6, 3, 13, 14, 10, 8]
        self.assertEqual(items, expected)

    def test_levelorder_traverse(self):
        items = list(self.bst.levelorder_traverse(self.bst.root))
        expected = [8, 3, 10, 1, 6, 14, 4, 7, 13]
        self.assertEqual(items, expected)

    def test_traverse(self):
        with self.assertRaises(ValueError):
            self.bst.traverse('NOT EXIST')

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
