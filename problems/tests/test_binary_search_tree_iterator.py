# coding: utf-8
import unittest

from problems.binary_search_tree_iterator import BSTIterator
from problems.utils.leetcode import deserialize_tree_str


class TestCase(unittest.TestCase):
    def setUp(self):
        root = deserialize_tree_str('[7,3,15,null,null,9,20]')
        self.bst_iterator = BSTIterator(root)

    def test(self):
        self.assertEqual(self.bst_iterator.next(), 3)
        self.assertEqual(self.bst_iterator.next(), 7)
        self.assertEqual(self.bst_iterator.hasNext(), True)
        self.assertEqual(self.bst_iterator.next(), 9)
        self.assertEqual(self.bst_iterator.hasNext(), True)
        self.assertEqual(self.bst_iterator.next(), 15)
        self.assertEqual(self.bst_iterator.hasNext(), True)
        self.assertEqual(self.bst_iterator.next(), 20)
        self.assertEqual(self.bst_iterator.hasNext(), False)


if __name__ == '__main__':
    unittest.main()
