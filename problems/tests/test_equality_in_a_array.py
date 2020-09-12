# coding: utf-8
import unittest

from problems.equality_in_a_array import equalizeArray


class TestCase(unittest.TestCase):
    def test(self):
        array = [
            {'arr': [3, 3, 2, 1, 3], 'expected': 2},
        ]
        for data in array:
            arr = data['arr']
            expected = data['expected']
            with self.subTest(arr=arr):
                self.assertEqual(equalizeArray(arr), expected)


if __name__ == '__main__':
    unittest.main()
