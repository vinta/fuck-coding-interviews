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

        # We check i and i + 1 in each loop,
        # so we only need length - 1 loops to cover all items
        for i in range(0, length - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True

        # We sort one item in each iteration,
        # so the length of remaining unsorted items is reduced by 1
        length = length - 1

    return arr


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
                self.assertEqual(bubble_sort(array.copy()), sorted(array))


if __name__ == '__main__':
    unittest.main()
