# coding: utf-8
import unittest

from problems.median_of_two_sorted_arrays import Solution
from problems.median_of_two_sorted_arrays import Solution2
from problems.median_of_two_sorted_arrays import Solution3


class TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test(self):
        array = [
            {'nums1': [1, 3], 'nums2': [2, ], 'expected': 2},
            {'nums1': [1, 2], 'nums2': [3, 4], 'expected': 2.5},
            {'nums1': [0, 0], 'nums2': [0, 0], 'expected': 0},
            {'nums1': [], 'nums2': [1, ], 'expected': 1},
            {'nums1': [2, ], 'nums2': [], 'expected': 2},
        ]
        for data in array:
            nums1 = data['nums1']
            nums2 = data['nums2']
            expected = data['expected']
            with self.subTest(nums1=nums1, nums2=nums2):
                self.assertEqual(self.solution.findMedianSortedArrays(nums1, nums2), expected)


class TestCase2(unittest.TestCase):
    def setUp(self):
        self.solution = Solution2()

    def test(self):
        array = [
            {'nums1': [1, 3], 'nums2': [2, ], 'expected': 2},
            {'nums1': [1, 2], 'nums2': [3, 4], 'expected': 2.5},
            {'nums1': [0, 0], 'nums2': [0, 0], 'expected': 0},
            {'nums1': [], 'nums2': [1, ], 'expected': 1},
            {'nums1': [2, ], 'nums2': [], 'expected': 2},
        ]
        for data in array:
            nums1 = data['nums1']
            nums2 = data['nums2']
            expected = data['expected']
            with self.subTest(nums1=nums1, nums2=nums2):
                self.assertEqual(self.solution.findMedianSortedArrays(nums1, nums2), expected)


class TestCase3(unittest.TestCase):
    def setUp(self):
        self.solution = Solution3()

    def test(self):
        array = [
            {'nums1': [1, 3], 'nums2': [2, ], 'expected': 2},
            {'nums1': [1, 2], 'nums2': [3, 4], 'expected': 2.5},
            {'nums1': [0, 0], 'nums2': [0, 0], 'expected': 0},
            {'nums1': [], 'nums2': [1, ], 'expected': 1},
            {'nums1': [2, ], 'nums2': [], 'expected': 2},
        ]
        for data in array:
            nums1 = data['nums1']
            nums2 = data['nums2']
            expected = data['expected']
            with self.subTest(nums1=nums1, nums2=nums2):
                self.assertEqual(self.solution.findMedianSortedArrays(nums1, nums2), expected)


if __name__ == '__main__':
    unittest.main()
