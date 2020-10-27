# coding: utf-8
import unittest

from problems.fizz_buzz import Solution


class TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test(self):
        test_data = [
            {'n': 1, 'expected': ['1', ]},
            {'n': 15, 'expected': ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13', '14', 'FizzBuzz']},
            {'n': 31, 'expected': ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13', '14', 'FizzBuzz', '16', '17', 'Fizz', '19', 'Buzz', 'Fizz', '22', '23', 'Fizz', 'Buzz', '26', 'Fizz', '28', '29', 'FizzBuzz', '31']},
            {'n': 0, 'expected': []},
            {'n': -15, 'expected': []},
        ]
        for data in test_data:
            n = data['n']
            expected = data['expected']
            with self.subTest(n=n):
                self.assertEqual(list(self.solution.fizzBuzz(n)), expected)


if __name__ == '__main__':
    unittest.main()
