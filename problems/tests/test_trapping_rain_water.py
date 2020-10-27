# coding: utf-8
import unittest

from problems.trapping_rain_water import Solution


class TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test(self):
        test_data = [
            {'height': [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 'expected': 6},
            {'height': [4, 2, 0, 3, 2, 5], 'expected': 9},
            {'height': [1, 1, 1], 'expected': 0},
        ]
        for data in test_data:
            height = data['height']
            expected = data['expected']
            with self.subTest(height=height):
                self.assertEqual(self.solution.trap(height), expected)


if __name__ == '__main__':
    unittest.main()
