# coding: utf-8
"""
https://leetcode.com/problems/implement-trie-prefix-tree/s
"""
from typing import Dict


# There is another implementation without the intermediate node class:
# https://github.com/vinta/fuck-coding-interviews/blob/master/data_structures/trees/trie.py
class TrieNode:
    __slots__ = ['label', 'children', 'is_ended']

    def __init__(self, label):
        self.label = label
        self.children: Dict[str, TrieNode] = {}
        self.is_ended = False


class Trie:
    def __init__(self):
        self.root = TrieNode(label='')
        self.size = 0

    def __len__(self):
        return self.size

    def insert(self, word: str) -> None:
        if not word:
            raise ValueError('word cannot be empty')

        node = self.root
        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                new_child = TrieNode(label=char)
                node.children[char] = new_child
                node = new_child

        # Since the searched word might be shorter than the word in Trie,
        # search() needs a way to determine whether the searching matches the exact word,
        # For instance, we have `hammer`in Trie and we are searching for `hammers` which should return False.
        node.is_ended = True
        self.size += 1

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            try:
                node = node.children[char]
            except KeyError:
                return False

        if node.is_ended:
            return True
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            try:
                node = node.children[char]
            except KeyError:
                return False

        return True
