# coding: utf-8
"""
Quick Sort
https://en.wikipedia.org/wiki/Quicksort

Worst-case Complexity: O(n^2)
Best-case Complexity: O(n * log(n))
Average Complexity: O(n * log(n))
"""
import unittest


# https://en.wikipedia.org/wiki/Quicksort#Hoare_partition_scheme
def quick_sort(arr):
    # Partition is to move all items that less than the pivot to the left side of the pivot,
    # and move all items that greater than the pivot to the right side of the pivot
    # As a result, the pivot is in the correct index,
    # but items in both sides of the pivot don't necessarily end up sorted
    def partition(arr, start, end):
        # Select the middle item as the pivot
        pivot = arr[round((start + end) / 2)]
        left = start
        right = end
        while True:
            # If the current item is less than the pivot,
            # it's in the proper side (left side of the pivot),
            # then we move the left cursor right to the next element
            while arr[left] < pivot:
                # The left cursor stops at the item which is greater than or equal to the pivot
                left = left + 1

            # Behave oppositely to the left cursor
            while arr[right] > pivot:
                right = right - 1

            # We swap both items the left and right cursor found that are in the wrong side,
            # In the end, we move all items to their proper side of the pivot
            if left < right:
                arr[left], arr[right] = arr[right], arr[left]
                # Since we already swapped both items the left and right cursor pointed to
                # Cursors move to the next index
                left = left + 1
                right = right - 1
            else:
                # If left >= right, we exit the loop
                return right

    def quick_sort_range(arr, start, end):
        # Base case
        # the array of size 0 or 1 which (start, end) is (0, -1) or (0, 0)
        if start >= end:
            return arr

        # Recursive case
        partition_index = partition(arr, start, end)
        quick_sort_range(arr, start, partition_index - 1)
        quick_sort_range(arr, partition_index + 1, end)
        return arr

    return quick_sort_range(arr, 0, len(arr) - 1)


def quick_sort_extra_space(arr):
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
        return quick_sort_extra_space(left_list) + pivot_list + quick_sort_extra_space(right_list)


class TestCase(unittest.TestCase):
    def test(self):
        test_lists = [
            [5, 7, 1, 9, 5, 5, -4, 3, 0, 2],
            [],
            [1, ],
            [1, 2],
            [1, 2, 3],
            [3, 2, 1],
            [1, 2, 3, 4],
            [4, 3, 2, 1],
            [1, 1, 1, 1],
        ]
        for array in test_lists:
            with self.subTest(array=array):
                self.assertEqual(quick_sort(array.copy()), sorted(array))


class TestCase2(unittest.TestCase):
    def test(self):
        test_lists = [
            [5, 7, 1, 9, 5, 5, -4, 3, 0, 2],
            [],
            [1, ],
            [1, 2],
            [1, 2, 3],
            [3, 2, 1],
            [1, 1, 1, 1],
        ]
        for array in test_lists:
            with self.subTest(array=array):
                self.assertEqual(quick_sort_extra_space(array.copy()), sorted(array))


if __name__ == '__main__':
    unittest.main()
