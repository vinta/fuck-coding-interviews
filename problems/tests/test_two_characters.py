# coding: utf-8
import unittest

from problems.two_characters import alternate


class TestCase(unittest.TestCase):
    def test(self):
        test_data = [
            {'s': 'beabeefeab', 'expected': 5},
            {'s': 'asdcbsdcagfsdbgdfanfghbsfdab', 'expected': 8},
            {'s': 'asvkugfiugsalddlasguifgukvsa', 'expected': 0},
        ]
        for data in test_data:
            s = data['s']
            expected = data['expected']
            with self.subTest(s=s):
                self.assertEqual(alternate(s), expected)


if __name__ == '__main__':
    unittest.main()
