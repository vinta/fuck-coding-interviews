# coding: utf-8
"""
https://leetcode.com/problems/contains-duplicate/
"""
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dedup_list = set(nums)
        if nums and (len(nums) != len(dedup_list)):
            return True

        return False


class Solution2:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dedup_set = set()
        for num in nums:
            if num in dedup_set:
                return True
            dedup_set.add(num)

        return False
