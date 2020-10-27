# coding: utf-8
import unittest

from problems.subsets import Solution
from problems.subsets import Solution2
from problems.subsets import Solution3


class TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test(self):
        nums = [1, 2, 3]
        expected = [
            [],
            [1],
            [2],
            [3],
            [1, 2],
            [1, 3],
            [2, 3],
            [1, 2, 3],
        ]
        self.assertCountEqual(self.solution.subsets(nums), expected)

    def test2(self):
        nums = []
        expected = [
            [],
        ]
        self.assertCountEqual(self.solution.subsets(nums), expected)

    def test3(self):
        nums = [1]
        expected = [
            [],
            [1, ],
        ]
        self.assertCountEqual(self.solution.subsets(nums), expected)

    def test4(self):
        nums = [1, 2]
        expected = [
            [],
            [1, ],
            [2, ],
            [1, 2],
        ]
        self.assertCountEqual(self.solution.subsets(nums), expected)


class TestCase2(unittest.TestCase):
    def setUp(self):
        self.solution = Solution2()

    def test(self):
        nums = [1, 2, 3]
        expected = [
            [],
            [1],
            [2],
            [3],
            [1, 2],
            [1, 3],
            [2, 3],
            [1, 2, 3],
        ]
        self.assertCountEqual(self.solution.subsets(nums), expected)

    def test2(self):
        nums = []
        expected = [
            [],
        ]
        self.assertCountEqual(self.solution.subsets(nums), expected)

    def test3(self):
        nums = [1]
        expected = [
            [],
            [1, ],
        ]
        self.assertCountEqual(self.solution.subsets(nums), expected)

    def test4(self):
        nums = [1, 2]
        expected = [
            [],
            [1, ],
            [2, ],
            [1, 2],
        ]
        self.assertCountEqual(self.solution.subsets(nums), expected)


class TestCase3(unittest.TestCase):
    def setUp(self):
        self.solution = Solution3()

    def test(self):
        nums = [1, 2, 3]
        expected = [
            [],
            [1],
            [2],
            [3],
            [1, 2],
            [1, 3],
            [2, 3],
            [1, 2, 3],
        ]
        self.assertCountEqual(self.solution.subsets(nums), expected)

    def test2(self):
        nums = []
        expected = [
            [],
        ]
        self.assertCountEqual(self.solution.subsets(nums), expected)

    def test3(self):
        nums = [1]
        expected = [
            [],
            [1, ],
        ]
        self.assertCountEqual(self.solution.subsets(nums), expected)

    def test4(self):
        nums = [1, 2]
        expected = [
            [],
            [1, ],
            [2, ],
            [1, 2],
        ]
        self.assertCountEqual(self.solution.subsets(nums), expected)


if __name__ == '__main__':
    unittest.main()
