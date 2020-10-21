# coding: utf-8
"""
https://leetcode.com/problems/median-of-two-sorted-arrays/
"""
from typing import List
import heapq
import statistics


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        sorted_nums = heapq.merge(nums1, nums2)
        return statistics.median(sorted_nums)


class Solution2:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        sorted_nums = []
        i1, leng1 = 0, len(nums1)
        i2, leng2 = 0, len(nums2)
        while True:
            try:
                n1 = nums1[i1]
            except IndexError:
                n1 = None

            try:
                n2 = nums2[i2]
            except IndexError:
                n2 = None

            if n1 is None:
                sorted_nums.extend(nums2[i2:])
                break
            elif n2 is None:
                sorted_nums.extend(nums1[i1:])
                break

            if n1 <= n2:
                sorted_nums.append(n1)
                i1 += 1
            else:
                sorted_nums.append(n2)
                i2 += 1

        max_index = leng1 + leng2 - 1
        if max_index == 0:
            return sorted_nums[0]

        index = max_index // 2
        if max_index % 2 == 0:
            return sorted_nums[index]
        else:
            return (sorted_nums[index] + sorted_nums[index + 1]) / 2


class Solution3:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def merge_nums():
            i1 = 0
            i2 = 0
            while True:
                try:
                    n1 = nums1[i1]
                except IndexError:
                    yield from nums2[i2:]
                    break

                try:
                    n2 = nums2[i2]
                except IndexError:
                    yield from nums1[i1:]
                    break

                if n1 <= n2:
                    yield n1
                    i1 += 1
                else:
                    yield n2
                    i2 += 1

        max_index = len(nums1) + len(nums2) - 1
        index = max_index // 2
        last_num = None
        for i, num in enumerate(merge_nums()):
            if i == index and max_index % 2 == 0:
                return num

            if i == index + 1:
                return (last_num + num) / 2

            last_num = num
