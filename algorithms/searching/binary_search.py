# coding: utf-8
import random
import unittest


def binary_search(array, target):
    low = 0
    high = len(array) - 1
    while low <= high:
        mid = int((low + high) / 2)
        mid_value = array[mid]
        if target < mid_value:
            high = mid - 1
        elif target > mid_value:
            low = mid + 1
        else:
            return mid

    return None


def binary_search_recursive(array, target):
    def binary_search_range(array, target, low, high):
        # Base case
        if low > high:
            return None

        # Recursive case
        mid = int((low + high) / 2)
        mid_value = array[mid]
        if target < mid_value:
            return binary_search_range(array, target, low, mid - 1)
        elif target > mid_value:
            return binary_search_range(array, target, mid + 1, high)
        else:
            return mid

    return binary_search_range(array, target, 0, len(array) - 1)


class TestCase(unittest.TestCase):
    def test(self):
        array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        target = random.choice(array)
        expected = array.index(target)
        self.assertEqual(binary_search(array, target), expected)

    def test2(self):
        array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        target = 100
        expected = None
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
        expected = None
        self.assertEqual(binary_search_recursive(array, target), expected)


if __name__ == '__main__':
    unittest.main()
