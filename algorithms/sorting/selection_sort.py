# coding: utf-8
"""
Selection Sort
https://en.wikipedia.org/wiki/Selection_sort

Worst-case Complexity: О(n^2) comparisons, О(n) swaps
Best-case Complexity: О(n^2) comparisons, О(n) swaps
Average Complexity: О(n^2) comparisons, О(n) swaps
"""
import unittest


def selection_sort(arr):
    sorted_arr = []

    def find_min_index(arr):
        if not arr:
            raise ValueError('The array is empty')

        min_index = 0
        for i, item in enumerate(arr):
            if item < arr[min_index]:
                min_index = i
        return min_index

    # The length of arr is reduced by 1 every loop because of arr.pop()
    for _ in range(len(arr)):
        # Find the smallest item in the unsorted list,
        index = find_min_index(arr)
        # Move it to the sorted list
        sorted_arr.append(arr.pop(index))

    return sorted_arr


def selection_sort2(arr):
    length = len(arr)
    for i in range(length - 1):
        # Find the smallest item in the unsorted sublist
        min_index = i
        for j in range(i + 1, length):
            if arr[j] < arr[min_index]:
                min_index = j

        # Swap the smallest item with the leftmost item of the unsorted sublist
        if min_index != i:
            # arr[i] belongs to the sorted sublist
            arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


class TestCase(unittest.TestCase):
    def test(self):
        array = [5, 7, 1, 9, 5, -4, 3, 0, 2]
        expected = [-4, 0, 1, 2, 3, 5, 5, 7, 9]
        self.assertEqual(selection_sort(array), expected)

    def test2(self):
        array = [1, 2, 3]
        expected = [1, 2, 3]
        self.assertEqual(selection_sort(array), expected)

    def test3(self):
        array = [1, ]
        expected = [1, ]
        self.assertEqual(selection_sort(array), expected)

    def test4(self):
        array = []
        expected = []
        self.assertEqual(selection_sort(array), expected)


class TestCase2(unittest.TestCase):
    def test(self):
        array = [5, 7, 1, 9, 5, -4, 3, 0, 2]
        expected = [-4, 0, 1, 2 ,3, 5, 5, 7, 9]
        self.assertEqual(selection_sort2(array), expected)

    def test2(self):
        array = [1, 2, 3]
        expected = [1, 2, 3]
        self.assertEqual(selection_sort2(array), expected)

    def test3(self):
        array = [1, ]
        expected = [1, ]
        self.assertEqual(selection_sort2(array), expected)

    def test4(self):
        array = []
        expected = []
        self.assertEqual(selection_sort2(array), expected)


unittest.main()
