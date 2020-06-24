# coding: utf-8
"""
https://leetcode.com/problems/group-anagrams/
"""
from collections import defaultdict
from typing import List
import unittest


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_words = defaultdict(list)
        for word in strs:
            sorted_word = str(sorted(word))
            sorted_words[sorted_word].append(word)

        output = []
        for word_list in sorted_words.values():
            output.append(word_list)

        return output


class TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test(self):
        strs = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']
        expected = [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
        self.assertCountEqual(self.solution.groupAnagrams(strs), expected)


if __name__ == '__main__':
    unittest.main()
