# coding: utf-8
import unittest

from problems.power_of_two import Solution
from problems.power_of_two import Solution2
from problems.power_of_two import Solution3


class TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test(self):
        test_data = [
            {'n': 0, 'expected': False},
            {'n': 1, 'expected': True},
            {'n': 2, 'expected': True},
            {'n': 1024, 'expected': True},
            {'n': 100000, 'expected': False},
        ]
        for data in test_data:
            n = data['n']
            expected = data['expected']
            with self.subTest(n=n):
                self.assertEqual(self.solution.isPowerOfTwo(n), expected)


class TestCase2(unittest.TestCase):
    def setUp(self):
        self.solution = Solution2()

    def test(self):
        test_data = [
            {'n': 0, 'expected': False},
            {'n': 1, 'expected': True},
            {'n': 2, 'expected': True},
            {'n': 1024, 'expected': True},
            {'n': 100000, 'expected': False},
        ]
        for data in test_data:
            n = data['n']
            expected = data['expected']
            with self.subTest(n=n):
                self.assertEqual(self.solution.isPowerOfTwo(n), expected)


class TestCase3(unittest.TestCase):
    def setUp(self):
        self.solution = Solution3()

    def test(self):
        test_data = [
            {'n': 0, 'expected': False},
            {'n': 1, 'expected': True},
            {'n': 2, 'expected': True},
            {'n': 1024, 'expected': True},
            {'n': 100000, 'expected': False},
        ]
        for data in test_data:
            n = data['n']
            expected = data['expected']
            with self.subTest(n=n):
                self.assertEqual(self.solution.isPowerOfTwo(n), expected)


if __name__ == '__main__':
    unittest.main()
