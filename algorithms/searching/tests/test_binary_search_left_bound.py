# coding: utf-8
import random
import unittest

from algorithms.searching.binary_search_left_bound import binary_search_left_bound


class TestCase(unittest.TestCase):
    def test(self):
        test_lists = [
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            [1, 2, 2, 2, 2, 3, 4],
            [1, 1, 1, 2, 2, 2, 3, 3, 3],
            [3],
            [3, 3],
            [3] * random.randint(1, 10),
        ]
        for array in test_lists:
            with self.subTest(array=array):
                target = random.choice(array)
                expected = array.index(target)
                self.assertEqual(binary_search_left_bound(array, target), expected)

                target = 100
                expected = -1
                self.assertEqual(binary_search_left_bound(array, target), expected)

    def test2(self):
        array = []
        target = 0
        expected = -1
        self.assertEqual(binary_search_left_bound(array, target), expected)

    def test3(self):
        array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        target = 100
        expected = -1
        self.assertEqual(binary_search_left_bound(array, target), expected)


if __name__ == '__main__':
    unittest.main()
