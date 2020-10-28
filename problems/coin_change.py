# coding: utf-8
"""
https://leetcode.com/problems/coin-change/
"""
from itertools import combinations
from typing import List


# Time Limit Exceeded.
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        if min(coins) > amount:
            return -1

        # Generate all subsets.
        def build_subsets(items):
            subsets = set()
            for i in range(1, len(items) + 1):
                subsets |= set(combinations(items, i))
            return subsets

        items = []
        for coin in coins:
            max_n = amount // coin
            items.extend([coin, ] * max_n)

        min_n = float('inf')
        for result in build_subsets(items):
            n = len(result)
            if n > min_n:
                continue
            if sum(result) == amount:
                if n < min_n:
                    min_n = n

        if min_n == float('inf'):
            return -1
        else:
            return min_n


class Solution2:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Numbers of coins for amount [0, ..., amount].
        coins_n = [float('inf'), ] * (amount + 1)
        coins_n[0] = 0

        for coin in coins:
            for current_amount in range(coin, amount + 1):  # [coin, ..., amount]
                # The number of coins before adding the current coin to it.
                previous_n = coins_n[current_amount - coin]
                current_n = previous_n + 1
                if coins_n[current_amount] > current_n:
                    coins_n[current_amount] = current_n

        if coins_n[amount] == float('inf'):
            return -1
        else:
            return coins_n[amount]


class Solution3:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Numbers of coins for amount [0, ..., amount].
        coins_n = [float('inf'), ] * (amount + 1)
        coins_n[0] = 0

        sorted_coins = sorted(coins)

        # Iterate every needed amount.
        for current_amount in range(1, amount + 1):
            for coin in sorted_coins:
                if coin > current_amount:
                    break

                # The number of coins before adding the current coin to it.
                previous_n = coins_n[current_amount - coin]
                # Add 1 of the current coin.
                current_n = previous_n + 1
                if coins_n[current_amount] > current_n:
                    coins_n[current_amount] = current_n

        if coins_n[amount] == float('inf'):
            return -1
        else:
            return coins_n[amount]
