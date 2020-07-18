# coding: utf-8
import unittest

from problems.validate_binary_search_tree import Solution
from problems.validate_binary_search_tree import Solution2
from problems.utils.leetcode import deserialize_tree_str


class TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test(self):
        test_data = [
            {'input': '[]', 'expected': True},
            {'input': '[2,1,3]', 'expected': True},
            {'input': '[5,1,4,null,null,3,6]', 'expected': False},
            {'input': '[1,1]', 'expected': False},
        ]
        for data in test_data:
            tree_str = data['input']
            expected = data['expected']
            with self.subTest(tree_str=tree_str, expected=expected):
                root = deserialize_tree_str(tree_str)
                output = self.solution.isValidBST(root)
                self.assertEqual(output, expected)


class TestCase2(unittest.TestCase):
    def setUp(self):
        self.solution = Solution2()

    def test(self):
        test_data = [
            {'input': '[]', 'expected': True},
            {'input': '[2,1,3]', 'expected': True},
            {'input': '[5,1,4,null,null,3,6]', 'expected': False},
            {'input': '[1,1]', 'expected': False},
        ]
        for data in test_data:
            tree_str = data['input']
            expected = data['expected']
            with self.subTest(tree_str=tree_str, expected=expected):
                root = deserialize_tree_str(tree_str)
                output = self.solution.isValidBST(root)
                self.assertEqual(output, expected)


if __name__ == '__main__':
    unittest.main()
