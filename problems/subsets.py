# coding: utf-8
"""
https://leetcode.com/problems/subsets/
"""
from itertools import combinations
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        output = []
        for i in range(0, len(nums) + 1):
            output.extend([list(p) for p in combinations(nums, i)])

        return output


class Solution2:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def gen_results(arr):
            # Base case
            if len(arr) <= 0:
                yield []

            # Recursive case
            else:
                for p in gen_results(arr[1:]):
                    yield [arr[0], ] + p
                    yield p

        return gen_results(nums)


class Solution3:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        results = []

        def build_results(items, result):
            results.append(result[:])

            for i, item in enumerate(items):
                result.append(item)

                pool_items = items[i + 1:]
                build_results(pool_items, result)

                result.pop()

        build_results(nums, [])
        return results
