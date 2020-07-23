# coding: utf-8
import random
import unittest

from algorithms.searching.linear_search import linear_search


class TestCase(unittest.TestCase):
    def test(self):
        array = [random.randint(-100, 100) for i in range(10000)]
        target = random.choice(array)
        expected = array.index(target)
        self.assertEqual(linear_search(array, target), expected)

    def test2(self):
        array = [random.randint(-100, 100) for i in range(10000)]
        target = 999
        expected = -1
        self.assertEqual(linear_search(array, target), expected)

    def test3(self):
        array = []
        target = 0
        expected = -1
        self.assertEqual(linear_search(array, target), expected)


if __name__ == '__main__':
    unittest.main()
