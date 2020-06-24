# coding: utf-8
"""
Quick Sort
https://en.wikipedia.org/wiki/Quicksort

Worst-case Complexity: O(n^2)
Best-case Complexity: O(n * log(n))
Average Complexity: O(n * log(n))
"""
import unittest


def quick_sort(arr):
    # Partition is to move all items that less than the pivot to the left side of the pivot,
    # and move all items that greater than the pivot to the right side of the pivot
    # As a result, the pivot is in the correct index,
    # but items in both sides of the pivot don't necessarily end up sorted
    def partition(arr, start, end):
        # Select the first item as the pivot,
        # So the left cursor starts from the next index of the pivot
        pivot_index = start
        pivot = arr[pivot_index]
        left = start + 1
        right = end

        while True:
            # If the current item is less than or equal to the pivot,
            # it's in the proper side (left side of the pivot),
            # then we move the left cursor right to the next element
            while left <= right and arr[left] <= pivot:
                # The left cursor stops at the item which is greater than the pivot
                left = left + 1

            # If the current item is greater than or equal to the pivot,
            # it's in the proper side (right side of the pivot),
            # then we move the right cursor left to the next element
            while left <= right and arr[right] >= pivot:
                # The right cursor stops at the item which is less than the pivot
                right = right - 1

            # We find items for both left and right cursor that are in the wrong side,
            # so we swap them ("the leftmost item which greater than pivot" and "the rightmost item which less than the pivot"),
            # In the end, we move all items to their proper side of the pivot
            if left <= right:
                arr[left], arr[right] = arr[right], arr[left]
            else:
                break

        # We swap the pivot with the right cursor,
        # so the pivot ends up in the correct index
        if pivot_index != right:
            arr[pivot_index], arr[right] = arr[right], arr[pivot_index]
            pivot_index = right

        return pivot_index

    def quick_sort_range(arr, start, end):
        # base case
        if start >= end:
            return arr

        # recursive case
        pivot_index = partition(arr, start, end)
        quick_sort_range(arr, start, pivot_index - 1)
        quick_sort_range(arr, pivot_index + 1, end)
        return arr

    return quick_sort_range(arr, 0, len(arr) - 1)


def quick_sort2(arr):
    if len(arr) <= 1:
        return arr
    else:
        # Select the first item as the pivot
        pivot = arr[0]

        # Partition the other elements into two sublists,
        # According to whether they are less than or greater than the pivot
        left_list = []
        right_list = []

        # There might be duplicates of pivot
        pivot_list = []
        for item in arr:
            if item < pivot:
                left_list.append(item)
            elif item > pivot:
                right_list.append(item)
            else:
                pivot_list.append(item)

        # Sublists are then sorted recursively
        return quick_sort2(left_list) + pivot_list + quick_sort2(right_list)


class TestCase(unittest.TestCase):
    def test(self):
        array = [5, 7, 1, 9, 5, 5, -4, 3, 0, 2]
        expected = [-4, 0, 1, 2, 3, 5, 5, 5, 7, 9]
        self.assertEqual(quick_sort(array), expected)

    def test2(self):
        array = []
        expected = []
        self.assertEqual(quick_sort(array), expected)

    def test3(self):
        array = [1, ]
        expected = [1, ]
        self.assertEqual(quick_sort(array), expected)

    def test4(self):
        array = [1, 2, 3]
        expected = [1, 2, 3]
        self.assertEqual(quick_sort(array), expected)

    def test5(self):
        array = [3, 2, 1]
        expected = [1, 2, 3]
        self.assertEqual(quick_sort(array), expected)


class TestCase2(unittest.TestCase):
    def test(self):
        array = [5, 7, 1, 9, 5, -4, 3, 0, 2]
        expected = [-4, 0, 1, 2, 3, 5, 5, 7, 9]
        self.assertEqual(quick_sort2(array), expected)

    def test2(self):
        array = []
        expected = []
        self.assertEqual(quick_sort2(array), expected)

    def test3(self):
        array = [1, ]
        expected = [1, ]
        self.assertEqual(quick_sort2(array), expected)

    def test4(self):
        array = [1, 2, 3]
        expected = [1, 2, 3]
        self.assertEqual(quick_sort2(array), expected)

    def test5(self):
        array = [3, 2, 1]
        expected = [1, 2, 3]
        self.assertEqual(quick_sort2(array), expected)


unittest.main()
