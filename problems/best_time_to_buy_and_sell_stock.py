# coding: utf-8
"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
"""
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for day, buy_price in enumerate(prices):
            for sell_price in prices[day + 1:]:
                profit = sell_price - buy_price
                if profit > max_profit:
                    max_profit = profit
        return max_profit


# The Two-Pointer way.
class Solution2:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        length = len(prices)
        buy = 0
        sell = 1
        while buy < length and sell < length:
            if prices[sell] > prices[buy]:
                # sell price is higher than buy price
                profit = prices[sell] - prices[buy]
                if profit > max_profit:
                    max_profit = profit

                sell += 1
            else:
                # sell price is lower than or equeal to buy price
                buy = sell
                sell += 1

        return max_profit


class Solution3:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0

        max_profit = 0
        buy_price = prices[0]
        for sell_price in prices[1:]:
            if sell_price > buy_price:
                profit = sell_price - buy_price
                if profit > max_profit:
                    max_profit = profit
            else:
                buy_price = sell_price

        return max_profit
