# coding: utf-8
import unittest

from problems.valid_palindrome import Solution
from problems.valid_palindrome import Solution2


class TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test(self):
        test_data = [
            {'s': 'A man, a plan, a canal: Panama', 'expected': True},
            {'s': 'race a car', 'expected': False},
            {'s': '0P', 'expected': False},
            {'s': '', 'expected': True},
        ]
        for data in test_data:
            s = data['s']
            expected = data['expected']
            with self.subTest(s=s, expected=expected):
                self.assertEqual(self.solution.isPalindrome(s), expected)


class TestCase2(unittest.TestCase):
    def setUp(self):
        self.solution = Solution2()

    def test(self):
        test_data = [
            {'s': 'A man, a plan, a canal: Panama', 'expected': True},
            {'s': 'race a car', 'expected': False},
            {'s': '0P', 'expected': False},
            {'s': '', 'expected': True},
        ]
        for data in test_data:
            s = data['s']
            expected = data['expected']
            with self.subTest(s=s, expected=expected):
                self.assertEqual(self.solution.isPalindrome(s), expected)


if __name__ == '__main__':
    unittest.main()
