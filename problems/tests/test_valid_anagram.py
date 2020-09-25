# coding: utf-8
import unittest

from problems.valid_anagram import Solution
from problems.valid_anagram import Solution2
from problems.valid_anagram import Solution3


class TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test(self):
        test_data = [
            {'s': 'anagram', 't': 'nagaram', 'expected': True},
            {'s': 'abc', 't': 'ab', 'expected': False},
        ]
        for data in test_data:
            s = data['s']
            t = data['t']
            expected = data['expected']
            with self.subTest(s=s, t=t, expected=expected):
                self.assertEqual(self.solution.isAnagram(s, t), expected)


class TestCase2(unittest.TestCase):
    def setUp(self):
        self.solution = Solution2()

    def test(self):
        test_data = [
            {'s': 'anagram', 't': 'nagaram', 'expected': True},
            {'s': 'abc', 't': 'ab', 'expected': False},
        ]
        for data in test_data:
            s = data['s']
            t = data['t']
            expected = data['expected']
            with self.subTest(s=s, t=t, expected=expected):
                self.assertEqual(self.solution.isAnagram(s, t), expected)


class TestCase3(unittest.TestCase):
    def setUp(self):
        self.solution = Solution3()

    def test(self):
        test_data = [
            {'s': 'anagram', 't': 'nagaram', 'expected': True},
            {'s': 'abc', 't': 'ab', 'expected': False},
        ]
        for data in test_data:
            s = data['s']
            t = data['t']
            expected = data['expected']
            with self.subTest(s=s, t=t, expected=expected):
                self.assertEqual(self.solution.isAnagram(s, t), expected)


if __name__ == '__main__':
    unittest.main()
