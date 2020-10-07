# coding: utf-8
"""
https://leetcode.com/problems/sort-colors/
"""
from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        def counting_sort(arr, max_num_in_array):
            counts = [0, ] * (max_num_in_array + 1)
            for num in arr:
                counts[num] += 1

            i = 0
            for num, count in enumerate(counts):
                for _ in range(count):
                    arr[i] = num
                    i += 1

        counting_sort(nums, 2)
