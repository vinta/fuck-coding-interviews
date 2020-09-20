# coding: utf-8
"""
https://leetcode.com/problems/third-maximum-number/
"""
from typing import List
import heapq


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        sorted_nums = sorted(set(nums), reverse=True)
        third_max = None
        for i in range(3):
            try:
                third_max = sorted_nums[i]
            except IndexError:
                return sorted_nums[0]
        return third_max


class Solution2:
    def thirdMax(self, nums: List[int]) -> int:
        max_heap = []
        for num in nums:
            heapq.heappush(max_heap, -num)

        order = 0
        last_num = None
        for _ in range(len(nums)):
            num = -heapq.heappop(max_heap)
            if num != last_num:
                order += 1
                if order == 3:
                    return num
            last_num = num

        return max(nums)


class Solution3:
    def thirdMax(self, nums: List[int]) -> int:
        dedup_nums = set()
        max_heap = []
        for num in nums:
            if num not in dedup_nums:
                dedup_nums.add(num)
                heapq.heappush(max_heap, -num)

        if len(max_heap) < 3:
            return -heapq.heappop(max_heap)
        else:
            third_max = None
            for _ in range(3):
                third_max = -heapq.heappop(max_heap)
            return third_max
