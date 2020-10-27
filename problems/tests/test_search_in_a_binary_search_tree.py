# coding: utf-8
import unittest

from problems.search_in_a_binary_search_tree import Solution
from problems.search_in_a_binary_search_tree import Solution2
from problems.utils.leetcode import deserialize_tree_str
from problems.utils.leetcode import serialize_treenode


class TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test(self):
        test_data = [
            {'input': '[4,2,7,1,3]', 'target': 2, 'expected': '[2,1,3]'},
            {'input': '[4,2,7,1,3]', 'target': 100, 'expected': '[]'},
            {'input': '[8,3,10,1,6,null,14,null,null,4,7,13]', 'target': 3, 'expected': '[3,1,6,null,null,4,7]'},
            {'input': '[]', 'target': 0, 'expected': '[]'},
        ]
        for data in test_data:
            tree_str = data['input']
            target = data['target']
            expected = data['expected']
            with self.subTest(tree_str=tree_str, target=target):
                root = deserialize_tree_str(tree_str)
                output = self.solution.searchBST(root, target)
                self.assertEqual(serialize_treenode(output), expected)


class TestCase2(unittest.TestCase):
    def setUp(self):
        self.solution = Solution2()

    def test(self):
        test_data = [
            {'input': '[4,2,7,1,3]', 'target': 2, 'expected': '[2,1,3]'},
            {'input': '[4,2,7,1,3]', 'target': 100, 'expected': '[]'},
            {'input': '[8,3,10,1,6,null,14,null,null,4,7,13]', 'target': 3, 'expected': '[3,1,6,null,null,4,7]'},
            {'input': '[]', 'target': 0, 'expected': '[]'},
        ]
        for data in test_data:
            tree_str = data['input']
            target = data['target']
            expected = data['expected']
            with self.subTest(tree_str=tree_str, target=target):
                root = deserialize_tree_str(tree_str)
                output = self.solution.searchBST(root, target)
                self.assertEqual(serialize_treenode(output), expected)


if __name__ == '__main__':
    unittest.main()
