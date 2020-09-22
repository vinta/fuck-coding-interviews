# coding: utf-8
"""
https://leetcode.com/problems/single-number/
"""
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        counter = {}
        for num in nums:
            if num not in counter:
                counter[num] = 1
            else:
                counter[num] += 1

        for num, count in counter.items():
            if count == 1:
                return num
