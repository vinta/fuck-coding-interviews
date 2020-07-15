# coding: utf-8
"""
https://leetcode.com/problems/maximum-subarray/
"""
from typing import List


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
