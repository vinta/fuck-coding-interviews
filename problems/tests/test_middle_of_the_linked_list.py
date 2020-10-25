# coding: utf-8
import unittest

from problems.middle_of_the_linked_list import Solution
from problems.middle_of_the_linked_list import Solution2
from problems.utils.leetcode import list_to_listnode
from problems.utils.leetcode import listnode_to_list


class TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test(self):
        test_array = [
            {'arr': [1, 2, 3, 4, 5], 'expected': [3, 4, 5]},
            {'arr': [1, 2, 3, 4, 5, 6], 'expected': [4, 5, 6]},
            {'arr': [], 'expected': []},
        ]
        for data in test_array:
            arr = data['arr']
            expected = data['expected']
            with self.subTest(arr=arr):
                head = list_to_listnode(arr)
                result = self.solution.middleNode(head)
                self.assertEqual(listnode_to_list(result), expected)


class TestCase2(unittest.TestCase):
    def setUp(self):
        self.solution = Solution2()

    def test(self):
        test_array = [
            {'arr': [1, 2, 3, 4, 5], 'expected': [3, 4, 5]},
            {'arr': [1, 2, 3, 4, 5, 6], 'expected': [4, 5, 6]},
            {'arr': [], 'expected': []},
        ]
        for data in test_array:
            arr = data['arr']
            expected = data['expected']
            with self.subTest(arr=arr):
                head = list_to_listnode(arr)
                result = self.solution.middleNode(head)
                self.assertEqual(listnode_to_list(result), expected)


if __name__ == '__main__':
    unittest.main()
