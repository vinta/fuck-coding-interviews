# coding: utf-8
import unittest

from problems.merge_intervals import Solution


class TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test(self):
        intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
        expected = [[1, 6], [8, 10], [15, 18]]
        self.assertEqual(self.solution.merge(intervals), expected)

    def test2(self):
        intervals = [[1, 4], [4, 5], [5, 6]]
        expected = [[1, 6]]
        self.assertEqual(self.solution.merge(intervals), expected)

    def test3(self):
        intervals = [[2, 3], [1, 4]]
        expected = [[1, 4]]
        self.assertEqual(self.solution.merge(intervals), expected)


if __name__ == '__main__':
    unittest.main()
