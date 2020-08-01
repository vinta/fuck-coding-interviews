# coding: utf-8
import unittest

from problems.univalued_binary_tree import Solution
from problems.utils.leetcode import deserialize_tree_str


class TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test(self):
        test_data = [
            {'tree_str': '[1,1,1,1,1,null,1]', 'expected': True},
            {'tree_str': '[2,2,2,5,2]', 'expected': False},
            {'tree_str': '[1]', 'expected': True},
            {'tree_str': '[]', 'expected': True},
        ]
        for data in test_data:
            tree_str = data['tree_str']
            expected = data['expected']
            with self.subTest(tree_str=tree_str, expected=expected):
                root = deserialize_tree_str(tree_str)
                output = self.solution.isUnivalTree(root)
                self.assertEqual(output, expected)


if __name__ == '__main__':
    unittest.main()
