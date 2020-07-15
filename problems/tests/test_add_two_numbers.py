# coding: utf-8
import unittest

from problems.add_two_numbers import Solution
from problems.utils.leetcode import list_to_listnode
from problems.utils.leetcode import listnode_to_list


class TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test(self):
        l1 = list_to_listnode([2, 4, 3])
        l2 = list_to_listnode([5, 6, 4])
        expected_head = self.solution.addTwoNumbers(l1, l2)
        expected = [7, 0, 8]
        self.assertEqual(listnode_to_list(expected_head), expected)

    def test2(self):
        l1 = list_to_listnode([0, 1, 0, 9])
        l2 = list_to_listnode([1, 9, 9])
        expected_head = self.solution.addTwoNumbers(l1, l2)
        expected = [1, 0, 0, 0, 1]
        self.assertEqual(listnode_to_list(expected_head), expected)


if __name__ == '__main__':
    unittest.main()
