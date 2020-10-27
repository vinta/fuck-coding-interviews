# coding: utf-8
import unittest

from problems.combinations import Solution
from problems.combinations import Solution2


class TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test(self):
        expected = [
            [2, 4],
            [3, 4],
            [2, 3],
            [1, 2],
            [1, 3],
            [1, 4],
        ]
        results = []
        for result in self.solution.combine(n=4, k=2):
            results.append(list(result))
        self.assertCountEqual(results, expected)

    def test2(self):
        expected = [
            [1],
        ]
        results = []
        for result in self.solution.combine(n=1, k=1):
            results.append(list(result))
        self.assertCountEqual(results, expected)


class TestCase2(unittest.TestCase):
    def setUp(self):
        self.solution = Solution2()

    def test(self):
        expected = [
            [2, 4],
            [3, 4],
            [2, 3],
            [1, 2],
            [1, 3],
            [1, 4],
        ]
        self.assertCountEqual(self.solution.combine(n=4, k=2), expected)

    def test2(self):
        expected = [
            [1],
        ]
        self.assertCountEqual(self.solution.combine(n=1, k=1), expected)


if __name__ == '__main__':
    unittest.main()
