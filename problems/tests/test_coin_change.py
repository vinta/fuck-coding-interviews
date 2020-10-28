# coding: utf-8
import unittest

from problems.coin_change import Solution
from problems.coin_change import Solution2
from problems.coin_change import Solution3


class TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test(self):
        test_data = [
            {'coins': [1, 2, 5], 'amount': 11, 'expected': 3},
            {'coins': [1, 2, 5], 'amount': 10, 'expected': 2},
            {'coins': [2], 'amount': 3, 'expected': -1},
            {'coins': [1], 'amount': 0, 'expected': 0},
            {'coins': [1], 'amount': 1, 'expected': 1},
            {'coins': [1], 'amount': 2, 'expected': 2},
        ]
        for data in test_data:
            coins = data['coins']
            amount = data['amount']
            expected = data['expected']
            with self.subTest(coins=coins, amount=amount):
                self.assertEqual(self.solution.coinChange(coins, amount), expected)


class TestCase2(unittest.TestCase):
    def setUp(self):
        self.solution = Solution2()

    def test(self):
        test_data = [
            {'coins': [1, 2, 5], 'amount': 11, 'expected': 3},
            {'coins': [1, 2, 5], 'amount': 10, 'expected': 2},
            {'coins': [2], 'amount': 3, 'expected': -1},
            {'coins': [1], 'amount': 0, 'expected': 0},
            {'coins': [1], 'amount': 1, 'expected': 1},
            {'coins': [1], 'amount': 2, 'expected': 2},
        ]
        for data in test_data:
            coins = data['coins']
            amount = data['amount']
            expected = data['expected']
            with self.subTest(coins=coins, amount=amount):
                self.assertEqual(self.solution.coinChange(coins, amount), expected)


class TestCase3(unittest.TestCase):
    def setUp(self):
        self.solution = Solution3()

    def test(self):
        test_data = [
            {'coins': [1, 2, 5], 'amount': 11, 'expected': 3},
            {'coins': [1, 2, 5], 'amount': 10, 'expected': 2},
            {'coins': [2], 'amount': 3, 'expected': -1},
            {'coins': [1], 'amount': 0, 'expected': 0},
            {'coins': [1], 'amount': 1, 'expected': 1},
            {'coins': [1], 'amount': 2, 'expected': 2},
        ]
        for data in test_data:
            coins = data['coins']
            amount = data['amount']
            expected = data['expected']
            with self.subTest(coins=coins, amount=amount):
                self.assertEqual(self.solution.coinChange(coins, amount), expected)


if __name__ == '__main__':
    unittest.main()
