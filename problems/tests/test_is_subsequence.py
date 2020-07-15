# coding: utf-8
import unittest

from problems.is_subsequence import Solution


class TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test(self):
        s = 'abc'
        t = 'ahbgdc'
        self.assertEqual(self.solution.isSubsequence(s, t), True)

    def test2(self):
        s = 'bale'
        t = 'abppplee'
        self.assertEqual(self.solution.isSubsequence(s, t), False)

    def test3(self):
        s = ''
        t = ''
        self.assertEqual(self.solution.isSubsequence(s, t), True)


if __name__ == '__main__':
    unittest.main()
