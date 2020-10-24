# coding: utf-8
import random
import unittest


from algorithms.sorting.selection_sort import selection_sort
from algorithms.sorting.selection_sort import selection_sort_in_place


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
            [random.randint(-100, 100) for i in range(1000)],
        ]
        for array in test_lists:
            with self.subTest(array=array):
                self.assertEqual(selection_sort(array.copy()), sorted(array))


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
            [random.randint(-100, 100) for i in range(1000)],
        ]
        for array in test_lists:
            with self.subTest(array=array):
                self.assertEqual(selection_sort_in_place(array.copy()), sorted(array))


if __name__ == '__main__':
    unittest.main()
