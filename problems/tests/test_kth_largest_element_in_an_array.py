# coding: utf-8
import unittest

from problems.kth_largest_element_in_an_array import Solution
from problems.kth_largest_element_in_an_array import Solution2
from problems.kth_largest_element_in_an_array import Solution3


class TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test(self):
        test_data = [
            {'nums': [3, 2, 1, 5, 6, 4], 'k': 2, 'expected': 5},
            {'nums': [3, 2, 3, 1, 2, 4, 5, 5, 6], 'k': 4, 'expected': 4},
        ]
        for data in test_data:
            nums = data['nums']
            k = data['k']
            expected = data['expected']
            with self.subTest(nums=nums, k=k):
                self.assertEqual(self.solution.findKthLargest(nums, k), expected)


class TestCase2(unittest.TestCase):
    def setUp(self):
        self.solution = Solution2()

    def test(self):
        test_data = [
            {'nums': [3, 2, 1, 5, 6, 4], 'k': 2, 'expected': 5},
            {'nums': [3, 2, 3, 1, 2, 4, 5, 5, 6], 'k': 4, 'expected': 4},
        ]
        for data in test_data:
            nums = data['nums']
            k = data['k']
            expected = data['expected']
            with self.subTest(nums=nums, k=k):
                self.assertEqual(self.solution.findKthLargest(nums, k), expected)


class TestCase3(unittest.TestCase):
    def setUp(self):
        self.solution = Solution3()

    def test(self):
        test_data = [
            {'nums': [3, 2, 1, 5, 6, 4], 'k': 2, 'expected': 5},
            {'nums': [3, 2, 3, 1, 2, 4, 5, 5, 6], 'k': 4, 'expected': 4},
        ]
        for data in test_data:
            nums = data['nums']
            k = data['k']
            expected = data['expected']
            with self.subTest(nums=nums, k=k):
                self.assertEqual(self.solution.findKthLargest(nums, k), expected)


if __name__ == '__main__':
    unittest.main()
