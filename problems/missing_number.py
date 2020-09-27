# coding: utf-8
"""
https://leetcode.com/problems/missing-number/
"""
from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        occurences = [0, ] * (n + 1)
        for num in nums:
            occurences[num] = 1

        for i, occur in enumerate(occurences):
            if occur == 0:
                return i


class Solution2:
    def missingNumber(self, nums: List[int]) -> int:
        return sum(range(0, len(nums) + 1)) - sum(nums)
