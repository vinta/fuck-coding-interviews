# coding: utf-8
import random
import unittest


def binary_search_left_bound(array, target):
    left = 0
    right = len(array) - 1
    while left <= right:
        mid = int((left + right) / 2)
        mid_value = array[mid]
        if target == mid_value:
            if mid > 0 and array[mid - 1] == target:
                left = mid - 1
                right = mid
            else:
                return mid
        elif target > mid_value:
            left = mid + 1
        elif target < mid_value:
            right = mid - 1

    return -1


class TestCase(unittest.TestCase):
    def test(self):
        test_lists = [
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            [1, 2, 2, 2, 2, 3, 4],
            [1, 1, 1, 2, 2, 2, 3, 3, 3],
            [3] * random.randint(0, 100000),
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
        array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        target = 100
        expected = -1
        self.assertEqual(binary_search_left_bound(array, target), expected)


if __name__ == '__main__':
    unittest.main()
