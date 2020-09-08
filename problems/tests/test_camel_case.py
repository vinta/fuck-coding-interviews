# coding: utf-8
import unittest

from problems.camel_case import camelcase


class TestCase(unittest.TestCase):
    def test(self):
        test_data = [
            {'input': 'saveChangesInTheEditor', 'expected': 5},
        ]
        for data in test_data:
            s = data['input']
            expected = data['expected']
            with self.subTest(s=s, expected=expected):
                self.assertEqual(camelcase(s), expected)


if __name__ == '__main__':
    unittest.main()
