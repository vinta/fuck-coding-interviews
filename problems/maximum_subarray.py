# coding: utf-8
"""
https://leetcode.com/problems/maximum-subarray/
"""
from typing import List
import unittest


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = current_sum = nums[0]
        for num in nums[1:]:
            current_sum = current_sum + num

            # if the current sum is less than the current num
            # there is no reason to continue to sum
            if current_sum < num:
                current_sum = num

            if current_sum > max_sum:
                max_sum = current_sum

        return max_sum


class TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test(self):
        nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
        self.assertEqual(self.solution.maxSubArray(nums), 6)


unittest.main()
