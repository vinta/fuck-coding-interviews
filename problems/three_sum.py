# coding: utf-8
"""
https://leetcode.com/problems/3sum/
"""
from typing import List
import unittest


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # there might be multiple results
        def twoSum(nums, target):
            results = []
            index_dict = {}
            for i, num in enumerate(nums):
                complement = target - num
                if complement in index_dict:
                    results.append([complement, num])
                index_dict[num] = i
            return results

        results = []
        results_set = set()
        for i, num in enumerate(nums):
            if num == 0:
                target = 0
            else:
                target = -num

            two_nums_lists = twoSum(nums[0:i] + nums[i + 1:], target)
            if two_nums_lists:
                for two_nums_list in two_nums_lists:
                    result = sorted([num, ] + two_nums_list)
                    result_tuple = tuple(result)
                    if result_tuple not in results_set:
                        results_set.add(result_tuple)
                        results.append(result)

        return results
