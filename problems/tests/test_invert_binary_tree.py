# coding: utf-8
import unittest

from problems.invert_binary_tree import Solution
from problems.invert_binary_tree import Solution2
from problems.utils.leetcode import deserialize_tree_str
from problems.utils.leetcode import serialize_treenode


class TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test(self):
        test_data = [
            {'input': '[4,2,7,1,3,6,9]', 'expected': '[4,7,2,9,6,3,1]'},
            {'input': '[]', 'expected': '[]'},
        ]
        for data in test_data:
            tree_str = data['input']
            expected = data['expected']
            with self.subTest(tree_str=tree_str, expected=expected):
                root = deserialize_tree_str(tree_str)
                output = self.solution.invertTree(root)
                self.assertEqual(serialize_treenode(output), expected)


class TestCase2(unittest.TestCase):
    def setUp(self):
        self.solution = Solution2()

    def test(self):
        test_data = [
            {'input': '[4,2,7,1,3,6,9]', 'expected': '[4,7,2,9,6,3,1]'},
            {'input': '[]', 'expected': '[]'},
        ]
        for data in test_data:
            tree_str = data['input']
            expected = data['expected']
            with self.subTest(tree_str=tree_str, expected=expected):
                root = deserialize_tree_str(tree_str)
                output = self.solution.invertTree(root)
                self.assertEqual(serialize_treenode(output), expected)


if __name__ == '__main__':
    unittest.main()
