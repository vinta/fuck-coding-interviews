# coding: utf-8
"""
https://leetcode.com/problems/find-the-duplicate-number/
"""
from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums) + 1
        counts = [0, ] * n
        for num in nums:
            counts[num] += 1
            if counts[num] > 1:
                return num
