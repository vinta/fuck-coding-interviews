# coding: utf-8
"""
https://leetcode.com/problems/permutations/
"""
from typing import List
import itertools


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return itertools.permutations(nums)


class Solution2:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def gen_results(elements):
            # Base case
            if len(elements) <= 1:
                yield elements  # elements is a list.

            # Recursive case
            else:
                for i, first in enumerate(elements):
                    other_elements = elements[:i] + elements[i + 1:]
                    for arr in gen_results(other_elements):
                        yield [first, ] + arr

        return gen_results(nums)


class Solution3:
    def permute(self, nums: List[int]) -> List[List[int]]:
        results = []
        length = len(nums)

        def build_results(items, result):
            if len(result) == length:
                results.append(result[:])
                return

            for i, item in enumerate(items):
                result.append(item)

                pool_items = items[:i] + items[i + 1:]
                build_results(pool_items, result)

                result.pop()

        build_results(nums, [])
        return results
