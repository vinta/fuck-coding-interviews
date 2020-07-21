# coding: utf-8
import unittest

from algorithms.sorting.quick_sort import quick_sort
from algorithms.sorting.quick_sort import quick_sort_in_place


class TestCase(unittest.TestCase):
    def test(self):
        test_lists = [
            [5, 7, 1, 9, 5, 5, -4, 3, 0, 2],
            [],
            [1, ],
            [1, 2],
            [1, 2, 3],
            [3, 2, 1],
            [1, 2, 3, 4],
            [4, 3, 2, 1],
            [1, 1, 1, 1],
            [-2, 3, -5],
            [-1, 2, -8, -10],
        ]
        for array in test_lists:
            with self.subTest(array=array):
                self.assertEqual(quick_sort(array.copy()), sorted(array))


class TestCase2(unittest.TestCase):
    def test(self):
        test_lists = [
            [5, 7, 1, 9, 5, 5, -4, 3, 0, 2],
            [],
            [1, ],
            [1, 2],
            [1, 2, 3],
            [3, 2, 1],
            [1, 2, 3, 4],
            [4, 3, 2, 1],
            [1, 1, 1, 1],
            [-2, 3, -5],
            [-1, 2, -8, -10],
        ]
        for array in test_lists:
            with self.subTest(array=array):
                self.assertEqual(quick_sort_in_place(array.copy()), sorted(array))


if __name__ == '__main__':
    unittest.main()
