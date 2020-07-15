# coding: utf-8
import unittest

from problems.best_time_to_buy_and_sell_stock import Solution
from problems.best_time_to_buy_and_sell_stock import Solution2


class TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test(self):
        prices = [7, 1, 5, 3, 6, 4]
        self.assertEqual(self.solution.maxProfit(prices), 5)


class TestCase2(unittest.TestCase):
    def setUp(self):
        self.solution = Solution2()

    def test(self):
        prices = [7, 1, 5, 3, 6, 4]
        self.assertEqual(self.solution.maxProfit(prices), 5)


if __name__ == '__main__':
    unittest.main()
