# coding: utf-8
import random
import unittest

from algorithms.searching.binary_search import binary_search
from algorithms.searching.binary_search import binary_search_recursive


class TestCase(unittest.TestCase):
    def test(self):
        array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        target = random.choice(array)
        expected = array.index(target)
        self.assertEqual(binary_search(array, target), expected)

    def test2(self):
        array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        target = 100
        expected = -1
        self.assertEqual(binary_search(array, target), expected)

    def test3(self):
        array = []
        target = 0
        expected = -1
        self.assertEqual(binary_search(array, target), expected)


class TestCase2(unittest.TestCase):
    def test(self):
        array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        target = random.choice(array)
        expected = array.index(target)
        self.assertEqual(binary_search_recursive(array, target), expected)

    def test2(self):
        array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        target = 100
        expected = -1
        self.assertEqual(binary_search_recursive(array, target), expected)

    def test3(self):
        array = []
        target = 0
        expected = -1
        self.assertEqual(binary_search(array, target), expected)


if __name__ == '__main__':
    unittest.main()
