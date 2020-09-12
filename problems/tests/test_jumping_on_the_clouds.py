# coding: utf-8
import unittest

from problems.jumping_on_the_clouds import jumpingOnClouds


class TestCase(unittest.TestCase):
    def test(self):
        array = [
            {'c': [0, 0, 1, 0, 0, 1, 0], 'expected': 4},
            {'c': [0, 0, 0, 1, 0, 0], 'expected': 3},
        ]
        for data in array:
            c = data['c']
            expected = data['expected']
            with self.subTest(c=c):
                self.assertEqual(jumpingOnClouds(c), expected)


if __name__ == '__main__':
    unittest.main()
