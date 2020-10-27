# coding: utf-8
import unittest

from problems.valid_parentheses import Solution


class TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test(self):
        test_data = [
            {'s': '()[]{}', 'expected': True},
            {'s': '{[]}', 'expected': True},
            {'s': '([)]', 'expected': False},
            {'s': ')(]', 'expected': False},
            {'s': '){', 'expected': False},
            {'s': '[', 'expected': False},
            {'s': '}', 'expected': False},
        ]
        for data in test_data:
            s = data['s']
            expected = data['expected']
            with self.subTest(s=s):
                self.assertEqual(self.solution.isValid(s), expected)


if __name__ == '__main__':
    unittest.main()
