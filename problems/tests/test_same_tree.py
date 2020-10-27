# coding: utf-8
import unittest

from problems.same_tree import Solution
from problems.utils.leetcode import deserialize_tree_str


class TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test(self):
        test_data = [
            {'p_tree_str': '[1,2,3]', 'q_tree_str': '[1,2,3]', 'expected': True},
            {'p_tree_str': '[1,2]', 'q_tree_str': '[1,null,2]', 'expected': False},
            {'p_tree_str': '[1,2,1]', 'q_tree_str': '[1,1,2]', 'expected': False},
        ]
        for data in test_data:
            p_tree_str = data['p_tree_str']
            q_tree_str = data['q_tree_str']
            expected = data['expected']
            with self.subTest(p_tree_str=p_tree_str, q_tree_str=q_tree_str):
                p = deserialize_tree_str(p_tree_str)
                q = deserialize_tree_str(q_tree_str)
                output = self.solution.isSameTree(p, q)
                self.assertEqual(output, expected)


if __name__ == '__main__':
    unittest.main()
