# coding: utf-8
import unittest

from problems.hackerrank_in_a_string import hackerrankInString


class TestCase(unittest.TestCase):
    def test(self):
        array = [
            {'s': 'hereiamstackerrank', 'expected': 'YES'},
            {'s': 'hackerworld', 'expected': 'NO'},
            {'s': 'hhaacckkekraraannk', 'expected': 'YES'},
            {'s': 'rhbaasdndfsdskgbfefdbrsdfhuyatrjtcrtyytktjjt', 'expected': 'NO'},
        ]
        for data in array:
            s = data['s']
            expected = data['expected']
            with self.subTest(s=s):
                self.assertEqual(hackerrankInString(s), expected)


if __name__ == '__main__':
    unittest.main()
