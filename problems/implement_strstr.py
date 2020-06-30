# coding: utf-8
"""
https://leetcode.com/problems/implement-strstr/
"""
import unittest


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0

        n_length = len(needle)
        for i in range(len(haystack)):
            if haystack[i:i + n_length] == needle:
                return i

        return -1


class Solution2:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0

        n_length = len(needle)
        h_length = len(haystack)

        if h_length < n_length:
            return -1

        for i in range(h_length - n_length + 1):
            if haystack[i:i + n_length] == needle:
                return i

        return -1


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
