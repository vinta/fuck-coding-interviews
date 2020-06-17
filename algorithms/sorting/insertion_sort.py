# coding: utf-8
"""
Insertion Sort
https://en.wikipedia.org/wiki/Insertion_sort

Worst-case Complexity: О(N^2) comparisons and swaps
Best-case Complexity: O(n) comparisons, O(1) swaps
Average Complexity: О(N^2) comparisons and swaps
"""
import unittest


def insertion_sort(arr):
    # Assume that arr[0] is already sorted, so start from arr[1]
    for i in range(1, len(arr)):
        # Iterate "the sorted part" backward, and find the correct position for arr[i]
        while (i > 0) and (arr[i] < arr[i - 1]):
            # If we use for loop above, we will have to run `i` steps for every unsorted element
            # However, arr[i] > arr[i - 1] means arr[i] is already in the right position
            # No need to check remaining elements of the sorted part
            arr[i], arr[i - 1] = arr[i - 1], arr[i]
            i = i - 1
    return arr


class TestCase(unittest.TestCase):
    def test(self):
        array = [5, 7, 1, 9, 5, -4, 3, 0, 2]
        expected = [-4, 0, 1, 2, 3, 5, 5, 7, 9]
        self.assertEqual(insertion_sort(array), expected)

    def test2(self):
        array = [1, 2, 3]
        expected = [1, 2, 3]
        self.assertEqual(insertion_sort(array), expected)

    def test3(self):
        array = [1, ]
        expected = [1, ]
        self.assertEqual(insertion_sort(array), expected)

    def test4(self):
        array = []
        expected = []
        self.assertEqual(insertion_sort(array), expected)


unittest.main()
