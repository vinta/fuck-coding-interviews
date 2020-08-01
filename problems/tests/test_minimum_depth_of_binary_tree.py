# coding: utf-8
import unittest

from problems.minimum_depth_of_binary_tree import Solution
from problems.utils.leetcode import deserialize_tree_str


class TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test(self):
        test_data = [
            {'tree_str': '[3,9,20,null,null,15,7]', 'expected': 2},
            {'tree_str': '[1]', 'expected': 1},
            {'tree_str': '[]', 'expected': 0},
        ]
        for data in test_data:
            tree_str = data['tree_str']
            expected = data['expected']
            with self.subTest(tree_str=tree_str, expected=expected):
                root = deserialize_tree_str(tree_str)
                output = self.solution.minDepth(root)
                self.assertEqual(output, expected)


if __name__ == '__main__':
    unittest.main()
