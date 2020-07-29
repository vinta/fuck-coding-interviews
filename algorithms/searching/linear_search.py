# coding: utf-8
"""
Linear Search
https://en.wikipedia.org/wiki/Linear_search

Worst-case performance: O(n)
Best-case performance: O(1)
Average performance: O(n)
"""


def linear_search(array, target):
    for i, item in enumerate(array):
        if item == target:
            return i

    return -1
