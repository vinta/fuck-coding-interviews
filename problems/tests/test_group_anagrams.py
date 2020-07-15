# coding: utf-8
import unittest

from problems.group_anagrams import Solution


class TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test(self):
        strs = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']
        expected = [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
        self.assertCountEqual(self.solution.groupAnagrams(strs), expected)


if __name__ == '__main__':
    unittest.main()
