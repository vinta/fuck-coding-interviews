# coding: utf-8
"""
https://leetcode.com/problems/two-sum/
"""
from typing import List
import unittest


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, num1 in enumerate(nums):
            for j, num2 in enumerate(nums[i + 1:]):
                if num1 + num2 == target:
                    real_index = j + i + 1
                    return [i, real_index]


class Solution2:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # there might be duplicates in `nums`
        index_dict = {}
        for index, num in enumerate(nums):
            complement = target - num
            if complement in index_dict:
                # return [index, index_dict[complement]]
                return [index_dict[complement], index]
            index_dict[num] = index


class TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test(self):
        nums = [2, 3, 7, 11, 15, 3]
        target = 6
        self.assertEqual(self.solution.twoSum(nums, target), [1, 5])


class TestCase2(unittest.TestCase):
    def setUp(self):
        self.solution = Solution2()

    def test(self):
        nums = [2, 3, 7, 11, 15, 3]
        target = 6
        self.assertEqual(self.solution.twoSum(nums, target), [1, 5])


if __name__ == '__main__':
    unittest.main()
