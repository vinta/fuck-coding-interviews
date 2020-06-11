# coding: utf-8
"""
Bubble Sort

Worst-case Complexity: O(n^2)
Best-case Complexity: O(n) (the input array is already sorted)
Average Complexity: O(n^2)
"""
import unittest


def bubble_sort(arr):
    length = len(arr)

    swapped = True
    while swapped:
        swapped = False

        # we check `i` and `i + 1` in each loop, so we only need `length - 1` loops to cover all items
        for i in range(0, length - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True

        # we sort one item in each iteration, so the length of remaining unsorted items is reduced by 1
        length = length - 1

    return arr


class TestCase(unittest.TestCase):
    def test(self):
        array = [5, 7, 1, 9, 5, -4, 3, 0, 2]
        expected = [-4, 0, 1, 2 ,3, 5, 5, 7, 9]
        self.assertEqual(bubble_sort(array), expected)

    def test2(self):
        array = [1, 2, 3]
        expected = [1, 2, 3]
        self.assertEqual(bubble_sort(array), expected)

    def test3(self):
        array = [1, ]
        expected = [1, ]
        self.assertEqual(bubble_sort(array), expected)

    def test4(self):
        array = []
        expected = []
        self.assertEqual(bubble_sort(array), expected)


unittest.main()
