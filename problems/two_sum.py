# coding: utf-8
"""
https://leetcode.com/problems/two-sum/
"""
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, num1 in enumerate(nums):
            for j, num2 in enumerate(nums[i + 1:]):
                if num1 + num2 == target:
                    real_index = j + i + 1
                    return [i, real_index]


class Solution2:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # there might be duplicates in `nums`
        mapping = {
            # num: index
        }
        for i, num in enumerate(nums):
            another = target - num
            another_i = mapping.get(another)
            if another_i is not None:
                return [another_i, i]
            mapping[num] = i
