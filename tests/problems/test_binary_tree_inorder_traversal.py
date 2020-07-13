# coding: utf-8
import unittest

from problems.binary_tree_inorder_traversal import Solution
from problems.utils.leetcode import deserialize_tree_str
from problems.utils.leetcode import list_to_compact_str


class TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test(self):
        test_data = [
            {'input': '[1,null,2,3]', 'expected': '[1,3,2]'},
            {'input': '[3,2,null,1]', 'expected': '[1,2,3]'},
            {'input': '[3,1,null,null,2]', 'expected': '[1,2,3]'},
            {'input': '[2,1,3]', 'expected': '[1,2,3]'},
            {'input': '[1,null,2,null,3]', 'expected': '[1,2,3]'},
            {'input': '[1,2,3,null,null,4,5]', 'expected': '[2,1,4,3,5]'},
            {'input': '[5,4,7,3,null,2,null,-1,null,9]', 'expected': '[-1,3,4,5,9,2,7]'},
            {'input': '[8,3,10,1,6,null,14,null,null,4,7,13]', 'expected': '[1,3,4,6,7,8,10,13,14]'},
            {'input': '[]', 'expected': '[]'},
        ]
        for data in test_data:
            tree_str = data['input']
            expected = data['expected']
            with self.subTest(tree_str=tree_str, expected=expected):
                root = deserialize_tree_str(tree_str)
                output = list_to_compact_str(self.solution.inorderTraversal(root))
                self.assertEqual(output, expected)


if __name__ == '__main__':
    unittest.main()
