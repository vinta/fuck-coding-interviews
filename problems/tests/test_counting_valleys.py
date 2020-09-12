# coding: utf-8
import unittest

from problems.counting_valleys import countingValleys


class TestCase(unittest.TestCase):
    def test(self):
        array = [
            {'path': 'UDDDUDUU', 'expected': 1},
            {'path': 'DDUUDDUDUUUD', 'expected': 2},
        ]
        for data in array:
            path = data['path']
            expected = data['expected']
            with self.subTest(path=path):
                self.assertEqual(countingValleys(len(path), path), expected)


if __name__ == '__main__':
    unittest.main()
