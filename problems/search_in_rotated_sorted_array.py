# coding: utf-8
"""
https://leetcode.com/problems/search-in-rotated-sorted-array/
"""
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # The simple brute-force way is quick enough.
        for i, num in enumerate(nums):
            if num == target:
                return i
        return -1


class Solution2:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        while low <= high:
            m = (low + high) // 2
            if target == nums[m]:
                return m

            # The left side is sorted.
            if nums[low] <= nums[m]:
                # The left side has target which is the case of a normal binary search.
                if nums[low] <= target < nums[m]:
                    high = m - 1
                # Since the left side doesn't have target, we don't need to check the left side anymore.
                # So reset the low pointer to m + 1.
                else:
                    low = m + 1
            # The right side is sorted.
            elif nums[m] <= nums[high]:
                if nums[m] < target <= nums[high]:
                    low = m + 1
                else:
                    high = m - 1

        return -1
