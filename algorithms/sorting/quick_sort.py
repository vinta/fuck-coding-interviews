# coding: utf-8
"""
Quick Sort
https://en.wikipedia.org/wiki/Quicksort

Worst-case Complexity: O(n^2)
Best-case Complexity: O(n * log(n))
Average Complexity: O(n * log(n))
"""
import random
import unittest


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        # Select the last item as the pivot
        pivot = arr.pop()

        # Partition the other elements into two sublists,
        # According to whether they are less than or greater than the pivot
        left_list = []
        right_list = []
        for item in arr:
            # There might be duplicates of pivot
            if item <= pivot:
                left_list.append(item)
            else:
                right_list.append(item)

        # The sublists are then sorted recursively
        return quick_sort(left_list) + [pivot, ] + quick_sort(right_list)


def quick_sort2(arr):
    if len(arr) <= 1:
        return arr
    else:
        # Select a random item as the pivot
        rand_index = random.randint(0, len(arr) - 1)
        pivot = arr.pop(rand_index)

        left_list = []
        right_list = []
        for item in arr:
            if item <= pivot:
                left_list.append(item)
            else:
                right_list.append(item)
        return quick_sort(left_list) + [pivot, ] + quick_sort(right_list)


class TestCase(unittest.TestCase):
    def test(self):
        array = [5, 7, 1, 9, 5, -4, 3, 0, 2]
        expected = [-4, 0, 1, 2, 3, 5, 5, 7, 9]
        self.assertEqual(quick_sort(array), expected)

    def test2(self):
        array = [1, 2, 3]
        expected = [1, 2, 3]
        self.assertEqual(quick_sort(array), expected)

    def test3(self):
        array = [1, ]
        expected = [1, ]
        self.assertEqual(quick_sort(array), expected)

    def test4(self):
        array = []
        expected = []
        self.assertEqual(quick_sort(array), expected)


class TestCase2(unittest.TestCase):
    def test(self):
        array = [5, 7, 1, 9, 5, -4, 3, 0, 2]
        expected = [-4, 0, 1, 2, 3, 5, 5, 7, 9]
        self.assertEqual(quick_sort2(array), expected)

    def test2(self):
        array = [1, 2, 3]
        expected = [1, 2, 3]
        self.assertEqual(quick_sort2(array), expected)

    def test3(self):
        array = [1, ]
        expected = [1, ]
        self.assertEqual(quick_sort2(array), expected)

    def test4(self):
        array = []
        expected = []
        self.assertEqual(quick_sort2(array), expected)


unittest.main()
