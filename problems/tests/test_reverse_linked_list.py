# coding: utf-8
import unittest

from problems.reverse_linked_list import Solution
from problems.reverse_linked_list import Solution2
from problems.utils.leetcode import list_to_listnode
from problems.utils.leetcode import listnode_to_list


class TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test(self):
        head = list_to_listnode([1, 2, 3, 4, 5])
        expected_head = self.solution.reverseList(head)
        expected = [5, 4, 3, 2, 1]
        self.assertEqual(listnode_to_list(expected_head), expected)


class TestCase2(unittest.TestCase):
    def setUp(self):
        self.solution = Solution2()

    def test(self):
        head = list_to_listnode([1, 2, 3, 4, 5])
        expected_head = self.solution.reverseList(head)
        expected = [5, 4, 3, 2, 1]
        self.assertEqual(listnode_to_list(expected_head), expected)


if __name__ == '__main__':
    unittest.main()
