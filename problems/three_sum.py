# coding: utf-8
"""
https://leetcode.com/problems/3sum/
"""
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        dedup_set = set(nums)
        length_dedup_set = len(dedup_set)
        if length_dedup_set <= 1:
            if sum(dedup_set) == 0 and len(nums) >= 3:
                return [[0, 0, 0]]
            return []

        nums.sort()

        # there might be multiple results
        def twoSum(nums, target):
            results = []
            index_dict = {}
            for num in nums:
                complement = target - num
                if complement in index_dict:
                    results.append([num, complement])
                else:
                    index_dict[num] = None
            return results

        results = []
        results_set = set()
        first_nums = set()
        for i, num in enumerate(nums):
            if num in first_nums:
                continue
            else:
                first_nums.add(num)

            if num == 0:
                target = 0
            else:
                target = -num

            two_nums_lists = twoSum(nums[i + 1:], target)
            if two_nums_lists:
                for two_nums_list in two_nums_lists:
                    result = sorted([num, ] + two_nums_list)
                    result_tuple = tuple(result)
                    if result_tuple not in results_set:
                        results_set.add(result_tuple)
                        results.append(result)

        return results
