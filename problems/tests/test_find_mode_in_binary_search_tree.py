# coding: utf-8
import unittest

from problems.find_mode_in_binary_search_tree import Solution
from problems.utils.leetcode import deserialize_tree_str


class TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test(self):
        test_data = [
            {'tree_str': '[1,null,2,2]', 'expected': [2, ]},
            {'tree_str': '[1,null,2]', 'expected': [1, 2]},
        ]
        for data in test_data:
            tree_str = data['tree_str']
            expected = data['expected']
            with self.subTest(tree_str=tree_str):
                root = deserialize_tree_str(tree_str)
                output = self.solution.findMode(root)
                self.assertCountEqual(output, expected)


if __name__ == '__main__':
    unittest.main()
