# coding: utf-8
"""
Multiset
https://en.wikipedia.org/wiki/Multiset

Multiset is a set which allows duplicates, and keeps track of how many times each elements appear.

Actually, a multiset is more like a hash map which keys are elements and values are counts of each elements.
"""
from collections import defaultdict


class Multiset:
    def __init__(self, iterable=()):
        self.dict = defaultdict(int)
        self.size = 0
        for elem in iterable:
            self.add(elem)

    def __len__(self):
        return self.size

    def __contains__(self, elem):
        return elem in self.dict

    def __iter__(self):
        for elem, count in self.dict.items():
            for _ in range(count):
                yield elem

    def add(self, elem):
        self.dict[elem] += 1
        self.size += 1

    def discard(self, elem):
        count = self.dict[elem]
        if count > 0:
            self.dict[elem] -= 1
            self.size -= 1

        if count <= 0:
            del self.dict[elem]

    def discard_all(self, elem):
        count = self.dict[elem]
        self.size = self.size - count
        del self.dict[elem]

    def num_unique_elements(self):
        return len(self.dict)
