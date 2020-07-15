# coding: utf-8
import unittest

from problems.implement_strstr import Solution
from problems.implement_strstr import Solution2


class TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test(self):
        haystack = 'hello'
        needle = 'll'
        expected = 2
        self.assertEqual(self.solution.strStr(haystack, needle), expected)

    def test2(self):
        haystack = 'aaaaa'
        needle = 'bba'
        expected = -1
        self.assertEqual(self.solution.strStr(haystack, needle), expected)

    def test3(self):
        haystack = 'xyz'
        needle = ''
        expected = 0
        self.assertEqual(self.solution.strStr(haystack, needle), expected)

    def test4(self):
        haystack = 'hello'
        needle = 'lo'
        expected = 3
        self.assertEqual(self.solution.strStr(haystack, needle), expected)

    def test5(self):
        haystack = 'aaa'
        needle = 'aaaaaaa'
        expected = -1
        self.assertEqual(self.solution.strStr(haystack, needle), expected)


class TestCase2(unittest.TestCase):
    def setUp(self):
        self.solution = Solution2()

    def test(self):
        haystack = 'hello'
        needle = 'll'
        expected = 2
        self.assertEqual(self.solution.strStr(haystack, needle), expected)

    def test2(self):
        haystack = 'aaaaa'
        needle = 'bba'
        expected = -1
        self.assertEqual(self.solution.strStr(haystack, needle), expected)

    def test3(self):
        haystack = 'xyz'
        needle = ''
        expected = 0
        self.assertEqual(self.solution.strStr(haystack, needle), expected)

    def test4(self):
        haystack = 'hello'
        needle = 'lo'
        expected = 3
        self.assertEqual(self.solution.strStr(haystack, needle), expected)

    def test5(self):
        haystack = 'aaa'
        needle = 'aaaaaaa'
        expected = -1
        self.assertEqual(self.solution.strStr(haystack, needle), expected)


if __name__ == '__main__':
    unittest.main()
