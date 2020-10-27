# coding: utf-8
import unittest

from problems.sock_merchant import sockMerchant


class TestCase(unittest.TestCase):
    def test(self):
        test_data = [
            {'n': 9, 'ar': [10, 20, 20, 10, 10, 30, 50, 10, 20], 'expected': 3},
        ]
        for data in test_data:
            n = data['n']
            ar = data['ar']
            expected = data['expected']
            with self.subTest(n=n, ar=ar):
                self.assertEqual(sockMerchant(n, ar), expected)


if __name__ == '__main__':
    unittest.main()
