# coding: utf-8
import unittest

from problems.balanced_binary_tree import Solution
from problems.utils.leetcode import deserialize_tree_str


class TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test(self):
        test_data = [
            {'input': '[]', 'expected': True},
            {'input': '[3,9,20,null,null,15,7]', 'expected': True},
            {'input': '[1,2,2,3,3,null,null,4,4]', 'expected': False},
            {'input': '[1,null,2,null,3]', 'expected': False},
        ]
        for data in test_data:
            tree_str = data['input']
            expected = data['expected']
            with self.subTest(tree_str=tree_str, expected=expected):
                root = deserialize_tree_str(tree_str)
                output = self.solution.isBalanced(root)
                self.assertEqual(output, expected)


if __name__ == '__main__':
    unittest.main()
