# coding: utf-8
"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
"""
from typing import List
import unittest


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for day, price in enumerate(prices):
            for other_price in prices[day + 1:]:
                if (other_price - price) > max_profit:
                    max_profit = other_price - price
        return max_profit


class Solution2:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        buy_price = prices[0]
        max_profit = 0
        for price in prices[1:]:
            if price < buy_price:
                buy_price = price
            else:
                profit = price - buy_price
                if profit > max_profit:
                    max_profit = profit
        return max_profit


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


unittest.main()
