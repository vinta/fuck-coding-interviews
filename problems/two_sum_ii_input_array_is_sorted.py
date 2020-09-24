# coding: utf-8
"""
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
"""
from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # NOTE: numbers is in increasing order.
        left = 0  # The left pointer starts from the leftmost index whose value is minimum.
        right = len(numbers) - 1  # The right pointer starts from the rightmost index whose value is maximum.
        while left < right:
            current_sum = numbers[left] + numbers[right]
            if current_sum == target:
                # Returned indexes are 1-based.
                return [left + 1, right + 1]
            elif current_sum < target:
                left += 1
            elif current_sum > target:
                right -= 1
