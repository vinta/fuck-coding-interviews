# coding: utf-8
import unittest

from problems.merge_k_sorted_lists import Solution
from problems.utils.leetcode import list_to_listnode
from problems.utils.leetcode import listnode_to_list


class TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test(self):
        test_array = [
            {
                'lists': [
                    [1, 4, 5],
                    [1, 3, 4],
                    [2, 6],
                ],
                'expected': [1, 1, 2, 3, 4, 4, 5, 6],
            },
        ]
        for data in test_array:
            lists = [list_to_listnode(array) for array in data['lists']]
            expected = data['expected']
            with self.subTest(lists=lists):
                head = self.solution.mergeKLists(lists)
                self.assertEqual(listnode_to_list(head), expected)


if __name__ == '__main__':
    unittest.main()
