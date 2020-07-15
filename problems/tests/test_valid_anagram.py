# coding: utf-8
import unittest

from problems.valid_anagram import Solution
from problems.valid_anagram import Solution2
from problems.valid_anagram import Solution3


class TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test(self):
        s = 'anagram'
        t = 'nagaram'
        self.assertEqual(self.solution.isAnagram(s, t), True)


class TestCase2(unittest.TestCase):
    def setUp(self):
        self.solution = Solution2()

    def test(self):
        s = 'anagram'
        t = 'nagaram'
        self.assertEqual(self.solution.isAnagram(s, t), True)


class TestCase3(unittest.TestCase):
    def setUp(self):
        self.solution = Solution3()

    def test(self):
        s = 'anagram'
        t = 'nagaram'
        self.assertEqual(self.solution.isAnagram(s, t), True)


if __name__ == '__main__':
    unittest.main()
