# coding: utf-8
import unittest

from problems.kth_smallest_element_in_a_bst import Solution
from problems.utils.leetcode import deserialize_tree_str


class TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test(self):
        test_data = [
            {'tree_str': '[3,1,4,null,2]', 'k': 1, 'expected': 1},
            {'tree_str': '[5,3,6,2,4,null,null,1]', 'k': 3, 'expected': 3},
        ]
        for data in test_data:
            tree_str = data['tree_str']
            k = data['k']
            expected = data['expected']
            with self.subTest(tree_str=tree_str, k=k):
                root = deserialize_tree_str(tree_str)
                output = self.solution.kthSmallest(root, k)
                self.assertEqual(output, expected)


if __name__ == '__main__':
    unittest.main()
