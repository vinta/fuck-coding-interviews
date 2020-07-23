# coding: utf-8
import unittest

from problems.top_k_frequent_elements import Solution


class TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test(self):
        nums = [1, 1, 1, 2, 2, 3]
        k = 2
        expected = [1, 2]
        self.assertEqual(self.solution.topKFrequent(nums, k), expected)

    def test2(self):
        nums = [1, ]
        k = 1
        expected = [1, ]
        self.assertEqual(self.solution.topKFrequent(nums, k), expected)


if __name__ == '__main__':
    unittest.main()
