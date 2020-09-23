# coding: utf-8
import unittest

from problems.mars_exploration import marsExploration


class TestCase(unittest.TestCase):
    def test(self):
        array = [
            {'message': 'SOSSPSSQSSOR', 'expected': 3},
            {'message': 'SOSSOT', 'expected': 1},
            {'message': 'SOSSOSSOS', 'expected': 0},
        ]
        for item in array:
            message = item['message']
            expected = item['expected']
            with self.subTest(message=message, expected=expected):
                self.assertEqual(marsExploration(message), expected)


if __name__ == '__main__':
    unittest.main()
