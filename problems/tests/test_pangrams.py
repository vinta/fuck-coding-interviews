# coding: utf-8
import unittest

from problems.pangrams import pangrams


class TestCase(unittest.TestCase):
    def test(self):
        test_array = [
            {'s': 'We promptly judged antique ivory buckles for the next prize', 'expected': 'pangram'},
            {'s': 'We promptly judged antique ivory buckles for the prize', 'expected': 'not pangram'},
        ]
        for data in test_array:
            s = data['s']
            expected = data['expected']
            with self.subTest(s=s):
                self.assertEqual(pangrams(s), expected)


if __name__ == '__main__':
    unittest.main()
