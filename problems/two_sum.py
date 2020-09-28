# coding: utf-8
"""
https://leetcode.com/problems/two-sum/
"""
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Is there duplicates in `nums`?
        for i, num1 in enumerate(nums):
            for j, num2 in enumerate(nums[i + 1:]):
                if num1 + num2 == target:
                    real_index = j + i + 1
                    return [i, real_index]


class Solution2:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapping = {
            # num: index
        }
        for i, num in enumerate(nums):
            mapping[num] = i

        for i, num in enumerate(nums):
            another = target - num
            try:
                # We cannot use the same element twice, so both returned indexes must be distinct.
                another_i = mapping[another]
                if another_i == i:
                    continue
                else:
                    return [i, another_i]
            except KeyError:
                continue


class Solution3:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapping = {
            # num: index
        }
        for i, num in enumerate(nums):
            another = target - num
            another_i = mapping.get(another)
            if another_i is not None:  # NOTE: The index of another might be 0, so we cannot use `if another_i:`.
                return [another_i, i]
            mapping[num] = i
