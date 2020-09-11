# coding: utf-8
import unittest

from problems.merge_two_sorted_lists import Solution
from problems.merge_two_sorted_lists import Solution2
from problems.merge_two_sorted_lists import Solution3
from problems.utils.leetcode import list_to_listnode
from problems.utils.leetcode import listnode_to_list


class TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test(self):
        test_array = [
            {'l1': [1, 2, 4], 'l2': [1, 3, 4], 'expected': [1, 1, 2, 3, 4, 4]},
        ]
        for data in test_array:
            l1 = list_to_listnode(data['l1'])
            l2 = list_to_listnode(data['l2'])
            expected = data['expected']
            with self.subTest(l1=l1, l2=l2):
                head = self.solution.mergeTwoLists(l1, l2)
                self.assertEqual(listnode_to_list(head), expected)


class TestCase2(unittest.TestCase):
    def setUp(self):
        self.solution = Solution2()

    def test(self):
        test_array = [
            {'l1': [1, 2, 4], 'l2': [1, 3, 4], 'expected': [1, 1, 2, 3, 4, 4]},
        ]
        for data in test_array:
            l1 = list_to_listnode(data['l1'])
            l2 = list_to_listnode(data['l2'])
            expected = data['expected']
            with self.subTest(l1=l1, l2=l2):
                head = self.solution.mergeTwoLists(l1, l2)
                self.assertEqual(listnode_to_list(head), expected)


class TestCase3(unittest.TestCase):
    def setUp(self):
        self.solution = Solution3()

    def test(self):
        test_array = [
            {'l1': [1, 2, 4], 'l2': [1, 3, 4], 'expected': [1, 1, 2, 3, 4, 4]},
        ]
        for data in test_array:
            l1 = list_to_listnode(data['l1'])
            l2 = list_to_listnode(data['l2'])
            expected = data['expected']
            with self.subTest(l1=l1, l2=l2):
                head = self.solution.mergeTwoLists(l1, l2)
                self.assertEqual(listnode_to_list(head), expected)


if __name__ == '__main__':
    unittest.main()
