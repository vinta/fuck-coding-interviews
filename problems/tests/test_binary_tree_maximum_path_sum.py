# coding: utf-8
import unittest

from problems.binary_tree_maximum_path_sum import Solution
from problems.utils.leetcode import deserialize_tree_str


class TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test(self):
        test_data = [
            {'input': '[1,2,3]', 'expected': 6},
            {'input': '[-10,9,20,null,null,15,7]', 'expected': 42},
            {'input': '[-3]', 'expected': -3},
            {'input': '[2,-1]', 'expected': 2},
            {'input': '[1,-2,3]', 'expected': 4},
            {'input': '[5,4,8,11,null,13,4,7,2,null,null,null,1]', 'expected': 48},
        ]
        for data in test_data:
            tree_str = data['input']
            expected = data['expected']
            with self.subTest(tree_str=tree_str, expected=expected):
                root = deserialize_tree_str(tree_str)
                self.assertEqual(self.solution.maxPathSum(root), expected)


if __name__ == '__main__':
    unittest.main()
