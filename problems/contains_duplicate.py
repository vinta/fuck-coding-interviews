# coding: utf-8
"""
https://leetcode.com/problems/contains-duplicate/
"""
from typing import List
import unittest


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dedup_list = set(nums)
        if nums and (len(nums) != len(dedup_list)):
            return True

        return False


class Solution2:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dedup_set = set()
        for num in nums:
            if num in dedup_set:
                return True
            dedup_set.add(num)

        return False


class TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test(self):
        nums = [1, 2, 3, 1]
        self.assertEqual(self.solution.containsDuplicate(nums), True)


class TestCase2(unittest.TestCase):
    def setUp(self):
        self.solution = Solution2()

    def test(self):
        nums = [1, 2, 3, 1]
        self.assertEqual(self.solution.containsDuplicate(nums), True)


if __name__ == '__main__':
    unittest.main()
