# coding: utf-8
import random
import unittest

from algorithms.searching.binary_search import binary_search
from algorithms.searching.binary_search import binary_search_recursive


class TestCase(unittest.TestCase):
    def test(self):
        sorted_array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        target = random.choice(sorted_array)
        expected = sorted_array.index(target)
        self.assertEqual(binary_search(sorted_array, target), expected)

    def test2(self):
        sorted_array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        target = 100
        expected = -1
        self.assertEqual(binary_search(sorted_array, target), expected)

    def test3(self):
        sorted_array = []
        target = 0
        expected = -1
        self.assertEqual(binary_search(sorted_array, target), expected)


class TestCase2(unittest.TestCase):
    def test(self):
        sorted_array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        target = random.choice(sorted_array)
        expected = sorted_array.index(target)
        self.assertEqual(binary_search_recursive(sorted_array, target), expected)

    def test2(self):
        sorted_array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        target = 100
        expected = -1
        self.assertEqual(binary_search_recursive(sorted_array, target), expected)

    def test3(self):
        sorted_array = []
        target = 0
        expected = -1
        self.assertEqual(binary_search(sorted_array, target), expected)


if __name__ == '__main__':
    unittest.main()
