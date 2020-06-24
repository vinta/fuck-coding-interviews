# coding: utf-8
"""
https://leetcode.com/problems/merge-intervals/
"""
from typing import List
import unittest


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) <= 1:
            return intervals

        intervals.sort(key=lambda x: x[0])

        first_pair = intervals[0]
        output = [first_pair, ]
        for pair in intervals[1:]:
            last_merged_pair = output[-1]

            # if the current pair's low is greater than the last merged pair's high
            # it must be a new interval
            if pair[0] > last_merged_pair[1]:
                output.append(pair)
                continue

            if pair[1] > last_merged_pair[1]:
                last_merged_pair[1] = pair[1]

        return output


class TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test(self):
        intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
        expected = [[1, 6], [8, 10], [15, 18]]
        self.assertEqual(self.solution.merge(intervals), expected)

    def test2(self):
        intervals = [[1, 4], [4, 5], [5, 6]]
        expected = [[1, 6]]
        self.assertEqual(self.solution.merge(intervals), expected)

    def test3(self):
        intervals = [[2, 3], [1, 4]]
        expected = [[1, 4]]
        self.assertEqual(self.solution.merge(intervals), expected)


if __name__ == '__main__':
    unittest.main()
