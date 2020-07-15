# coding: utf-8
"""
https://leetcode.com/problems/group-anagrams/
"""
from collections import defaultdict
from typing import List


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
