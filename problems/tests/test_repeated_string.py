# coding: utf-8
import unittest

from problems.repeated_string import repeatedString


class TestCase(unittest.TestCase):
    def test(self):
        array = [
            {'s': 'aba', 'n': 10, 'expected': 7},
            {'s': 'a', 'n': 1000000000000, 'expected': 1000000000000},
        ]
        for data in array:
            s = data['s']
            n = data['n']
            expected = data['expected']
            with self.subTest(s=s, n=n):
                self.assertEqual(repeatedString(s, n), expected)


if __name__ == '__main__':
    unittest.main()
