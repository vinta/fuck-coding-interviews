# coding: utf-8
import unittest

from problems.valid_parentheses import Solution


class TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test(self):
        s = '()[]{}'
        self.assertEqual(self.solution.isValid(s), True)

    def test2(self):
        s = '{[]}'
        self.assertEqual(self.solution.isValid(s), True)

    def test3(self):
        s = '([)]'
        self.assertEqual(self.solution.isValid(s), False)

    def test4(self):
        s = '){'
        self.assertEqual(self.solution.isValid(s), False)


if __name__ == '__main__':
    unittest.main()
