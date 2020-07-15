# coding: utf-8
import unittest

from problems.remove_nth_node_from_end_of_list import Solution
from problems.remove_nth_node_from_end_of_list import Solution2
from problems.utils.leetcode import list_to_listnode
from problems.utils.leetcode import listnode_to_list


class TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test(self):
        head = list_to_listnode([1, 2, 3, 4, 5])
        n = 2
        expected_head = self.solution.removeNthFromEnd(head, n)
        expected = [1, 2, 3, 5]
        self.assertEqual(listnode_to_list(expected_head), expected)

    def test2(self):
        head = list_to_listnode([1, 2, 3, 4, 5])
        n = 1
        expected_head = self.solution.removeNthFromEnd(head, n)
        expected = [1, 2, 3, 4]
        self.assertEqual(listnode_to_list(expected_head), expected)

    def test3(self):
        head = list_to_listnode([1, 2])
        n = 2
        expected_head = self.solution.removeNthFromEnd(head, n)
        expected = [2]
        self.assertEqual(listnode_to_list(expected_head), expected)

    def test4(self):
        head = list_to_listnode([1])
        n = 1
        expected_head = self.solution.removeNthFromEnd(head, n)
        expected = []
        self.assertEqual(listnode_to_list(expected_head), expected)


class TestCase2(unittest.TestCase):
    def setUp(self):
        self.solution = Solution2()

    def test(self):
        head = list_to_listnode([1, 2, 3, 4, 5])
        n = 2
        expected_head = self.solution.removeNthFromEnd(head, n)
        expected = [1, 2, 3, 5]
        self.assertEqual(listnode_to_list(expected_head), expected)

    def test2(self):
        head = list_to_listnode([1, 2, 3, 4, 5])
        n = 1
        expected_head = self.solution.removeNthFromEnd(head, n)
        expected = [1, 2, 3, 4]
        self.assertEqual(listnode_to_list(expected_head), expected)

    def test3(self):
        head = list_to_listnode([1, 2])
        n = 2
        expected_head = self.solution.removeNthFromEnd(head, n)
        expected = [2]
        self.assertEqual(listnode_to_list(expected_head), expected)

    def test4(self):
        head = list_to_listnode([1])
        n = 1
        expected_head = self.solution.removeNthFromEnd(head, n)
        expected = []
        self.assertEqual(listnode_to_list(expected_head), expected)


if __name__ == '__main__':
    unittest.main()
