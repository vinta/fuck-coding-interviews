# coding: utf-8
import unittest

from problems.best_time_to_buy_and_sell_stock import Solution
from problems.best_time_to_buy_and_sell_stock import Solution2
from problems.best_time_to_buy_and_sell_stock import Solution3


class TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test(self):
        test_data = [
            {'prices': [7, 1, 5, 3, 6, 4], 'expected': 5},
            {'prices': [7, 6, 4, 3, 1], 'expected': 0},
            {'prices': [1, ], 'expected': 0},
            {'prices': [], 'expected': 0},
        ]
        for data in test_data:
            prices = data['prices']
            expected = data['expected']
            with self.subTest(prices=prices, expected=expected):
                self.assertEqual(self.solution.maxProfit(prices), expected)


class TestCase2(unittest.TestCase):
    def setUp(self):
        self.solution = Solution2()

    def test(self):
        test_data = [
            {'prices': [7, 1, 5, 3, 6, 4], 'expected': 5},
            {'prices': [7, 6, 4, 3, 1], 'expected': 0},
            {'prices': [1, ], 'expected': 0},
            {'prices': [], 'expected': 0},
        ]
        for data in test_data:
            prices = data['prices']
            expected = data['expected']
            with self.subTest(prices=prices, expected=expected):
                self.assertEqual(self.solution.maxProfit(prices), expected)


class TestCase3(unittest.TestCase):
    def setUp(self):
        self.solution = Solution3()

    def test(self):
        test_data = [
            {'prices': [7, 1, 5, 3, 6, 4], 'expected': 5},
            {'prices': [7, 6, 4, 3, 1], 'expected': 0},
            {'prices': [1, ], 'expected': 0},
            {'prices': [], 'expected': 0},
        ]
        for data in test_data:
            prices = data['prices']
            expected = data['expected']
            with self.subTest(prices=prices, expected=expected):
                self.assertEqual(self.solution.maxProfit(prices), expected)

if __name__ == '__main__':
    unittest.main()
