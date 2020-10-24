# coding: utf-8
import random
import unittest

from algorithms.searching.binary_search import binary_search
from algorithms.searching.binary_search import binary_search_recursive
from algorithms.searching.binary_search import binary_search_left_bound


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


class TestCase3(unittest.TestCase):
    def test(self):
        test_lists = [
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            [1, 2, 2, 2, 2, 3, 4],
            [1, 1, 1, 2, 2, 2, 3, 3, 3],
            [3],
            [3, 3],
            [3] * random.randint(1, 10),
        ]
        for sorted_array in test_lists:
            with self.subTest(sorted_array=sorted_array):
                target = random.choice(sorted_array)
                expected = sorted_array.index(target)
                self.assertEqual(binary_search_left_bound(sorted_array, target), expected)

                target = 100
                expected = -1
                self.assertEqual(binary_search_left_bound(sorted_array, target), expected)

    def test2(self):
        sorted_array = []
        target = 0
        expected = -1
        self.assertEqual(binary_search_left_bound(sorted_array, target), expected)

    def test3(self):
        sorted_array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        target = 100
        expected = -1
        self.assertEqual(binary_search_left_bound(sorted_array, target), expected)


if __name__ == '__main__':
    unittest.main()
