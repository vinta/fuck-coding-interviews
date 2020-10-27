# coding: utf-8
import unittest

from problems.reverse_string import Solution


class TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test(self):
        test_data = [
            {'s': ['h', 'e', 'l', 'l', 'o']},
            {'s': ['H', 'a', 'n', 'n', 'a', 'h']},
        ]
        for data in test_data:
            s = data['s']
            expected = list(reversed(s))
            with self.subTest(s=s):
                self.solution.reverseString(s)
                self.assertEqual(s, expected)


if __name__ == '__main__':
    unittest.main()
