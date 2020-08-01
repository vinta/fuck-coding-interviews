# coding: utf-8
import unittest

from problems.binary_tree_level_order_traversal import Solution
from problems.utils.leetcode import deserialize_tree_str


class TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test(self):
        test_data = [
            {'tree_str': '[3,9,20,null,null,15,7]', 'expected': [[3], [9, 20], [15, 7]]},
        ]
        for data in test_data:
            tree_str = data['tree_str']
            expected = data['expected']
            with self.subTest(tree_str=tree_str, expected=expected):
                root = deserialize_tree_str(tree_str)
                output = self.solution.levelOrder(root)
                self.assertEqual(output, expected)


if __name__ == '__main__':
    unittest.main()
