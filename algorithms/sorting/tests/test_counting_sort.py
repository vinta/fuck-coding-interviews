# coding: utf-8
import random
import unittest

from algorithms.sorting.counting_sort import counting_sort


class TestCase(unittest.TestCase):
    def test(self):
        test_lists = [
            [5, 7, 1, 9, 5, 5, 3, 0, 2, 3, 6, 3, 8],
            [],
            [1, ],
            [1, 2],
            [1, 2, 3],
            [3, 2, 1],
            [1, 2, 3, 4],
            [4, 3, 2, 1],
            [1, 1, 1, 1],
            [random.randint(0, 100) for i in range(1000)],
        ]
        for array in test_lists:
            with self.subTest(array=array):
                self.assertEqual(counting_sort(array.copy()), sorted(array))


if __name__ == '__main__':
    unittest.main()
