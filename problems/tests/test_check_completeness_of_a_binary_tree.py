# coding: utf-8
import unittest

from problems.check_completeness_of_a_binary_tree import Solution
from problems.utils.leetcode import deserialize_tree_str


class TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test(self):
        test_data = [
            {'input': '[1,2,3,4,5,6]', 'expected': True},
            {'input': '[1,2,3,4,5,null,7]', 'expected': False},
            {'input': '[1,2,3,5,null,7,8]', 'expected': False},
        ]
        for data in test_data:
            tree_str = data['input']
            expected = data['expected']
            with self.subTest(tree_str=tree_str):
                root = deserialize_tree_str(tree_str)
                output = self.solution.isCompleteTree(root)
                self.assertEqual(output, expected)


if __name__ == '__main__':
    unittest.main()
