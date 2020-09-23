# coding: utf-8
import unittest

from problems.path_sum import Solution
from problems.utils.leetcode import deserialize_tree_str


class TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test(self):
        test_data = [
            {'tree_str': '[5,4,8,11,null,13,4,7,2,null,null,null,1]', 'path_sum': 22, 'expected': True},
        ]
        for data in test_data:
            tree_str = data['tree_str']
            path_sum = data['path_sum']
            expected = data['expected']
            with self.subTest(tree_str=tree_str, path_sum=path_sum, expected=expected):
                root = deserialize_tree_str(tree_str)
                self.assertEqual(self.solution.hasPathSum(root, path_sum), expected)


if __name__ == '__main__':
    unittest.main()
