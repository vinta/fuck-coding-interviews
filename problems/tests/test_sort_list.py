# coding: utf-8
import unittest

from problems.sort_list import Solution
from problems.sort_list import Solution2
from problems.sort_list import Solution3
from problems.utils.leetcode import list_to_listnode
from problems.utils.leetcode import listnode_to_list


class TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test(self):
        test_array = [
            {'arr': [4, 2, 1, 3]},
            {'arr': [-1, 5, 3, 4, 0]},
            {'arr': [1, 2, 3, 4, 5]},
            {'arr': []},
        ]
        for data in test_array:
            arr = data['arr']
            expected = sorted(data['arr'])
            with self.subTest(arr=arr):
                head = list_to_listnode(arr)
                result = self.solution.sortList(head)
                self.assertEqual(listnode_to_list(result), expected)


class TestCase2(unittest.TestCase):
    def setUp(self):
        self.solution = Solution2()

    def test(self):
        test_array = [
            {'arr': [4, 2, 1, 3]},
            {'arr': [-1, 5, 3, 4, 0]},
            {'arr': [1, 2, 3, 4, 5]},
            {'arr': []},
        ]
        for data in test_array:
            arr = data['arr']
            expected = sorted(data['arr'])
            with self.subTest(arr=arr):
                head = list_to_listnode(arr)
                result = self.solution.sortList(head)
                self.assertEqual(listnode_to_list(result), expected)


class TestCase3(unittest.TestCase):
    def setUp(self):
        self.solution = Solution3()

    def test(self):
        test_array = [
            {'arr': [4, 2, 1, 3]},
            {'arr': [-1, 5, 3, 4, 0]},
            {'arr': [1, 2, 3, 4, 5]},
            {'arr': []},
        ]
        for data in test_array:
            arr = data['arr']
            expected = sorted(data['arr'])
            with self.subTest(arr=arr):
                head = list_to_listnode(arr)
                result = self.solution.sortList(head)
                self.assertEqual(listnode_to_list(result), expected)


if __name__ == '__main__':
    unittest.main()
